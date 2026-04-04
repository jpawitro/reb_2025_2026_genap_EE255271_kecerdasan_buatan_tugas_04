Tugas 4 - ANFIS

Repo ini berisi review jurnal dalam format LaTeX dan pengaturan proyek minimal.

Struktur penting:
- reports/
  - jurnal_review_fuzzy_joko_pawitro_6022251005.tex (laporan utama)
  - references.bib (bibliografi IEEE)
  - ITS_pojok.pdf, kurikulum_ai.pdf, Secure_Control_....pdf (dependensi lokal)
- plots/ (kosong)
- src/ (kosong)
- tests/ (kosong)

Cara kompilasi (dari folder `reports`):

pdflatex jurnal_review_fuzzy_joko_pawitro_6022251005.tex
bibtex jurnal_review_fuzzy_joko_pawitro_6022251005
pdflatex jurnal_review_fuzzy_joko_pawitro_6022251005.tex
pdflatex jurnal_review_fuzzy_joko_pawitro_6022251005.tex

Atau pakai `latexmk -pdf jurnal_review_fuzzy_joko_pawitro_6022251005.tex` jika tersedia.

## Python Prototype (Phase 1)

Implementasi awal AMETM T-S fuzzy tersedia di `src/ametm_ts`.

Dependensi utama:
- numpy
- pandas
- matplotlib
- seaborn

Contoh menjalankan unittest:

```bash
PYTHONPATH=src .venv/bin/python -m unittest discover -s tests -p "test_*.py"
```

Contoh menjalankan pipeline simulasi (buat data sintetik + hasil CSV + plot):

```bash
PYTHONPATH=src .venv/bin/python -m ametm_ts.cli \
  --data-path data/synthetic_wind_turbine_case.csv \
  --result-path data/simulation_results.csv \
  --plot-path plots/simulation_overview.png
```

Output utama:
- `data/synthetic_wind_turbine_case.csv`
- `data/simulation_results.csv`
- `plots/simulation_overview.png`
