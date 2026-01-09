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
