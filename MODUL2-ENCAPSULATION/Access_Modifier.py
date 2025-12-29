class Mahasiswa:
    def __init__(self, nim, nama, semester, ipk):
        self.nim = nim               # public
        self.nama = nama             # public
        self._semester = semester    # protected
        self.__ipk = ipk             # private

    # Getter protected (semester)
    def get_semester(self):
        return self._semester

    # Setter protected (semester)
    def set_semester(self, smt_baru):
        if smt_baru <= 0:
            raise ValueError("Semester harus lebih dari 0.")
        self._semester = smt_baru

    # Getter private (ipk)
    def get_ipk(self):
        return self.__ipk

    # Setter private (ipk)
    def set_ipk(self, nilai_baru):
        if not (0.0 <= nilai_baru <= 4.0):
            raise ValueError("IPK harus antara 0.0 - 4.0.")
        self.__ipk = round(nilai_baru, 2)


# Contoh penggunaan
if __name__ == "__main__":
    mhs = Mahasiswa("23001", "Budi", 2, 3.25)

    print("NIM:", mhs.nim)
    print("Nama:", mhs.nama)
    print("Semester:", mhs.get_semester())
    print("IPK:", mhs.get_ipk())

    mhs.set_semester(3)
    print("Semester Baru:", mhs.get_semester())

    mhs.set_ipk(3.85)
    print("IPK Baru:", mhs.get_ipk())