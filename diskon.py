class Cal:
    barang = 0
    diskon = 15/100

    def __init__(self, angka1, angka2):
        self.Angka1 = angka1
        self.Angka2 = angka2

    def tbh(self):  # Konstruktor
        print(f' hasil tambah : {self.Angka1 + self.Angka2}')
        print(f' hasil kali : {self.Angka1 * self.Angka2}')
        print(f' hasil bagi : {self.Angka1 / self.Angka2}')
        print(f' hasil kurang : {self.Angka1 - self.Angka2}')


a1 = int(input())  # Membuat Variabel input angka 1
a2 = int(input())  # Membuat variabel input angka 2
hasil = Cal(a1, a2)  # Membuat objek dari kelas Cal sesuai format
hasil.tbh()
