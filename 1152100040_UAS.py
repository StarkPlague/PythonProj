from random import randrange
import random


penyakit = {
    "Batuk": {
        "Lasal Expectorant", "Transpulmin Syrup", "Levopront"
    },
    "Pilek": {
        "Paracetamol", "ibuprofen", "Loratadine"
    }
}

dokter = {
    "Batuk": "Izuma",
    "Pilek": "Samsudin"
}

harga = [10000, 20000, 30000, 40000, 50000, 60000, 70000]


class Pasien():
    def __init__(self, nama, umur, jeniskelamin, sakit):
        self.nama = nama
        self.umur = umur
        self.jeniskelamin = jeniskelamin
        self.sakit = sakit


class Dokter():
    def __init__(self, nama, spesialis, apotek):
        self.nama = nama
        self.spesialis = spesialis
        self.apotek = apotek


class Obat():
    def __init__(self, resep, harga):
        self.resep = resep
        self.harga = harga

    @property
    def info(self):
        return "Obat: {} Harga: {}".format(self.resep, self.harga)


list_obat = []


def Command():
    # NAMA UMUR JENISKELAMIN SAKIT
    command = input("Silahkan Masukkan data diri anda: ")
    split = command.split()
    pasien = Pasien(split[0], split[1], split[2], split[3])
    if pasien.sakit == "Batuk":
        print(
            f'Nama Pasien: {pasien.nama}\nUmur: {pasien.umur}\nJenis Kelamin:{pasien.jeniskelamin}\nKeluhan: {pasien.sakit}')
        r = random.choice(harga)
        obat = Obat(i, int(r))
        print(
            f"Silahkan menunggu antrean untuk Dokter {dokter['Batuk']}\nResep : ")
        print(obat.info)

    elif pasien.sakit == "Pilek":
        print(
            f'Nama Pasien: {pasien.nama}\nUmur: {pasien.umur}\nJenis Kelamin:{pasien.jeniskelamin}\nKeluhan: {pasien.sakit}')
        for i in penyakit[split[3]]:
            r = random.choice(harga)
            obat = Obat(i, int(r))
        print(
            f"Silahkan menunggu antrean untuk Dokter {dokter['Pilek']}\nResep : ")
        print(obat.info)


Command()
