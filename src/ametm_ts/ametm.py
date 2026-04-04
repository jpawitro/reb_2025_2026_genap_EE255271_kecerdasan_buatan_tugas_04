"""Implementasi Adaptive Memory Event-Triggered Mechanism (AMETM)."""

from __future__ import annotations

from collections import deque

import numpy as np
from numpy.typing import NDArray

Array1D = NDArray[np.float64]


class AdaptiveMemoryEventTrigger:
    """Pemicu berbasis memori dengan threshold adaptif sadar-ACK dan ZOH."""

    def __init__(
        self,
        base_threshold: float = 0.006,
        attack_scale: float = 2.0,
        memory_size: int = 8,
        memory_weight: float = 0.4,
    ) -> None:
        """Inisialisasi state internal AMETM.

        Parameter
        ----------
        base_threshold:
            Ambang dasar pemicu untuk operasi normal.
        attack_scale:
            Pengali ambang saat ACK mengindikasikan risiko serangan.
        memory_size:
            Jumlah hasil release terbaru yang disimpan di memori.
        memory_weight:
            Bobot rata-rata memori pada ambang adaptif.
        """
        if memory_size <= 0:
            raise ValueError("memory_size must be positive")
        if base_threshold <= 0:
            raise ValueError("base_threshold must be positive")

        self.base_threshold = float(base_threshold)
        self.attack_scale = float(attack_scale)
        self.memory_weight = float(memory_weight)
        self._history: deque[int] = deque(
            [1] * memory_size,
            maxlen=memory_size,
        )

    def adaptive_threshold(self, ack_attack_flag: int) -> float:
        """Hitung ambang adaptif dari flag ACK dan statistik memori.

        Parameter
        ----------
        ack_attack_flag:
            Flag biner, `1` berarti kondisi komunikasi berisiko serangan.

        Hasil
        -------
        float
            Nilai ambang adaptif untuk keputusan release.
        """
        history_mean = float(np.mean(self._history))
        attack_term = self.attack_scale if int(ack_attack_flag) == 1 else 0.0
        return self.base_threshold * (
            1.0 + attack_term + self.memory_weight * history_mean
        )

    def should_release(
        self,
        state_error: Array1D,
        ack_attack_flag: int,
    ) -> bool:
        """Tentukan apakah paket perlu di-release pada langkah saat ini.

        Parameter
        ----------
        state_error:
            Vektor error antara state saat ini dan state terakhir release.
        ack_attack_flag:
            Indikator biner risiko serangan dari kanal ACK.

        Hasil
        -------
        bool
            `True` jika kondisi event melebihi ambang adaptif.
        """
        threshold = self.adaptive_threshold(ack_attack_flag)
        error_energy = float(state_error.T @ state_error)
        return error_energy > threshold

    def update_memory(self, release_success: bool) -> None:
        """Perbarui memori internal dengan status keberhasilan release.

        Parameter
        ----------
        release_success:
            `True` jika release paket berhasil, selain itu `False`.
        """
        self._history.append(1 if release_success else 0)
