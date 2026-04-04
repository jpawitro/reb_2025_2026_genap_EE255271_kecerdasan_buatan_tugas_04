"""Unit test bergaya integrasi untuk data dan simulasi."""

import unittest

from ametm_ts.ametm import AdaptiveMemoryEventTrigger
from ametm_ts.controller import default_controller_gains
from ametm_ts.data_utils import generate_synthetic_case
from ametm_ts.simulation import run_simulation
from ametm_ts.wind_turbine import SimplifiedWindTurbine


class TestDataAndSimulation(unittest.TestCase):
    """Memvalidasi skema data dan konsistensi output simulasi."""

    def test_synthetic_schema(self) -> None:
        """Dataset sintetik harus menyediakan kolom wajib."""
        case = generate_synthetic_case(num_steps=64, dt=0.1, seed=7)
        required = {
            "time_s",
            "wind_speed_mps",
            "disturbance",
            "dos_flag",
            "ack_flag",
        }
        self.assertTrue(required.issubset(case.columns))

    def test_simulation_runs(self) -> None:
        """Simulasi harus menghasilkan output dengan kolom kontrol."""
        case = generate_synthetic_case(num_steps=80, dt=0.1, seed=10)
        plant = SimplifiedWindTurbine()
        trigger = AdaptiveMemoryEventTrigger()
        gains = default_controller_gains()

        results = run_simulation(
            case,
            plant=plant,
            trigger=trigger,
            gains=gains,
        )

        self.assertEqual(len(results), len(case))
        self.assertIn("u_applied", results.columns)
        self.assertIn("release_success", results.columns)
        self.assertFalse(results.isna().any().any())


if __name__ == "__main__":
    unittest.main()
