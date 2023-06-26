# Hierarchical Inhertitence

from abc import ABC, abstractclassmethod


class cal(ABC):
    @abstractclassmethod
    def hitung(self):
        pass


class tambah(cal):

    def hitung(self):
        a1 = input()
        a2 = input()
        a = int(float(a1)) + int(float(a2))
        print(a)


class kurang(cal):
    def __init__(self, a1, a2):
        self.angka1 = a1
        self.angka2 = a2

    def hitung(self):
        a = self.angka1 - self.angka2
        print(a)


class bagi(cal):
    def __init__(self, a1, a2):
        self.angka1 = a1
        self.angka2 = a2

    def hitung(self):
        a = self.angka1 / self.angka2
        print(a)


class kali(cal):
    def __init__(self, a1, a2):
        self.angka1 = a1
        self.angka2 = a2

    def hitung(self):
        a = self.angka1 * self.angka2
        print(a)


Tambah = tambah()
Tambah.hitung()
