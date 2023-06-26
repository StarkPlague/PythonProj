
class total:
    diskon = 15/100
    barang = 0
    total = 0

    def bar(self):
        return self.barang

    def harga(self, tambahBarang):
        self.barang = self.barang+tambahBarang


class Dis(total):
    def harga(self, tambahBarang):
        super().harga(tambahBarang)
        self.pajak = self.barang * super().diskon


barang1 = int(input())
hasil = total(barang1)

print(hasil)
