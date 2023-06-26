class Siswa():
    def __init__(self, nama):
        self.nama = nama
        self.nis = NIS(None, None)


class NIS():
    def __init__(self, sekolah, idNis):
        self.sekolah = sekolah
        self.idnis = idNis

    def cetakDaftar(self):
        print("Siswa", self.idnis, "dari", self.sekolah, "Terdaftar")


def main():
    siswa = Siswa("siswa")
    siswa.nis.sekolah = input("Masukkan nama sekolah: ")
    siswa.nis.idnis = input("Masukkan NIS: ")
    siswa.nis.cetakDaftar()


main()
