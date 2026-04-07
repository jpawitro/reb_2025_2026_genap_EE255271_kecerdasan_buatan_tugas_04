# Tugas 4 ANFIS

Repository ini berisi dua deliverable:
- Review jurnal berbasis LaTeX (IEEE style).
- Prototype Python AMETM T-S fuzzy untuk simulasi sederhana.

## Quick Start (Python)

Prasyarat:
- Python 3.8+

### Opsi A (Direkomendasikan): `uv`

Setup environment dan sinkronisasi dependency:

```bash
uv sync
```

Jalankan simulasi dari root repository:

```bash
uv run python run.py \
  --data-path data/synthetic_wind_turbine_case.csv \
  --result-path data/simulation_results.csv \
  --plot-path plots/simulation_overview.png
```

Jalankan unit test:

```bash
uv run python -m unittest discover -s tests -t . -p "test_*.py"
```

### Opsi B: `venv` + `pip` langsung

Buat virtual environment, aktifkan, lalu install editable package:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -U pip
python -m pip install -e .
```

Jalankan simulasi dari root repository:

```bash
python run.py \
  --data-path data/synthetic_wind_turbine_case.csv \
  --result-path data/simulation_results.csv \
  --plot-path plots/simulation_overview.png
```

Alternatif setara:

```bash
run-ametm-prototype --help
python -m ametm_ts.cli --help
```

Jalankan unit test:

```bash
python -m unittest discover -s tests -t . -p "test_*.py"
```

Output utama:
- `data/synthetic_wind_turbine_case.csv`
- `data/simulation_results.csv`
- `plots/simulation_overview.png`

## Build Laporan LaTeX

Dari folder `reports`:

```bash
pdflatex jurnal_review_fuzzy_joko_pawitro_6022251005.tex
bibtex jurnal_review_fuzzy_joko_pawitro_6022251005
pdflatex jurnal_review_fuzzy_joko_pawitro_6022251005.tex
pdflatex jurnal_review_fuzzy_joko_pawitro_6022251005.tex
```

Jika tersedia, bisa diringkas dengan:

```bash
latexmk -pdf jurnal_review_fuzzy_joko_pawitro_6022251005.tex
```

## Struktur Folder Singkat

- `src/ametm_ts`: implementasi prototype.
- `tests`: unit test.
- `data`: data sintetik dan hasil simulasi.
- `plots`: keluaran visualisasi.
- `reports`: laporan `.tex`, `.bib`, dan PDF.
- `references`: paper acuan dan dokumen pendukung.
