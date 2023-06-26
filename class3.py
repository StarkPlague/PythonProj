
# Multiple Inheritence
# inheritence atau pewarisan memungkinkan penggunaan class dengan attribute dari kelas lain.
class Ayah:
    silsilah = "Pambudi"

    def sebutSilsilah(self):
        print(self.silsilah)


class Ibu:
    silsilah = "Pambudo"


class Anak(Ayah, Ibu):

    def __init__(self):
        # super() bakal mengambil dari kelas ayah nya, super() digunakan jika ada method yang sama dalam 2 class
        super().sebutSilsilah
        self.sebutSilsilah()

    def sebutSilsilah(self):
        print("Silsilah anak")


anak1 = Anak()
print(anak1.silsilah)
