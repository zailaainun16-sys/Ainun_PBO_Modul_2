class Mahasiswa:
    def __init__(self, nim, nama, semester, ipk):
        self.nim = nim               # public
        self.nama = nama             # public
        self._semester = semester    # protected
        self.__ipk = ipk             # private

    # Getter protected (semester)
    def get_semester(self):
        return self._semester

    # Getter private (ipk)
    def get_ipk(self):
        return self.__ipk


# Contoh penggunaan
if __name__ == "__main__":
    m1 = Mahasiswa("202412035", "Hasan", 2, 3.25)
    m2 = Mahasiswa("202412036", "Ainun", 2, 3.80)

    print("=== Data Mahasiswa 1 ===")
    print("NIM:", m1.nim)
    print("Nama:", m1.nama)
    print("Semester:", m1.get_semester())
    print("IPK:", m1.get_ipk())

    print("\n=== Data Mahasiswa 2 ===")
    print("NIM:", m2.nim)
    print("Nama:", m2.nama)
    print("Semester:", m2.get_semester())
    print("IPK:", m2.get_ipk())
