# Mencari Domain dan Range Dari Fungsi

Proyek ini menyediakan skrip Python untuk menghitung domain dan range dari fungsi matematika simbolik menggunakan pustaka SymPy. Pengguna dapat memberikan ekspresi fungsi dalam format string, dan sistem ini akan mengembalikan domain dan range dari fungsi tersebut.

## Fitur 

* **Menghitung domain dari fungsi matematika simbolik:** Fitur ini memungkinkan pengguna untuk menghitung domain fungsi secara otomatis dari ekspresi matematika simbolik.
* **Menghitung range dari fungsi berdasarkan domain yang sudah ditemukan:** Fitur ini menghitung range dari fungsi dengan memperhatikan domain yang sudah dihitung sebelumnya. Ini penting karena range fungsi bisa sangat berbeda tergantung pada pembatasan domain yang ada.
* **Menangani ekspresi fungsi dalam bentuk string:** Pengguna cukup memberikan fungsi dalam format string yang mudah dipahami, seperti '1/x', 'sin(x)', atau 'x**2'. Fungsi ini kemudian akan memproses ekspresi tersebut dan mengonversinya menjadi objek ekspresi simbolik yang dapat dianalisis secara matematis menggunakan SymPy.
* **Menghasilkan hasil dalam format simbolik yang dapat dimanipulasi lebih lanjut dengan pustaka SymPy:** Proyek ini memanfaatkan SymPy, pustaka Python untuk perhitungan simbolik. Dengan menggunakan SymPy, fungsi ini dapat menghitung domain dan range dari ekspresi simbolik dalam bentuk yang sangat fleksibel dan kuat.

## Struktur Kode

* **Fungsi analisis_fungsi:** Fungsi utama yang menerima ekspresi dalam format string dan mengembalikan domain dan range dari fungsi tersebut.
* **Fungsi temukan_domain_dan_range:** Fungsi pembantu yang digunakan untuk menghitung domain dan range dari ekspresi yang diberikan dalam format simbolik SymPy.
  
## Cara Penggunaaan Fungsi

1. **Install Python** Pastikan Anda sudah menginstal Python (lebih baik versi 3.x).
2. **Install Dictionary:** Install pustaka SymPy dengan menjalankan perintah berikut di terminal atau command prompt: **pip install sympy**
3. **Salin Kode:** Salin kode program yang diberikan ke dalam file Python.
4. **Panggil fungsi analisis_fungsi:** Gunakan fungsi **analisis_fungsi('ekspresi')** untuk menganalisis domain dan range dari ekspresi yang diberikan.
5. **Lihat hasil:** Cek hasil domain dan range yang dikembalikan oleh fungsi.
6. **Tangani Kesalahan (Opsional):** Tangani kesalahan dalam ekspresi atau analisis dengan mengecek hasil yang dikembalikan.

## Dependensi

Proyek ini membutuhkan SymPy, pustaka Python untuk perhitungan simbolik matematika.
* Sympy
