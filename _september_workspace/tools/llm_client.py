"""
LLM 客户端 (V1 折中补 8-10 天真实工作量)
============================================

按 P-A V0 spec §3 + KT_A1_SPEC_V0 §3.1:
- LLM 玩家: Doubao (volces_ark_bytedance) + DeepSeek
- 4 选 1 决策(GSM8K / StrategyQA / 合成陷阱 / 2x2 矩阵)
- runtime 读 API key(Path().read_text()), 不入 prompt(7 条铁律)

实现:
- LLMStrategy 抽象基类
- DoubaoStrategy(火山引擎方舟 API)
- DeepSeekStrategy(DeepSeek API)
- LLMClient 工厂

V0.2 修复(P0, 2026-09-09):
- 禁止静默随机退化: 依赖缺失 / API 调用失败 / 返回解析失败 → 显式异常,
  删除 random.choice 兜底(铁律: LLM 客户端绝不随机退化)
- API key: 环境变量优先(Doubao=ARK_API_KEY, DeepSeek=DEEPSEEK_API_KEY),
  其次运行时读文件; 异常只报路径不报值, key 不入任何日志/异常文本
- transport 可注入: 离线 FakeTransport 全链路测试, 零真实 API 调用;
  生产 transport 用 openai SDK(方舟/DeepSeek 均为 openai 兼容端点),
  key 仅在生产 transport 内运行时读取(构造对象零副作用)
"""

from __future__ import annotations

import os
from abc import ABC, abstractmethod
from pathlib import Path

# 7 条铁律: runtime 读 API key, 不入 prompt
API_KEY_PATH = Path('C:/Users/Administrator/Desktop/AI/新建文本文档.txt')

# 环境变量名(env 优先于文件读取)
DOUBAO_ENV_KEY = 'ARK_API_KEY'
DEEPSEEK_ENV_KEY = 'DEEPSEEK_API_KEY'


def get_api_key(env_var: str | None = None) -> str:
    """runtime 读 API key(7 条铁律): 环境变量优先, 其次运行时读文件.

    key 不缓存, 每次重新读, 不写入任何 .py / .json / 验证脚本 / 日志;
    异常信息只含环境变量名与文件路径, 不含 key 值.
    支持多编码(UTF-8 / GBK / GB18030).
    """
    if env_var:
        val = os.environ.get(env_var, '')
        if val.strip():
            return val.strip()
    if not API_KEY_PATH.exists():
        raise FileNotFoundError(
            f'API key 未配置: 环境变量 {env_var or "(未指定)"} 未设置, '
            f'且 key 文件不存在: {API_KEY_PATH}'
        )
    for enc in ('utf-8', 'gbk', 'gb18030', 'utf-8-sig', 'latin-1'):
        try:
            return API_KEY_PATH.read_text(encoding=enc).strip()
        except (UnicodeDecodeError, LookupError):
            continue
    # 兜底: 二进制读 + 解码
    raw = API_KEY_PATH.read_bytes()
    return raw.decode('utf-8', errors='ignore').strip()


def _openai_transport(base_url: str, env_var: str, body: dict, timeout: int = 30) -> dict:
    """生产 transport: openai SDK 发请求, 返回统一 dict 结构.

    依赖缺失 / API 调用失败 → 显式异常(绝不静默退化);
    key 在此运行时读取(env 优先), 不缓存, 不入异常文本.
    """
    try:
        from openai import OpenAI
    except ImportError as e:
        raise ImportError(
            '依赖 openai 未安装, LLM 决策不可用(显式失败, 不做随机退化)'
        ) from e
    api_key = get_api_key(env_var)  # 每次重新读, 不缓存
    client = OpenAI(api_key=api_key, base_url=base_url, timeout=timeout)
    resp = client.chat.completions.create(
        model=body['model'],
        messages=body['messages'],
        temperature=body['temperature'],
        max_tokens=body['max_tokens'],
    )
    return {'choices': [{'message': {'content': resp.choices[0].message.content}}]}


class LLMStrategy(ABC):
    """LLM 玩家抽象基类"""

    @abstractmethod
    def decide(self, prompt: str, options: list[str], temperature: float = 0.0) -> str:
        """返回 4 选 1 的决策"""
        pass

    @abstractmethod
    def name(self) -> str:
        """返回 LLM 名称 (Doubao / DeepSeek)"""
        pass


class _ChatCompletionsStrategy(LLMStrategy):
    """chat/completions 协议通用实现(Doubao / DeepSeek 共用).

    transport 签名: (base_url, env_var, body, timeout) -> dict,
    返回结构须含 choices[0].message.content;
    测试时注入 FakeTransport 即可全链路离线运行.
    """

    base_url: str = ''
    env_var: str = ''
    default_model: str = ''

    def __init__(self, model: str | None = None, transport=None):
        self.model = model or self.default_model
        # transport 可注入(离线 FakeTransport); None = 生产 _openai_transport
        self._transport = transport

    def decide(self, prompt: str, options: list[str], temperature: float = 0.0) -> str:
        body = {
            'model': self.model,
            'messages': [
                {'role': 'system',
                 'content': f'You must choose exactly one option from: {options}. '
                            f'Respond with ONLY the option text, no explanation.'},
                {'role': 'user', 'content': prompt},
            ],
            'temperature': temperature,
            'max_tokens': 50,
        }
        transport = self._transport if self._transport is not None else _openai_transport
        # 依赖缺失 / API 调用失败 → 由 transport 显式抛异常, 此处不做任何兜底
        data = transport(self.base_url, self.env_var, body, 30)
        try:
            content = data['choices'][0]['message']['content'].strip()
        except (KeyError, IndexError, AttributeError, TypeError) as e:
            raise ValueError('LLM 返回结构异常, 缺少 choices[0].message.content') from e
        # 匹配最接近的 option
        for opt in options:
            if opt in content or content in opt:
                return opt
        # 解析失败 → 显式异常(拒绝静默选第一个选项)
        raise ValueError(f'LLM 返回内容无法匹配任何选项, 拒绝兜底: {content[:80]!r}')


class DoubaoStrategy(_ChatCompletionsStrategy):
    """Doubao (volces_ark_bytedance) via 火山引擎方舟 API(openai 兼容端点)"""

    base_url = 'https://ark.cn-beijing.volces.com/api/v3'
    env_var = DOUBAO_ENV_KEY
    default_model = 'doubao-pro-32k'

    def name(self) -> str:
        return 'Doubao'


class DeepSeekStrategy(_ChatCompletionsStrategy):
    """DeepSeek API(openai 兼容端点)"""

    base_url = 'https://api.deepseek.com'
    env_var = DEEPSEEK_ENV_KEY
    default_model = 'deepseek-chat'

    def name(self) -> str:
        return 'DeepSeek'


class LLMClient:
    """LLM 客户端工厂"""

    @staticmethod
    def create(strategy: str = 'doubao', transport=None) -> LLMStrategy:
        """创建 LLM 玩家; transport 可注入(离线 FakeTransport 测试用)."""
        if strategy == 'doubao':
            return DoubaoStrategy(transport=transport)
        elif strategy == 'deepseek':
            return DeepSeekStrategy(transport=transport)
        else:
            raise ValueError(f'Unknown strategy: {strategy}')


if __name__ == '__main__':
    # 自检: 零真实 API 调用, 用可注入的 FakeTransport 离线验证决策路径
    def _fake_transport(base_url, env_var, body, timeout):
        # 离线假传输: 不读 key, 不发网络请求, 返回可匹配 'No' 的内容
        return {'choices': [{'message': {'content': 'No'}}]}

    def _unmatched_transport(base_url, env_var, body, timeout):
        # 离线假传输: 返回无法匹配任何选项的内容(测解析失败路径)
        return {'choices': [{'message': {'content': 'zzz-unmatched-zzz'}}]}

    ok = True
    for strategy in ('doubao', 'deepseek'):
        client = LLMClient.create(strategy, transport=_fake_transport)
        decision = client.decide('self-test?', ['Yes', 'No'])
        print(f'{strategy}: decide -> {decision} (name={client.name()})')
        if decision != 'No':
            ok = False
        # 解析失败必须显式抛 ValueError, 不允许静默兜底
        bad = LLMClient.create(strategy, transport=_unmatched_transport)
        try:
            bad.decide('self-test?', ['Yes', 'No'])
            print(f'{strategy}: ERROR 解析失败未抛异常')
            ok = False
        except ValueError:
            print(f'{strategy}: 解析失败显式抛 ValueError OK')
    print('OK: FakeTransport 离线自检通过' if ok else 'FAIL: 离线自检未通过')
