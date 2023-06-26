class Ayah:
    _silsilah = "gledek"


class Anak(Ayah):  # class Anak(Ayah <- turunan dari class sebelumnya agar bisa mengambil attribute dari kelas sebelumnya)
    def cetakSilsilah(self):
        print("Silsilah anak adalah", self._silsilah)


anak1 = Anak()
anak1.cetakSilsilah()
