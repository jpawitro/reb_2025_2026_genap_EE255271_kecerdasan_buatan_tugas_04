"""Utilitas controller untuk hukum kendali fuzzy mirip PDC sederhana."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from numpy.typing import NDArray

Array1D = NDArray[np.float64]
Array2D = NDArray[np.float64]


@dataclass(frozen=True)
class ControllerGains:
    """Gain fuzzy-rule untuk titik operasi rendah dan tinggi."""

    low: Array2D
    high: Array2D


def default_controller_gains() -> ControllerGains:
    """Kembalikan gain heuristik untuk controller PDC sederhana.

    Hasil
    -------
    ControllerGains
        Matriks gain low/high dengan bentuk `(1, 2)`.
    """
    return ControllerGains(
        low=np.array([[1.25, 0.55]], dtype=float),
        high=np.array([[1.45, 0.70]], dtype=float),
    )


def blend_gain(weights: Array1D, gains: ControllerGains) -> Array2D:
    """Blend gain low/high menggunakan bobot membership fuzzy saat ini.

    Parameter
    ----------
    weights:
        Vektor membership dua aturan `[w_low, w_high]`.
    gains:
        Container gain untuk aturan low/high.

    Hasil
    -------
    numpy.ndarray
        Matriks gain hasil blending dengan bentuk `(1, 2)`.
    """
    if weights.shape != (2,):
        raise ValueError("weights must be a 2-element vector")

    return float(weights[0]) * gains.low + float(weights[1]) * gains.high


def compute_control(
    state: Array1D,
    weights: Array1D,
    gains: ControllerGains,
) -> float:
    """Hitung input kontrol skalar dengan feedback berbobot mirip PDC.

    Parameter
    ----------
    state:
        Vektor state plant saat ini.
    weights:
        Bobot membership fuzzy.
    gains:
        Gain controller low/high.

    Hasil
    -------
    float
        Aksi kontrol skalar `u = -(K_blended * x)`.
    """
    k_blended = blend_gain(weights, gains)
    return float(-(k_blended @ state.reshape(-1, 1)).item())
