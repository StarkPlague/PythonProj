class gaji():
    def hitung_gaji(self, karyawan):
        print("Menghitung gaji")
        print("______________")
        for karyawan in gaji:
            print(f'gaji untuk: {karyawan.id} - {karyawan.nama}')
            print(f'- Total: {karyawan.hitung_gaji()}')
            print("")


class Karyawan:
    def __init__(self, id, nama):
        self.id = id
        self.nama = nama


class GajiKaryawan(Karyawan):
    def __init__(self, id, nama, gaji_mingguan):
        super().__init__(id, nama)
        self.gaji_karyawan = gaji_mingguan

    def hitung_gaji(self):
        return self.gaji_mingguan


class GajiJam(Karyawan):
    def __init__(self, id, nama, kerja_perjam, gaji_perjam):
        super().__init__(id, nama)
        self.kerja_perjam = kerja_perjam
        self.gaji_perjam = gaji_perjam

    def hitung_gaji(self):
        return self.kerja_perjam * self.gaji_perjam


class KomisiKaryawan(GajiKaryawan):
    def __init__(self, id, nama, gaji_mingguan, komisi):
        super().__init__(id, nama, gaji_mingguan)
        self.komisi = komisi

    def HitungGaji(self):
        total = super().hitung_gaji()
        return total + self.komisi


gaji_karyawan = GajiKaryawan(1, "Budi", 5000000)
gaji.hitung_gaji(gaji_karyawan)
