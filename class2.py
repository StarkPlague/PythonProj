class Orang:
    NamaLain = "Herman"

    def __init__(self, nama, jenis_kelamin):
        self.nama = nama
        self.jk = jenis_kelamin

    def cetak(self):
        print(f'nama : {self.nama} {self.NamaLain}')
        print(f'jenis kelamin : {self.jk}')


orang1 = Orang("Budi", "L")
orang2 = Orang("Maria", "P")
print(orang1.nama)

print(orang1.jk)

print(orang2.nama, orang2.jk)

orang1.cetak()
