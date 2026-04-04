"""Unit test untuk fungsi membership fuzzy."""

import unittest

import numpy as np

from ametm_ts.fuzzy import compute_two_rule_weights


class TestFuzzyMembership(unittest.TestCase):
    """Memvalidasi properti membership dua aturan."""

    def test_weights_sum_to_one(self) -> None:
        """Bobot harus selalu berjumlah satu untuk semua kecepatan rotor."""
        speeds = np.linspace(6.0, 18.0, 25)
        for speed in speeds:
            weights = compute_two_rule_weights(float(speed))
            self.assertAlmostEqual(float(np.sum(weights)), 1.0, places=10)

    def test_low_high_limits(self) -> None:
        """Nilai ekstrem harus saturasi ke dominasi rule low atau high."""
        low_case = compute_two_rule_weights(1.0)
        high_case = compute_two_rule_weights(30.0)
        self.assertGreaterEqual(float(low_case[0]), 0.999)
        self.assertGreaterEqual(float(high_case[1]), 0.999)


if __name__ == "__main__":
    unittest.main()
