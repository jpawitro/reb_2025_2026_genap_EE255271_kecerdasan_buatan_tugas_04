"""Unit test untuk metrik simulasi."""

import unittest

import pandas as pd

from ametm_ts.metrics import summarize_metrics


class TestMetrics(unittest.TestCase):
    """Memvalidasi rentang metrik dan ketersediaan kunci output."""

    def test_summary_metric_ranges(self) -> None:
        """Nilai metrik harus berada pada rentang numerik yang valid."""
        results = pd.DataFrame(
            {
                "x1": [0.1, 0.2, 0.1, 0.05],
                "x2": [-0.1, -0.05, 0.0, 0.02],
                "u_applied": [0.1, 0.12, 0.08, 0.05],
                "release_success": [1, 0, 1, 1],
            }
        )
        summary = summarize_metrics(results, state_bound=1.0)

        self.assertIn("release_ratio", summary)
        self.assertIn("communication_saving", summary)
        self.assertGreaterEqual(summary["release_ratio"], 0.0)
        self.assertLessEqual(summary["release_ratio"], 1.0)


if __name__ == "__main__":
    unittest.main()
