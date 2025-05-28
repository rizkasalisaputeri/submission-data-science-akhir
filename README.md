# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding

Jaya Jaya Institut merupakan institusi pendidikan tinggi yang mengalami tantangan serius terkait tingginya tingkat mahasiswa yang tidak menyelesaikan studi (dropout). Hal ini tidak hanya berdampak pada reputasi institusi, tetapi juga pada efisiensi penggunaan sumber daya pendidikan.

Sebagai bentuk antisipasi, diperlukan sistem prediktif untuk mengidentifikasi mahasiswa yang berisiko tinggi melakukan dropout, agar bisa diberikan dukungan lebih awal. Solusi berbasis data science diperlukan untuk menyelesaikan permasalahan ini.

### Permasalahan Bisnis

- Tingginya angka dropout mahasiswa dari tahun ke tahun.
- Belum ada sistem deteksi dini berbasis data untuk memprediksi potensi dropout.
- Minimnya wawasan terkait faktor-faktor yang berkontribusi terhadap kegagalan studi mahasiswa.

### Cakupan Proyek

- Melakukan eksplorasi data (EDA) untuk memahami distribusi status mahasiswa.
- Menganalisis hubungan antara faktor-faktor seperti gender, beasiswa, nilai masuk, dan status finansial terhadap status akhir mahasiswa.
- Membangun model prediksi mahasiswa dropout.
- Membuat dashboard interaktif untuk membantu pemantauan performa dan risiko dropout mahasiswa.

### Persiapan

**Sumber Data:**  
Dataset yang digunakan berasal dari file `data.csv`, yaitu kumpulan data bernama **Student's Performance** dari institusi pendidikan tinggi. Dataset mencakup informasi demografi, sosial-ekonomi, dan performa akademik mahasiswa pada semester awal yang diakses pada link berikut.
[https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv](https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv)

**Setup environment:**

```
# Instalasi dependencies
pip install pipenv
pipenv install
pipenv shell
pip install -r requirements.txt

```

## Business Dashboard
Dashboard dibuat menggunakan Metabase dan berisi beberapa visualisasi utama :
1. Distribusi status mahasiswa (Dropout, Graduate, Enrolled) di institusi
2. Pengaruh Jenis Kelamin terhadap Dropout
3. Hubungan mahasiswa yang memiliki utang dengan Risiko Dropout
4. Perbedaan Proporsi Dropout Berdasarkan Beasiswa

### Fungsi Dashboard

Dashboard ini digunakan untuk:
- Mengidentifikasi kelompok mahasiswa yang berisiko tinggi dropout
- Menganalisis faktor-faktor seperti gender, utang, dan beasiswa
- Memberi insight kepada pihak akademik untuk penanganan lebih awal terhadap potensi dropout

```
# Jalankan Metabase (dengan Docker)
docker run -d ^
  --name <nama_kontainer> ^
  -p 3000:3000 ^
  -v "<path_local_proyek>:/<direktori di kontainer>" ^
  -e "MB_DB_FILE=/<direktori di kontainer>/metabase.db" ^
  metabase/metabase

# Menambahkan Data Source SQLite
Setelah Metabase jalan:
1. Masuk ke Admin settings → Databases → Add database
2. Pilih SQLite
3. Masukkan Database file path:
  /<direktori_di_kontainer>/data_mahasiswa.db
4. Klik Save

```

Akses Dashboard:
```
Email: rizkasalisaputeri@gmail.com
Password: dicoding123
URL: http://localhost:3000

```

## Menjalankan Sistem Machine Learning
Sistem machine learning dibangun menggunakan Random Forest Classifier dan telah di-deploy sebagai prototype menggunakan Streamlit.

Untuk mengakses prototype streamlit:

```
https://submission-data-science-akhir.streamlit.app/

```

Untuk mengakses prototype streamlit secara lokal:

```
streamlit run app.py

```
File model telah disimpan sebagai model.pkl.

## Conclusion

Hasil analisis menunjukkan bahwa tingkat dropout mahasiswa cukup tinggi, dipengaruhi oleh beberapa faktor utama seperti kepemilikan beasiswa, status sebagai debitur, jenis kelamin, dan performa akademik. Visualisasi pada dashboard mengungkap bahwa mahasiswa tanpa beasiswa lebih sering dropout, begitu juga dengan mahasiswa yang memiliki utang. Selain itu, mahasiswa laki-laki memiliki tingkat dropout lebih tinggi dibandingkan perempuan. Rasio kelulusan mata kuliah (unit disetujui vs terdaftar) juga menjadi indikator penting dalam menentukan risiko. Model prediksi yang dibangun menggunakan Random Forest menghasilkan akurasi sebesar 86%, yang cukup baik untuk membantu institusi mengidentifikasi mahasiswa berisiko dan melakukan intervensi lebih awal.

### Rekomendasi Action Items

Berikut beberapa rekomendasi yang dapat dilakukan oleh Jaya Jaya Institut:

- Lakukan pemantauan terhadap mahasiswa yang diprediksi berisiko dropout tinggi dan berikan bimbingan secara rutin.
- Perluas akses dan kuota beasiswa karena terbukti dapat mengurangi angka dropout.
- Gunakan dashboard Metabase sebagai alat pemantauan rutin oleh tim akademik.
- Evaluasi dan latih ulang model machine learning secara berkala untuk menjaga akurasi prediksi.
- Koordinasikan antara bagian keuangan dan tim konselor untuk memberikan dukungan bagi mahasiswa yang mengalami kendala finansial.
