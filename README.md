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
