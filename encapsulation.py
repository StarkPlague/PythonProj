# SETTER AND GETTER

class Ayah:
    _silsilah = "gledek"


class Anak(Ayah):  # class Anak(Ayah <- turunan dari class sebelumnya agar bisa mengambil attribute dari kelas sebelumnya)
    def __init__(self, nama, umur):
        self.__nama = nama
        self.__umur = umur

    def cetakSilsilah(self):
        print("Silsilah anak adalah", self._silsilah)

    def setNama(self, namaBaru):  # untuk merubah settings dari self.__nama yang private
        self.__nama = namaBaru

    def getNama(self):  # untuk mengambil/mengembalikan data yang sudah di ubah melalui Setter ^^^^
        return self.__nama

    @classmethod  # Bisa memanggil class tanpa membuat objek kembali.
    def cetakClassMethod(cls):
        print("ini adalah class method")


anak1 = Anak("budi", 12)
anak2 = Anak("Andi", 13)
print(anak1.getNama())
print(anak2.nama)

anak1.setNama("Andi")  # Merubah data dari private method (self.__nama)

# Mengambil data dari private method (self.__nama) yang sudah diubah.
print(anak1.getNama())

anak1.cetakClassMethod()  # ???
Anak.cetakClassMethod()  # @classmethod
