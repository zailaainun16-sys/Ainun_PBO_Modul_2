class Buku:
    def __init__(self, judul, penulis, kode_buku, stok, lokasi_rak):
        self.judul = judul
        self.penulis = penulis
        self.kode_buku = kode_buku
        self._stok = stok
        self.__lokasi_rak = lokasi_rak

    # Getter & Setter Lokasi Rak
    def get_lokasi_rak(self):
        return self.__lokasi_rak

    def set_lokasi_rak(self, lokasi_baru):
        self.__lokasi_rak = lokasi_baru

    # Tambah & Kurangi Stok
    def tambah_stok(self, jumlah):
        self._stok += jumlah

    def kurangi_stok(self, jumlah):
        if self._stok >= jumlah:
            self._stok -= jumlah
            return True
        return False

    def info(self):
        return f"{self.kode_buku} - {self.judul} ({self.penulis}) | Stok: {self._stok} | Rak: {self.get_lokasi_rak()}"


class Anggota:
    def __init__(self, id_anggota, nama, maks_pinjam=3):
        self.id_anggota = id_anggota
        self.nama = nama
        self._maks_pinjam = maks_pinjam
        self.__status_aktif = True
        self.daftar_peminjaman = []  # aggregation

    # Getter & Setter Status
    def get_status(self):
        return self.__status_aktif

    def set_status(self, status_baru):
        self.__status_aktif = status_baru

    # Pinjam & Kembalikan Buku
    def pinjam_buku(self, peminjaman):
        if not self.__status_aktif:
            print("⚠ Anggota tidak aktif!")
            return
        if len(self.daftar_peminjaman) >= self._maks_pinjam:
            print("⚠ Telah mencapai batas maksimal peminjaman!")
            return
        if peminjaman.buku.kurangi_stok(1):
            peminjaman.status = "Dipinjam"
            self.daftar_peminjaman.append(peminjaman)
            print(f"✔ {self.nama} berhasil meminjam '{peminjaman.buku.judul}'")
        else:
            print(f"❌ Stok buku '{peminjaman.buku.judul}' habis!")

    def kembalikan_buku(self, peminjaman):
        if peminjaman in self.daftar_peminjaman:
            peminjaman.buku.tambah_stok(1)
            peminjaman.status = "Dikembalikan"
            self.daftar_peminjaman.remove(peminjaman)
            print(f"✔ {self.nama} mengembalikan '{peminjaman.buku.judul}'")
        else:
            print("⚠ Buku tersebut tidak sedang dipinjam oleh anggota ini")

    def info(self):
        return f"{self.id_anggota} - {self.nama} | Status: {'Aktif' if self.get_status() else 'Nonaktif'}"


class Peminjaman:
    def __init__(self, buku, tanggal_pinjam, tanggal_kembali):
        self.buku = buku
        self.kode_buku = buku.kode_buku
        self.tanggal_pinjam = tanggal_pinjam
        self.tanggal_kembali = tanggal_kembali
        self.status = "Belum Dipinjam"

    def info_peminjaman(self):
        return f"{self.buku.judul} | Pinjam: {self.tanggal_pinjam} | Kembali: {self.tanggal_kembali} | Status: {self.status}"


# ----------- DEMONSTRASI PROGRAM -----------
if __name__ == "__main__":
    # 3 Buku
    buku1 = Buku("Laskar Pelangi", "Andrea Hirata", "B001", 2, "Rak A1")
    buku2 = Buku("Negeri 5 Menara", "Ahmad Fuadi", "B002", 1, "Rak B2")
    buku3 = Buku("Ayat-Ayat Cinta", "Habiburrahman El Shirazy", "B003", 3, "Rak C3")

    # 2 Anggota
    anggota1 = Anggota("A01", "Dina")
    anggota2 = Anggota("A02", "Putra")

    # Peminjaman
    p1 = Peminjaman(buku1, "10-01-2025", "17-01-2025")
    p2 = Peminjaman(buku2, "10-01-2025", "17-01-2025")
    p3 = Peminjaman(buku3, "11-01-2025", "18-01-2025")

    # Anggota 1 pinjam 2 buku
    anggota1.pinjam_buku(p1)
    anggota1.pinjam_buku(p2)

    # Anggota 2 pinjam 1 buku
    anggota2.pinjam_buku(p3)

    # Pengembalian buku oleh anggota1
    anggota1.kembalikan_buku(p1)

    # ================= OUTPUT ================
    print("\n=== INFORMASI BUKU ===")
    print(buku1.info())
    print(buku2.info())
    print(buku3.info())

    print("\n=== INFORMASI ANGGOTA DAN DAFTAR PEMINJAMAN ===")
    for anggota in [anggota1, anggota2]:
        print("\n" + anggota.info())
        if anggota.daftar_peminjaman:
            for p in anggota.daftar_peminjaman:
                print(" -", p.info_peminjaman())
        else:
            print(" - Tidak ada buku yang sedang dipinjam")