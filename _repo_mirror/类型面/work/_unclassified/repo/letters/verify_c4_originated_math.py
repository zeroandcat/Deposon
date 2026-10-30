"""Finite exact-arithmetic checks of the originated reply's mathematics.

All inputs here are synthetic mathematical examples, not deposon measurements.
This script reads no project artifacts and invokes no network or model API.
"""

from fractions import Fraction
from itertools import product
import unittest


ACTIONS = range(4)


def payoff(action, mask):
    return int(bool(mask & (1 << action)))


def conditional_minimum(keys, observations, probabilities):
    labels = sorted(set(observations))
    best_correct = sum(
        max(
            sum(
                (p * payoff(a, key) for key, z, p in
                 zip(keys, observations, probabilities) if z == label),
                Fraction(0),
            )
            for a in ACTIONS
        )
        for label in labels
    )
    return 1 - best_correct


def enumerated_minimum(keys, observations, probabilities):
    labels = sorted(set(observations))
    risks = []
    for choices in product(ACTIONS, repeat=len(labels)):
        policy = dict(zip(labels, choices))
        risk = sum(
            (p * (1 - payoff(policy[z], key)) for key, z, p in
             zip(keys, observations, probabilities)),
            Fraction(0),
        )
        risks.append(risk)
    return min(risks)


class OriginatedMathChecks(unittest.TestCase):
    def test_every_nonempty_key_has_exact_optimum_and_bound_one(self):
        for mask in range(1, 16):
            rewards = [payoff(a, mask) for a in ACTIONS]
            self.assertEqual(max(rewards), 1)
            self.assertTrue(all(r in (0, 1) for r in rewards))

    def test_conditional_formula_matches_all_deterministic_policies(self):
        count = 0
        probabilities = [Fraction(i, 10) for i in (1, 2, 3, 4)]
        for optimal_labels in product(ACTIONS, repeat=4):
            keys = [1 << a for a in optimal_labels]
            for observations in product(range(2), repeat=4):
                self.assertEqual(
                    conditional_minimum(keys, observations, probabilities),
                    enumerated_minimum(keys, observations, probabilities),
                )
                count += 1
        probabilities = [Fraction(1, 3), Fraction(2, 3)]
        for keys in product(range(1, 16), repeat=2):
            for observations in product(range(2), repeat=2):
                self.assertEqual(
                    conditional_minimum(keys, observations, probabilities),
                    enumerated_minimum(keys, observations, probabilities),
                )
                count += 1
        self.assertEqual(count, 4996)

    def test_no_information_can_still_allow_zero_regret(self):
        self.assertEqual(
            conditional_minimum([1, 1], [0, 0], [Fraction(1, 2)] * 2),
            0,
        )
        self.assertEqual(
            conditional_minimum([1, 2], [0, 0], [Fraction(1, 2)] * 2),
            Fraction(1, 2),
        )

    def test_uniform_action_identity_for_every_key(self):
        for mask in range(1, 16):
            actual = sum(
                (Fraction(1 - payoff(a, mask), 4) for a in ACTIONS),
                Fraction(0),
            )
            expected = 1 - Fraction(bin(mask).count("1"), 4)
            self.assertEqual(actual, expected)
        self.assertEqual(expected, 0)  # All four actions accepted.
        self.assertEqual(1 - Fraction(1, 4), Fraction(3, 4))

    def test_two_normalized_errors_are_not_bounded_by_one(self):
        self.assertEqual(sum(1 - payoff(a, 1) for a in (1, 2)), 2)

    def test_guarded_ratio_algebra_and_noncancellation(self):
        for gl, gb, c, eps in product(
            range(5), range(4),
            (Fraction(1, 2), Fraction(1), Fraction(2)),
            (Fraction(1, 10), Fraction(1), Fraction(2)),
        ):
            normalized = (gl / c) / max(gb / c, eps)
            rearranged = Fraction(gl) / max(Fraction(gb), c * eps)
            self.assertEqual(normalized, rearranged)
        self.assertEqual(Fraction(2) / Fraction(1, 10), 20)
        self.assertEqual(Fraction(2) / Fraction(2, 10), 10)


if __name__ == "__main__":
    unittest.main(verbosity=2)
