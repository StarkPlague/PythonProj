class Penjual():
    def __init__(self, nama, barang, harga):
        self.nama = nama
        self.barang = barang
        self.harga = harga

    def jual(self, pembeli):
        print(self.nama, "menjual", self.barang,
              "kepada", pembeli, "seharga", self.harga)

#asosiasi = berinteraksi


class Pembeli():
    def __init__(self, nama):
        self.nama = nama


def main():
    print("Hubungan asosiasi antara penjual dan pembeli")
    arif = Penjual("Arif", "Semangka", 10000)
    budi = Pembeli("Budi")
    arif.jual(budi.nama)


main()
