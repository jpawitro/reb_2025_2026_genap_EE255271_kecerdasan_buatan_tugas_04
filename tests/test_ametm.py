"""Unit test untuk perilaku pemicu AMETM."""

import unittest

import numpy as np

from ametm_ts.ametm import AdaptiveMemoryEventTrigger


class TestAMETM(unittest.TestCase):
    """Memvalidasi adaptasi threshold dan keputusan release."""

    def test_threshold_increases_in_attack_state(self) -> None:
        """Threshold adaptif harus meningkat pada kondisi ACK berisiko."""
        trigger = AdaptiveMemoryEventTrigger(
            base_threshold=0.01,
            attack_scale=2.5,
        )
        normal = trigger.adaptive_threshold(ack_attack_flag=0)
        attack = trigger.adaptive_threshold(ack_attack_flag=1)
        self.assertGreater(attack, normal)

    def test_release_decision_with_large_error(self) -> None:
        """Error state besar harus memicu percobaan release."""
        trigger = AdaptiveMemoryEventTrigger(
            base_threshold=0.001,
            attack_scale=0.0,
        )
        large_error = np.array([0.2, -0.2], dtype=float)
        self.assertTrue(trigger.should_release(large_error, ack_attack_flag=0))


if __name__ == "__main__":
    unittest.main()
