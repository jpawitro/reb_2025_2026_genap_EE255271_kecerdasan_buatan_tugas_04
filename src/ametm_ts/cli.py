"""Titik masuk command-line untuk simulasi AMETM T-S fuzzy sederhana."""

from __future__ import annotations

import argparse
from pathlib import Path

from .ametm import AdaptiveMemoryEventTrigger
from .controller import default_controller_gains
from .data_utils import generate_synthetic_case, load_case_csv, save_case_csv
from .metrics import summarize_metrics
from .plotting import plot_simulation_results
from .simulation import run_simulation
from .wind_turbine import SimplifiedWindTurbine


DEFAULT_DATA_PATH = Path("data/synthetic_wind_turbine_case.csv")
DEFAULT_RESULT_PATH = Path("data/simulation_results.csv")
DEFAULT_PLOT_PATH = Path("plots/simulation_overview.png")


def run_pipeline(
    data_path: str | Path = DEFAULT_DATA_PATH,
    result_path: str | Path = DEFAULT_RESULT_PATH,
    plot_path: str | Path = DEFAULT_PLOT_PATH,
    num_steps: int = 600,
    dt: float = 0.1,
    seed: int = 42,
) -> dict[str, float]:
    """Jalankan generasi data, simulasi, metrik, dan plotting satu pipeline.

    Parameter
    ----------
    data_path:
        Path CSV untuk data input sintetik.
    result_path:
        Path CSV untuk output hasil simulasi.
    plot_path:
        Path gambar untuk diagnostik ringkasan.
    num_steps:
        Jumlah sampel sintetik jika data dibuat.
    dt:
        Interval sampling yang dipakai generator data sintetik.
    seed:
        Seed acak untuk reproduksibilitas.

    Hasil
    -------
    dict[str, float]
        Dictionary ringkasan metrik.
    """
    data_path = Path(data_path)
    result_path = Path(result_path)
    plot_path = Path(plot_path)

    if not data_path.exists():
        synthetic = generate_synthetic_case(
            num_steps=num_steps,
            dt=dt,
            seed=seed,
        )
        save_case_csv(synthetic, data_path)

    case_data = load_case_csv(data_path)
    plant = SimplifiedWindTurbine()
    trigger = AdaptiveMemoryEventTrigger()
    gains = default_controller_gains()

    results = run_simulation(
        case_data,
        plant=plant,
        trigger=trigger,
        gains=gains,
    )
    save_case_csv(results, result_path)
    plot_simulation_results(results, plot_path)

    return summarize_metrics(results)


def build_parser() -> argparse.ArgumentParser:
    """Bangun parser CLI untuk eksekusi pipeline simulasi.

    Hasil
    -------
    argparse.ArgumentParser
        Instance parser yang sudah dikonfigurasi.
    """
    parser = argparse.ArgumentParser(
        description="Jalankan simulasi AMETM T-S fuzzy sederhana"
    )
    parser.add_argument("--data-path", default=str(DEFAULT_DATA_PATH))
    parser.add_argument("--result-path", default=str(DEFAULT_RESULT_PATH))
    parser.add_argument("--plot-path", default=str(DEFAULT_PLOT_PATH))
    parser.add_argument("--num-steps", type=int, default=600)
    parser.add_argument("--dt", type=float, default=0.1)
    parser.add_argument("--seed", type=int, default=42)
    return parser


def main() -> None:
    """Eksekusi alur kerja CLI dan cetak ringkasan metrik."""
    args = build_parser().parse_args()
    summary = run_pipeline(
        data_path=args.data_path,
        result_path=args.result_path,
        plot_path=args.plot_path,
        num_steps=args.num_steps,
        dt=args.dt,
        seed=args.seed,
    )
    for key, value in summary.items():
        print(f"{key}: {value:.6f}")


if __name__ == "__main__":
    main()
