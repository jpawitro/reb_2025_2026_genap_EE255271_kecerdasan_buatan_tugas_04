"""Utilitas membership fuzzy untuk pendekatan Takagi-Sugeno dua aturan."""

from __future__ import annotations

import numpy as np
from numpy.typing import NDArray

Array1D = NDArray[np.float64]


def compute_two_rule_weights(
    rotor_speed: float,
    nominal_speed: float = 12.0,
    spread: float = 4.0,
) -> Array1D:
    """Hitung bobot membership dua aturan yang ternormalisasi.

    Parameter
    ----------
    rotor_speed:
        Nilai surrogate kecepatan rotor saat ini dalam m/s.
    nominal_speed:
        Kecepatan rotor nominal sebagai pusat partisi fuzzy.
    spread:
        Rentang kecepatan simetris di sekitar nominal untuk blending.

    Hasil
    -------
    numpy.ndarray
        Array dua elemen `[w_low, w_high]` dengan jumlah 1.0.
    """
    if spread <= 0:
        raise ValueError("spread must be positive")

    left = nominal_speed - spread / 2.0
    right = nominal_speed + spread / 2.0

    if rotor_speed <= left:
        low = 1.0
    elif rotor_speed >= right:
        low = 0.0
    else:
        low = (right - rotor_speed) / (right - left)

    high = 1.0 - low
    weights = np.array([low, high], dtype=float)
    weights /= np.sum(weights)
    return weights
