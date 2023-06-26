from abc import ABC, abstractclassmethod


class LukisanAbstrak(ABC):

    @abstractclassmethod
    def warna(self):
        print("sub clsss ini harus menggunakan fungsi warna")


class Lukisan(LukisanAbstrak):
    def warna(self):
        print("dominasi warna tulisan adalah merah dan hijau")


class Hewan(ABC):
    @abstractclassmethod
    def perilaku(self):
        pass


class Ular(Hewan):
    def perilaku(self):
        print("berbisa dan melata")


class Anjing(Hewan):
    def perilaku(self):
        print("penciuman saya tajam")


ular = Ular()
ular.perilaku()
anjing = Anjing()
anjing.perilaku()

lukisan = LukisanAbstrak()
lukisan.warna()
