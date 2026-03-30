Laporan Review Akademik: Secure Control for T–S Fuzzy Wind Turbine Systems

1. Identitas Jurnal dan Informasi Umum

Dalam lanskap evolusi menuju smart grid, integrasi energi terbarukan—khususnya turbin angin—menghadapi tantangan fundamental yang bersifat multidimensi: kompleksitas intrinsik dari non-linearitas sistem fisik serta kerentanan sistemik terhadap gangguan siber pada saluran komunikasi. Review ini menyajikan dekonstruksi analitis terhadap literatur yang mengusulkan kerangka kerja kendali aman berbasis kecerdasan buatan untuk menjamin reliabilitas operasional. Penggunaan pemodelan Takagi-Sugeno (T-S) Fuzzy di sini diposisikan sebagai jembatan matematis yang krusial untuk mentransformasikan dinamika non-linear sistem ke dalam domain kendali linear yang robust, selaras dengan visi rekayasa elektrik berkelanjutan.

Komponen Identitas	Detail Informasi
Judul Artikel	Secure Control for T–S Fuzzy Wind Turbine Systems Under Hybrid Cyberattacks via an Adaptive Memory Event-Triggered Mechanism
Penulis	Dong Xu, Yajuan Liu, Sangmoon Lee
Nama Jurnal	IEEE Transactions on Fuzzy Systems
Volume / Issue / Tahun	Vol. 33, Issue 5, 2025
DOI	10.1109/TFUZZ.2025.3525778
Afiliasi Penulis	North China Electric Power University (Tiongkok) & Kyungpook National University (Korea Selatan)

Analisis Identitas: IEEE Transactions on Fuzzy Systems merupakan jurnal kuartil teratas (Q1) dengan faktor dampak yang signifikan, memvalidasi orisinalitas dan rigiditas matematis dari setiap publikasinya. Artikel ini merepresentasikan standar tertinggi dalam penerapan logika fuzzy tingkat lanjut untuk menyelesaikan problematik keamanan pada Networked Control Systems (NCS).


--------------------------------------------------------------------------------


2. Abstrak Review

Review ini mengevaluasi secara kritis metodologi kendali aman yang diusulkan oleh Xu dkk. untuk sistem turbin angin berbasis Permanent Magnet Synchronous Generator (PMSG) yang terpapar serangan siber hibrida. Fokus utama analisis terletak pada kebaruan Adaptive Memory Event-Triggered Mechanism (AMETM) yang mengintegrasikan sinyal Acknowledgement (ACK) untuk mendeteksi kehadiran serangan Denial-of-Service (DoS). Melalui pendekatan stabilitas Lyapunov dan optimasi berbasis Linear Matrix Inequalities (LMI), ulasan ini membedah bagaimana mekanisme pemicu adaptif mampu menjamin mean-square H∞ asymptotic stability pada kondisi normal, serta uniformly ultimate boundedness saat terjadi intrusi DoS. Analisis ini menegaskan bahwa penggunaan memori data historis merupakan diferensiator teknis utama yang mempercepat konvergensi sistem dibandingkan mekanisme pemicu statis konvensional.


--------------------------------------------------------------------------------


3. Pendahuluan: Signifikansi AI dalam Energi Terbarukan

Pergeseran paradigma energi global menuju dekarbonisasi menempatkan turbin angin PMSG sebagai elemen vital karena efisiensi dan biaya pemeliharaannya yang rendah. Namun, ketergantungan PMSG pada parameter kecepatan angin yang stokastik menciptakan non-linearitas ekstrem yang sulit dikelola oleh kendali PID klasik. Di sinilah logika fuzzy memberikan nilai transformatif dengan menyediakan skema decision-making yang cerdas di bawah ketidakpastian.

Problem Statement: Integrasi jaringan komunikasi nirkabel pada NCS turbin angin membuka celah bagi serangan siber hibrida. Serangan DoS melumpuhkan ketersediaan data (availability), sementara deception attacks merusak integritas data (integrity). Tanpa mekanisme proteksi yang adaptif, serangan ini dapat memicu osilasi mekanis yang destruktif pada komponen turbin, mengancam keberlanjutan pasokan energi pada grid.

Tujuan Review: Review ini bertujuan mengevaluasi efektivitas metodologi AMETM dan T-S Fuzzy dalam mempertahankan performa sistem di bawah tekanan serangan hibrida, sekaligus memetakan relevansinya terhadap kurikulum magister rekayasa elektrik.


--------------------------------------------------------------------------------


4. Ringkasan Artikel: Dekonstruksi Metodologi

Penulis jurnal memperkenalkan kerangka kerja kendali yang menyatukan pemodelan fuzzy dengan mekanisme pemicu yang peka terhadap serangan. Berikut adalah dekonstruksi teknisnya:

* Pemodelan T-S Fuzzy & Variabel Premis: Sistem PMSG ditransformasikan menjadi sekumpulan subsistem linear melalui membership functions. Variabel premis utama adalah kecepatan sudut rotor (\omega_g), yang dipetakan untuk menghasilkan plant rules yang presisi. Pendekatan ini memungkinkan penggunaan teknik parallel distributed compensation (PDC) untuk desain kontroler.
* Arsitektur AMETM (Adaptive Memory Event-Triggered Mechanism): Kebaruan utama terletak pada penggunaan buffer memori yang menyimpan set sinyal rilis terbaru (m). Hukum adaptif menyesuaikan ambang batas (\varsigma) secara dinamis. Poin krusial yang diangkat adalah integrasi sinyal ACK (Acknowledgement); jika ACK=1 (terdeteksi DoS), mekanisme secara otomatis memperketat kondisi pemicu untuk menahan transmisi sia-sia, sehingga menghemat energi baterai node sensor.
* Logika Algorithm 1 & ZOH: Sistem menggunakan Zero-Order Hold (ZOH) untuk mempertahankan sinyal kontrol terakhir yang berhasil ditransmisikan selama jendela serangan DoS berlangsung. Hal ini krusial untuk menjaga kontinuitas kendali saat jalur komunikasi terputus.
* Stabilitas Sistem: Penulis membuktikan bahwa sistem mencapai stabilitas asimptotik mean-square H_\infty saat tidak ada serangan. Namun, karena DoS bersifat energy-constrained yang memutus feedback loop, sistem hanya dapat dijamin mencapai uniformly ultimate boundedness (tetap berada dalam batas yang ditentukan) selama durasi serangan.


--------------------------------------------------------------------------------


5. Analisis Kritis: Evaluasi dan Dampak (The "So What?" Layer)

Sebagai pakar sistem kendali, kami memandang bahwa validasi algoritma AI harus melampaui hasil simulasi ideal dan menyentuh aspek ketahanan sistemik.

Evaluasi Diferensiator Utama: Penggunaan memori dalam AMETM bukan sekadar tren, melainkan solusi teknis untuk masalah peak fluctuations. Dengan mempertimbangkan data historis, probabilitas rilis paket ditingkatkan pada titik-titik transien ekstrem, yang secara empiris mempercepat konvergensi sistem. Hal ini sangat kontras dengan ETM statis yang sering kali "terlambat" merespons perubahan beban yang cepat.

Analisis Hasil Simulasi & SRP: Interpretasi data pada Scenario 1 dan 2 menunjukkan penurunan persentase Successfully Released Packets (SRP) saat DoS aktif. Dalam perspektif operasional, ini adalah indikator keberhasilan strategi keamanan; algoritma secara cerdas mendeteksi bahwa upaya transmisi saat saluran dikuasai penyerang hanya akan menghabiskan sumber daya baterai tanpa memberikan dampak kendali.

Kelebihan & Kekurangan (Expert Perspective):

Kelebihan Inovasi Teknis	Kekurangan & Kompleksitas
Integrasi ACK memungkinkan deteksi DoS secara real-time tanpa perangkat keras deteksi intrusi tambahan.	Desain gain kontroler (K_{rj}) memerlukan penyelesaian LMI yang sangat kompleks, memberikan beban komputasi tinggi pada fase perancangan.
Penggunaan Slack Matrices pada Theorem 2 berhasil mengatasi masalah Mismatched Membership Functions, memberikan fleksibilitas desain yang lebih tinggi.	Model mengasumsikan bounded uncertainty (E) untuk dampak serangan. Pada skenario serangan "Zero-day" yang tidak terprediksi, batas ini mungkin terlalu konservatif.
Reduksi transmisi data redundan hingga >50% memperpanjang siklus hidup infrastruktur sensor nirkabel.	Kebutuhan buffer memori pada node sensor meningkatkan biaya per unit perangkat keras di lapangan.


--------------------------------------------------------------------------------


6. Relevansi dengan Kurikulum S2 Rekayasa Elektrik Berkelanjutan ITS

Literatur ini merupakan studi kasus sempurna yang mengintegrasikan beberapa Capaian Pembelajaran Lulusan (CPL) pada mata kuliah Artificial Intelligence (EE235271) di ITS:

* CLO-3 (Mastering Fuzzy Systems): Implementasi model T-S Fuzzy untuk PMSG menunjukkan aplikasi nyata logika fuzzy dalam decision making pada sistem dinamis yang kompleks.
* CPL-04 (Mastering Concepts for Analysis and Design): Jurnal ini mendemonstrasikan penguasaan prinsip rekayasa dalam merancang strategi kendali yang komprehensif menghadapi tantangan teknologi informasi (serangan siber).
* CPL-08 (Decision Making in Technology Development): Kemampuan algoritma untuk beralih mode operasional berdasarkan analisis data siber mencerminkan pengambilan keputusan rekayasa yang etis dan berkelanjutan.

Aplikasi Praktis di Indonesia: Metode ini sangat relevan untuk diaplikasikan pada PLTB Sidrap atau Jeneponto. Karakteristik angin di pesisir Indonesia memiliki profil turbulensi frekuensi tinggi yang sering kali menciptakan asynchronous premise variables antara sensor dan kontroler. Penggunaan AMETM yang robust terhadap ketidaksinkronan ini akan sangat meningkatkan reliabilitas PLTB nasional.


--------------------------------------------------------------------------------


7. Kesimpulan dan Rekomendasi Strategis

Review analitis ini menyimpulkan bahwa integrasi AMETM dan T-S Fuzzy merupakan lompatan signifikan dalam menciptakan infrastruktur energi yang resilient. Metodologi ini berhasil menjawab dilema antara efisiensi komunikasi dan keamanan sistem tenaga listrik.

Rekomendasi Strategis untuk Pengembangan Selanjutnya:

1. Optimasi Meta-Heuristik: Mengingat kompleksitas penentuan fungsi keanggotaan fuzzy, disarankan menggunakan Genetic Algorithm (GA) untuk mengoptimasi lebar fungsi keanggotaan dan bobot matriks (Q, R, P) secara otomatis.
2. Unbounded Attack Scenarios: Penelitian masa depan perlu menguji ketahanan model terhadap unbounded deception attacks untuk memetakan batas kegagalan absolut sistem.
3. Hardware-in-the-Loop (HIL): Bagi mahasiswa magister ITS, disarankan melakukan validasi menggunakan HIL untuk mengukur latensi nyata dari pemrosesan LMI pada embedded controller.


--------------------------------------------------------------------------------


8. Daftar Pustaka

[1] D. Xu, Y. Liu, and S. Lee, "Secure Control for T–S Fuzzy Wind Turbine Systems Under Hybrid Cyberattacks via an Adaptive Memory Event-Triggered Mechanism," IEEE Transactions on Fuzzy Systems, vol. 33, no. 5, pp. 1-13, 2025.

[2] T. J. Ross, Fuzzy Logic with Engineering Applications, 3rd ed. Chichester, U.K.: John Wiley & Sons Ltd, 2010.

[3] Departemen Teknik Elektro ITS, Silabus Mata Kuliah S2 Rekayasa Elektrik Berkelanjutan: EE235271 Artificial Intelligence, Surabaya: ITS, 2023.

[4] E. Tian and C. Peng, "Memory-based event-triggering H_\infty load frequency control for power systems under deception attacks," IEEE Trans. Cybern., vol. 50, no. 11, pp. 4610–4618, Nov. 2020.
