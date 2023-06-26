# Method Resolution Order
class Ayah:
    def __init__(self, nama):
        self.nama = nama

    def tampilkanNama(self):
        print("Nama Saya: ", self.nama)


class Ibu:
    def __init__(self, nama):
        self.nama = nama

    def tampilkanNama(self):
        print("Nama Saya: ", self.nama)


# (3) akan mengecek tampilkanNama() di kelas lain, sesuai urutan. Ayah dlu baru ibu.
class Anak(Ayah, Ibu):
    def __init__(self, nama):
        self.nama = nama
        print("Nama Saya: ", self.nama)

    # (2) Mengecek apakah ada "tampilkanNama()" di sini, jika tidak ada maka
    def tampilkanNama(self):
        print("Nama Saya: ", self.nama)


anak = Anak("Muhammad Soleh")
# (1) ketika memanggil fungsi seperti ini, akan mengecek method nya di kelas anak.
anak.tampilkanNama()
# help(anak)
