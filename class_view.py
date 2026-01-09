from class_data import Mahasiswa
from class_process import NilaiProcess


class MainView:

    @staticmethod
    def jalankan():
        try:
            nim = input("Masukkan Nama Mahasiswa  : ")
            nama = input("Masukkan Nim Mahasiswa : ")
            nilai = int(input("Masukkan Nilai        : "))

    
            NilaiProcess.validasi_nilai(nilai)

            mhs = Mahasiswa(nama, nim, nilai)
            grade = NilaiProcess.hitung_grade(nilai)

            print("\n+----------------------------------+")
            print("|          HASIL NILAI              |")
            print("+-------------------+--------------+")
            print("| NIM               | {:<12} |".format(mhs.nama))
            print("| Nama Mahasiswa    | {:<12} |".format(mhs.nim))
            print("| Nilai             | {:<12} |".format(mhs.nilai))
            print("| Grade             | {:<12} |".format(grade))
            print("+-------------------+--------------+")

        except ValueError as e:
            print("Error:", e)

if __name__ == "__main__":
    MainView.jalankan()