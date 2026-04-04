"""Penggerak simulasi untuk eksperimen AMETM T-S fuzzy sederhana."""

from __future__ import annotations

from dataclasses import dataclass

import pandas as pd

from .ametm import AdaptiveMemoryEventTrigger
from .controller import ControllerGains, compute_control
from .fuzzy import compute_two_rule_weights
from .wind_turbine import SimplifiedWindTurbine


@dataclass(frozen=True)
class SimulationConfig:
    """Nilai konfigurasi untuk simulasi domain waktu."""

    nominal_speed: float = 12.0
    fuzzy_spread: float = 4.0


def run_simulation(
    case_data: pd.DataFrame,
    plant: SimplifiedWindTurbine,
    trigger: AdaptiveMemoryEventTrigger,
    gains: ControllerGains,
    config: SimulationConfig | None = None,
) -> pd.DataFrame:
    """Jalankan simulasi end-to-end untuk kendali event-triggered sadar DoS.

    Parameter
    ----------
    case_data:
        Dataframe input dengan kolom `time_s`, `wind_speed_mps`,
        `disturbance`, `dos_flag`, dan `ack_flag`.
    plant:
        Instance model plant.
    trigger:
        Instance pemicu AMETM.
    gains:
        Gain controller untuk aturan fuzzy low/high.
    config:
        Konfigurasi simulasi opsional.

    Hasil
    -------
    pandas.DataFrame
        Hasil deret waktu berisi state, sinyal kontrol, event trigger,
        dan outcome komunikasi.
    """
    required_cols = {
        "time_s",
        "wind_speed_mps",
        "disturbance",
        "dos_flag",
        "ack_flag",
    }
    missing = required_cols.difference(case_data.columns)
    if missing:
        raise ValueError(f"case_data missing columns: {sorted(missing)}")

    sim_cfg = config or SimulationConfig()
    last_released_state = plant.state
    held_control = 0.0

    records: list[dict[str, float | int]] = []
    for row in case_data.to_dict(orient="records"):
        time_s = float(row["time_s"])
        wind_speed = float(row["wind_speed_mps"])
        disturbance = float(row["disturbance"])
        dos_flag = int(row["dos_flag"])
        ack_flag = int(row["ack_flag"])

        weights = compute_two_rule_weights(
            rotor_speed=wind_speed,
            nominal_speed=sim_cfg.nominal_speed,
            spread=sim_cfg.fuzzy_spread,
        )

        state_before = plant.state
        control_candidate = compute_control(state_before, weights, gains)

        release_attempt = trigger.should_release(
            state_error=(state_before - last_released_state),
            ack_attack_flag=ack_flag,
        )

        dos_active = dos_flag == 1
        release_success = bool(release_attempt and not dos_active)

        if release_success:
            held_control = control_candidate
            last_released_state = state_before.copy()

        trigger.update_memory(release_success)
        state_after = plant.step(
            float(held_control),
            disturbance,
            weights,
        )

        records.append(
            {
                "time_s": time_s,
                "wind_speed_mps": wind_speed,
                "disturbance": disturbance,
                "dos_flag": dos_flag,
                "ack_flag": ack_flag,
                "membership_low": float(weights[0]),
                "membership_high": float(weights[1]),
                "x1": float(state_after[0]),
                "x2": float(state_after[1]),
                "u_candidate": float(control_candidate),
                "u_applied": float(held_control),
                "release_attempt": int(release_attempt),
                "release_success": int(release_success),
            }
        )

    return pd.DataFrame.from_records(records)
