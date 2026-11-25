#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Strict option parsing adapter for tools/llm_client.py (append-only).

The legacy parser accepts opt-in-content or content-in-opt, which can turn a
single letter or an explanatory sentence into a false option match. This module
keeps the original transports and credential behavior unchanged, but accepts
only an exact option string after surrounding whitespace is removed.
"""
import importlib.util
from pathlib import Path

def _dep_path(rel=""):
    """按名搜索：先在仓内候选根按相对路径找，再按件名全树找；皆不中则回原样。"""
    import os as _os
    from pathlib import Path as _P
    base = _P(__file__).resolve()
    roots = []
    for _i in range(1, 8):
        try:
            roots.append(base.parents[_i])
        except IndexError:
            break
    rel = rel.replace("\\", "/").lstrip("/")
    for _c in roots:
        if rel:
            _p = _c / rel
            if _p.exists():
                return str(_p)
    _name = rel.split("/")[-1] if rel else ""
    if _name:
        for _c in roots:
            for _dp, _dn, _fn in _os.walk(str(_c)):
                if _name in _fn:
                    return _os.path.join(_dp, _name)
    return rel


_SPEC = importlib.util.spec_from_file_location(
    "llm_client_anchor",
    Path(r_dep_path("tools/llm_client.py")),
)
_anchor = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(_anchor)


class _StrictOptionMixin:
    def decide(self, prompt: str, options: list[str], temperature: float = 0.0) -> str:
        body = {
            "model": self.model,
            "messages": [
                {
                    "role": "system",
                    "content": f"You must choose exactly one option from: {options}. Respond with ONLY the option text, no explanation.",
                },
                {"role": "user", "content": prompt},
            ],
            "temperature": temperature,
            "max_tokens": 50,
        }
        transport = self._transport if self._transport is not None else _anchor._openai_transport
        data = transport(self.base_url, self.env_var, body, 30)
        try:
            content = data["choices"][0]["message"]["content"].strip()
        except (KeyError, IndexError, AttributeError, TypeError) as exc:
            raise ValueError("LLM 返回结构异常, 缺少 choices[0].message.content") from exc
        for option in options:
            if content == option:
                return option
        raise ValueError(f"LLM 返回内容不是精确选项文本, 拒绝兜底: {content[:80]!r}")


class StrictDoubaoStrategy(_StrictOptionMixin, _anchor.DoubaoStrategy):
    pass


class StrictDeepSeekStrategy(_StrictOptionMixin, _anchor.DeepSeekStrategy):
    pass


class StrictLLMClient:
    @staticmethod
    def create(strategy: str = "doubao", transport=None):
        if strategy == "doubao":
            return StrictDoubaoStrategy(transport=transport)
        if strategy == "deepseek":
            return StrictDeepSeekStrategy(transport=transport)
        raise ValueError(f"Unknown strategy: {strategy}")
