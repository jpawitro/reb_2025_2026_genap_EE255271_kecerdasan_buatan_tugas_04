"""Model plant sederhana untuk surrogate kendali turbin angin T-S fuzzy."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from numpy.typing import NDArray

Array1D = NDArray[np.float64]
Array2D = NDArray[np.float64]


@dataclass(frozen=True)
class RuleMatrices:
    """Container matriks state-space untuk satu aturan fuzzy."""

    a: Array2D
    b: Array2D
    e: Array2D


def default_rule_matrices() -> tuple[RuleMatrices, RuleMatrices]:
    """Kembalikan matriks default titik operasi low/high plant 2-state.

    Hasil
    -------
    tuple[RuleMatrices, RuleMatrices]
        Matriks `(low_rule, high_rule)` yang dipakai model surrogate.
    """
    low = RuleMatrices(
        a=np.array([[0.965, 0.018], [-0.052, 0.938]], dtype=float),
        b=np.array([[0.045], [0.020]], dtype=float),
        e=np.array([[0.050], [0.030]], dtype=float),
    )
    high = RuleMatrices(
        a=np.array([[0.935, 0.026], [-0.045, 0.908]], dtype=float),
        b=np.array([[0.052], [0.017]], dtype=float),
        e=np.array([[0.060], [0.028]], dtype=float),
    )
    return low, high


def blend_rule_matrices(
    low: RuleMatrices,
    high: RuleMatrices,
    weights: Array1D,
) -> RuleMatrices:
    """Blend dua matriks aturan menggunakan bobot membership fuzzy.

    Parameter
    ----------
    low:
        Paket matriks untuk aturan fuzzy kecepatan rendah.
    high:
        Paket matriks untuk aturan fuzzy kecepatan tinggi.
    weights:
        Vektor membership dua elemen `[w_low, w_high]`.

    Hasil
    -------
    RuleMatrices
        Paket matriks berbobot untuk langkah simulasi saat ini.
    """
    if weights.shape != (2,):
        raise ValueError("weights must be a 2-element vector")

    w_low, w_high = float(weights[0]), float(weights[1])
    return RuleMatrices(
        a=w_low * low.a + w_high * high.a,
        b=w_low * low.b + w_high * high.b,
        e=w_low * low.e + w_high * high.e,
    )


class SimplifiedWindTurbine:
    """Surrogate turbin angin diskrit 2-state untuk pengujian kendali."""

    def __init__(self, x0: Array1D | None = None) -> None:
        """Inisialisasi state plant dan matriks aturan fuzzy.

        Parameter
        ----------
        x0:
            Vektor state awal opsional dengan bentuk `(2,)`.
        """
        self.low_rule, self.high_rule = default_rule_matrices()
        self._x = np.array(
            x0 if x0 is not None else [0.08, -0.04],
            dtype=float,
        )

    @property
    def state(self) -> Array1D:
        """Kembalikan salinan vektor state plant saat ini."""
        return self._x.copy()

    def step(
        self,
        control: float,
        disturbance: float,
        weights: Array1D,
    ) -> Array1D:
        """Majukan plant satu langkah waktu.

        Parameter
        ----------
        control:
            Input kontrol skalar yang diterapkan.
        disturbance:
            Sinyal gangguan eksternal skalar.
        weights:
            Vektor membership fuzzy dua aturan.

        Hasil
        -------
        numpy.ndarray
            Vektor state terbaru setelah satu langkah simulasi.
        """
        blended = blend_rule_matrices(self.low_rule, self.high_rule, weights)
        u_vec = np.array([[control]], dtype=float)
        d_vec = np.array([[disturbance]], dtype=float)
        next_state = (
            blended.a @ self._x.reshape(-1, 1)
            + blended.b @ u_vec
            + blended.e @ d_vec
        )
        self._x = next_state.reshape(-1)
        return self.state
