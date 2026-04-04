"""Utilitas metrik untuk evaluasi output simulasi AMETM sederhana."""

from __future__ import annotations

import numpy as np
import pandas as pd


def summarize_metrics(
    results: pd.DataFrame,
    state_bound: float = 1.5,
) -> dict[str, float]:
    """Hitung ringkasan metrik dari output simulasi.

    Parameter
    ----------
    results:
        Dataframe hasil simulasi.
    state_bound:
        Batas absolut untuk evaluasi proxy boundedness.

    Hasil
    -------
    dict[str, float]
        Dictionary berisi release ratio, boundedness ratio, RMS state,
        control effort, dan proxy penghematan komunikasi.
    """
    required_cols = {"x1", "x2", "u_applied", "release_success"}
    missing = required_cols.difference(results.columns)
    if missing:
        raise ValueError(f"results missing columns: {sorted(missing)}")

    state_norm = np.sqrt(results["x1"] ** 2 + results["x2"] ** 2)
    release_ratio = float(results["release_success"].mean())
    bounded_ratio = float((state_norm <= state_bound).mean())

    return {
        "release_ratio": release_ratio,
        "communication_saving": 1.0 - release_ratio,
        "bounded_ratio": bounded_ratio,
        "rms_state": float(np.sqrt(np.mean(state_norm**2))),
        "control_effort_l1": float(np.mean(np.abs(results["u_applied"]))),
    }
