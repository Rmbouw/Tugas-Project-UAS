# Program Pengolahan Nilai Mahasiswa (Python OOP)

##  Deskripsi Program
<md>Program ini merupakan aplikasi sederhana berbasis **Python** yang digunakan untuk mengolah nilai mahasiswa menggunakan konsep **Object Oriented Programming (OOP)**.  
Program memisahkan fungsi menjadi tiga bagian utama, yaitu **Data**, **Process**, dan **View** agar struktur kode lebih rapi, terorganisir, dan mudah dipahami.</md>

Program berjalan di **terminal (CLI)** dan menampilkan hasil nilai mahasiswa dalam bentuk **tabel**.


## Struktur File Program
📁 project-folder<br>
│<br>
├── class_data.py<br>
├── class_process.py<br>
└── class_view.py
<pre>
Penjelasan:
- `class_data.py` → Menyimpan data mahasiswa
- `class_process.py` → Mengelola proses dan logika
- `class_view.py` → Menampilkan tampilan dan input/output



Penjelasan Setiap File

 class_data.py (Class Data)
File ini berfungsi untuk **menyimpan data mahasiswa**.

Atribut yang disimpan:
- NIM
- Nama Mahasiswa
- Nilai

<pre>class Mahasiswa:
    def __init__(self, nim, nama, nilai):
        self.nim = nim
        self.nama = nama
        self.nilai = nilai</pre>

<b>File ini tidak memiliki logika perhitungan, hanya sebagai tempat penyimpanan data.</b>
</pre>
<pre>class_process.py (Class Process)
File ini berisi logika program, yaitu:
Validasi nilai
Perhitungan grade
class NilaiProcess:

    @staticmethod
    def validasi_nilai(nilai):
        if nilai < 0 or nilai > 100:
            raise ValueError("Nilai harus di antara 0 - 100")

    @staticmethod
    def hitung_grade(nilai):
        if nilai >= 80:
            return "A"
        elif nilai >= 70:
            return "B"
        elif nilai >= 60:
            return "C"
        else:
            return "D"
</pre>
<pre>Menggunakan @staticmethod karena method ini tidak bergantung pada objek.
class_view.py (Class View)
File ini bertugas sebagai tampilan utama program, meliputi:
Input data dari pengguna
Pemanggilan class Data dan Process
Menampilkan output dalam bentuk tabel</pre>

<b><pre>from class_data import Mahasiswa
from class_process import NilaiProcess</b></pre>


File ini menjadi entry point program dan dijalankan pertama kali.

### Contoh Output Program
<pre>Masukkan NIM Mahasiswa  : 23101123
Masukkan Nama Mahasiswa : Agus
Masukkan Nilai          : 85

+----------------------------------+
|          HASIL NILAI              |
+-------------------+--------------+
| NIM               | 23101123     |
| Nama Mahasiswa    | Agus         |
| Nilai             | 85           |
| Grade             | A            |
+-------------------+--------------+
kalau Nilainya Lebih Dari 100 maka pada bagian perintahnya menampilkan eror</pre>

### Cara Menjalankan Program
<li>Buka terminal di folder project
<li>Jalankan perintah berikut:
<li>python class_view.py atau Klik pada menu pousennya</li>

<pre>Konsep OOP yang Digunakan
Class & Object
Constructor (__init__)
Atribut dan Method
Static Method
Pemrograman Modular</pre>

### Kesimpulan
Program ini menerapkan konsep Object Oriented Programming dengan pemisahan tugas yang jelas antara data, proses, dan tampilan.
Struktur program menjadi lebih rapi, mudah dikembangkan, dan sesuai dengan standar pemrograman Python.


