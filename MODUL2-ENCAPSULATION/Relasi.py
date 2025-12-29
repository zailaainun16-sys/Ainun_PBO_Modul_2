# relasi aggregation
class Nilai:
    def __init__(self, kode_mk: str, skor: float):
        self.kode_mk = kode_mk
        self.skor = skor


class Mahasiswa:
    def __init__(self, nim, nama):
        self.nim = nim
        self.nama = nama
        self.daftar_nilai = []   # agregasi: Nilai dapat berdiri sendiri

    def tambah_nilai(self, nilai):
        self.daftar_nilai.append(nilai)

    # (f) method rata-rata nilai mahasiswa
    def rata_rata(self):
        if not self.daftar_nilai:
            return 0
        return sum(n.skor for n in self.daftar_nilai) / len(self.daftar_nilai)


class MataKuliah:
    def __init__(self, kode: str, nama: str):
        self.kode = kode
        self.nama = nama


class ProgramStudi:
    def __init__(self, nama):
        self.nama = nama
        self.daftar_matakuliah = []  # agregasi

    def tambah_matakuliah(self, mk: MataKuliah):
        self.daftar_matakuliah.append(mk)


# relasi composition
class Universitas:
    def __init__(self, nama):
        self.nama = nama
        self.programs = []

    def buat_program(self, nama_prodi):
        prodi = ProgramStudi(nama_prodi)
        self.programs.append(prodi)
        return prodi


# fungsi report program
def report_program(prodi: ProgramStudi, semua_mahasiswa: list[Mahasiswa]):
    print(f"\nProgram Studi: {prodi.nama}")
    print("Mata Kuliah:", ", ".join([mk.kode for mk in prodi.daftar_matakuliah]) or "-")
    print("Mahasiswa dan rata-rata nilai:")
    for m in semua_mahasiswa:
        relevan = [n for n in m.daftar_nilai if any(n.kode_mk == mk.kode for mk in prodi.daftar_matakuliah)]
        if relevan:
            avg = sum(n.skor for n in relevan) / len(relevan)
            print(f" {m.nim} - {m.nama}: {round(avg, 2)}")
    print("-" * 40)


# ---------------------------
# MAIN PROGRAM
# ---------------------------
if __name__ == "__main__":
    # Universitas
    uni = Universitas("Universitas A")

    # Program Studi (a)
    prodi_ti = uni.buat_program("Teknik Informatika")
    prodi_si = uni.buat_program("Sistem Informasi")
    prodi_mi = uni.buat_program("Bisnis Digital")

    # Tambahkan mata kuliah (b)
    prodi_ti.tambah_matakuliah(MataKuliah("TI101", "Pemrograman Dasar"))
    prodi_ti.tambah_matakuliah(MataKuliah("TI102", "Struktur Data"))

    prodi_si.tambah_matakuliah(MataKuliah("SI201", "Analisis Sistem"))
    prodi_si.tambah_matakuliah(MataKuliah("SI202", "Basis Data"))

    prodi_mi.tambah_matakuliah(MataKuliah("MI301", "Administrasi Bisnis"))
    prodi_mi.tambah_matakuliah(MataKuliah("MI302", "Akuntansi Dasar"))

    # Mahasiswa (c)
    m1 = Mahasiswa("202412035", "BudiHasan")
    m2 = Mahasiswa("202412036", "Ainun")
    m3 = Mahasiswa("202412037", "Herdi")

    # Tambahkan nilai (c)
    m1.tambah_nilai(Nilai("TI101", 85))
    m1.tambah_nilai(Nilai("SI201", 90))

    m2.tambah_nilai(Nilai("TI102", 98))
    m2.tambah_nilai(Nilai("MI301", 88))

    m3.tambah_nilai(Nilai("SI202", 92))
    m3.tambah_nilai(Nilai("MI301", 75))

    semua_mahasiswa = [m1, m2, m3]

    # (d) Tampilkan daftar mata kuliah setiap Program Studi
    print("\n=== Daftar Mata Kuliah Per Program Studi ===")
    for p in uni.programs:
        print(f"{p.nama}:")
        for mk in p.daftar_matakuliah:
            print(f" - {mk.kode} | {mk.nama}")

    # (e) Tampilkan daftar nilai setiap mahasiswa
    print("\n=== Daftar Nilai Mahasiswa ===")
    for m in semua_mahasiswa:
        print(f"{m.nim} - {m.nama}")
        for n in m.daftar_nilai:
            print(f"  {n.kode_mk}: {n.skor}")
        print(f"  Rata-rata: {round(m.rata_rata(), 2)}")  # (f)

    # (g) Panggil fungsi report_program untuk setiap program studi
    print("\n=== REPORT PROGRAM STUDI ===")
    report_program(prodi_ti, semua_mahasiswa)
    report_program(prodi_si, semua_mahasiswa)
    report_program(prodi_mi, semua_mahasiswa)