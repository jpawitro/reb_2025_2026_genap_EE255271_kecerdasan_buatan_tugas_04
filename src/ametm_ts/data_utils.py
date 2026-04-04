"""Utilitas data sintetik untuk eksperimen simulasi AMETM T-S fuzzy."""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd


def generate_synthetic_case(
    num_steps: int = 600,
    dt: float = 0.1,
    seed: int = 42,
) -> pd.DataFrame:
    """Bangkitkan data sintetik operasi turbin dengan profil DoS/ACK.

    Parameter
    ----------
    num_steps:
        Jumlah sampel simulasi.
    dt:
        Interval sampling dalam detik.
    seed:
        Seed acak untuk reproduksibilitas.

    Hasil
    -------
    pandas.DataFrame
        Dataset dengan kolom `time_s`, `wind_speed_mps`, `disturbance`,
        `dos_flag`, `ack_flag`, dan `deception_noise`.
    """
    if num_steps <= 0:
        raise ValueError("num_steps must be positive")
    if dt <= 0:
        raise ValueError("dt must be positive")

    rng = np.random.default_rng(seed)
    time_s = np.arange(num_steps, dtype=float) * dt

    wind_speed = (
        12.0
        + 1.3 * np.sin(2 * np.pi * time_s / 55.0)
        + 0.25 * rng.normal(size=num_steps)
    )
    disturbance = (
        0.08 * np.sin(2 * np.pi * time_s / 18.0)
        + 0.03 * rng.normal(size=num_steps)
    )

    periodic_dos = ((time_s % 30.0) >= 12.0) & ((time_s % 30.0) < 16.0)
    random_burst = rng.random(num_steps) < 0.025
    dos_flag = (periodic_dos | random_burst).astype(int)

    ack_flag = dos_flag.copy()
    deception_noise = 0.015 * rng.normal(size=num_steps)

    return pd.DataFrame(
        {
            "time_s": time_s,
            "wind_speed_mps": wind_speed,
            "disturbance": disturbance,
            "dos_flag": dos_flag,
            "ack_flag": ack_flag,
            "deception_noise": deception_noise,
        }
    )


def save_case_csv(dataframe: pd.DataFrame, output_path: str | Path) -> Path:
    """Simpan dataframe sintetik atau hasil simulasi ke CSV.

    Parameter
    ----------
    dataframe:
        DataFrame yang akan ditulis.
    output_path:
        Path file CSV tujuan.

    Hasil
    -------
    pathlib.Path
        Path output ter-resolve setelah proses tulis.
    """
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    dataframe.to_csv(path, index=False)
    return path


def load_case_csv(input_path: str | Path) -> pd.DataFrame:
    """Muat dataset CSV untuk simulasi.

    Parameter
    ----------
    input_path:
        Path file CSV.

    Hasil
    -------
    pandas.DataFrame
        Dataset hasil pemuatan.
    """
    return pd.read_csv(input_path)
