"""Helper plotting untuk diagnostik simulasi AMETM T-S fuzzy."""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


sns.set_theme(style="whitegrid")


def plot_simulation_results(
    results: pd.DataFrame,
    output_path: str | Path,
) -> Path:
    """Buat dan simpan plot diagnostik dari hasil simulasi.

    Parameter
    ----------
    results:
        DataFrame keluaran runner simulasi.
    output_path:
        Path tujuan untuk gambar plot.

    Hasil
    -------
    pathlib.Path
        Path gambar ter-resolve tempat figur disimpan.
    """
    required_cols = {
        "time_s",
        "x1",
        "x2",
        "u_applied",
        "release_success",
        "dos_flag",
        "membership_low",
    }
    missing = required_cols.difference(results.columns)
    if missing:
        raise ValueError(f"results missing columns: {sorted(missing)}")

    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)

    fig, axes = plt.subplots(4, 1, figsize=(11, 12), sharex=True)

    sns.lineplot(data=results, x="time_s", y="x1", ax=axes[0], label="x1")
    sns.lineplot(data=results, x="time_s", y="x2", ax=axes[0], label="x2")
    axes[0].set_title("State Trajectory")

    sns.lineplot(
        data=results,
        x="time_s",
        y="u_applied",
        ax=axes[1],
        color="tab:green",
    )
    axes[1].set_title("Applied Control (ZOH-aware)")

    sns.lineplot(
        data=results,
        x="time_s",
        y="release_success",
        ax=axes[2],
        color="tab:blue",
    )
    sns.lineplot(
        data=results,
        x="time_s",
        y="dos_flag",
        ax=axes[2],
        color="tab:red",
        alpha=0.6,
    )
    axes[2].set_title("Release Success vs DoS")

    sns.lineplot(
        data=results,
        x="time_s",
        y="membership_low",
        ax=axes[3],
        color="tab:orange",
    )
    axes[3].set_title("Low-Rule Membership")
    axes[3].set_xlabel("Time (s)")

    fig.tight_layout()
    fig.savefig(output, dpi=160)
    plt.close(fig)
    return output
