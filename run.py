"""Entry point dari root repository untuk menjalankan pipeline AMETM."""

from __future__ import annotations

from ametm_ts.cli import main as cli_main


def main() -> None:
    """Delegasikan eksekusi ke CLI utama paket ametm_ts."""
    cli_main()


if __name__ == "__main__":
    main()
