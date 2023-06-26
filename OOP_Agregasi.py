class Karyawan():
    def __init__(self, nama, nip):
        self.nama = nama
        self.nip = nip

    def gajian(self, honor):
        totalGaji = honor.gajiPokok + honor.lembur + honor.tunjangan
        totalGaji = totalGaji - honor.pajak
        print(self.nama, "Mendapatkan Honor sebanyak", totalGaji)


class Honor():
    def __init__(self, gajiPokok, lembur, tunjangan, pajak):
        self.gajiPokok = gajiPokok
        self.lembur = lembur
        self.tunjangan = tunjangan
        self.pajak = pajak


def main():
    arif = Karyawan("Arif", "001")
    honor = Honor(4000000, 1000000, 2000000, 50000)
    arif.gajian(honor)


main()
