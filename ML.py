
from itertools import chain


item = []
hero = []
hero_Att = []
heroItem = []
lordHealth = []
cekhero = []
herospec = []


class Lord:

    def __init__(self, Lord, h):
        self.namaLord = Lord
        self.health = int(h)

    def get_hp(self):
        return self.hp

    def isAttacked(self, h):
        self.health -= h


class Item:
    def __init__(self, i, ia):
        self.nama = i
        self.iAtt = ia


class Hero:
    def __init__(self, n, a):
        self.nama = n
        self.att = int(a)

    def heroAtt(self, n, a):
        self.nama = n
        self.att = int(a)

    def tambah_item(self, a):
        self.att += int(a)

    def ganti_item(self, a):
        self.att -= a


class heroSpec:
    def __init__(self, n, att, it):
        self.nama = n
        self.attack = att
        self.item = it


def index2d(i):
    for j, k in enumerate(hero):
        if k.nama == i:
            return j
    return -1


def index2dItem(i):
    for j, k in enumerate(item):
        if k.nama == i:
            return j
    return -1


def index2dheroI(i):
    for j, k in enumerate(heroItem):
        if k.nama == i:
            return j
    return -1


def index2dheroAtt(i):
    for j, k in enumerate(hero_Att):
        if k.nama == i:
            return j
    return -1


def index2dspec(i):
    for j, k in enumerate(herospec):
        if k.nama == i:
            return j
    return -1


def Main():
    i = 1
    jmlHero = int(input("Masukkan Jumlah Hero: "))
    while (i < jmlHero+1):
        nmHero = input()
        fmHero = nmHero.split("%")
        hero.append(Hero(fmHero[0], fmHero[1]))  # Masuk ke list hero = []
        i += 1

    j = 1
    jmlItem = int(input("Masukkan Jumlah item: "))
    while (j < jmlItem+1):
        nmItem = input()
        fmItem = nmItem.split(";")
        item.append(Item(fmItem[0], fmItem[1]))  # Masuk ke list item = []
        j += 1

    if j == jmlItem+1:
        print("!! Lord Respawn !!")
        nmLord = input()
        fmLord = nmLord.split("*")
        lordHealth.append(Lord(fmLord[0], fmLord[1]))
        print("!! Welcome to Hero vs Lord")
        print("// Five Seconds 'til the Lord reach the battlefiled, smash him. //")
        # Memunculkan hp lord
        while True:
            x = input()
            y = x.split(";")
            if y[0] == "PILIH ITEM":
                if hero[index2d(y[1])].nama in cekhero:
                    print(y[1],  "sudah memiliki senjata!")
                else:
                    he = hero[index2d(y[1])]
                    it = item[index2dItem(y[2])]
                    heroItem.append(Item(he.nama, it.nama))
                    cekhero.append(he.nama)
                    hero_Att.append(Hero(he, it.iAtt))
                    he.tambah_item(it.iAtt)
                    herospec.append(heroSpec(he.nama, he.att, it.nama))
                    print(f'{he.nama} berhasil memakai {it.nama} !')

            elif y[0] == "GANTI ITEM":
                he = hero[index2d(y[1])]
                it = item[index2dItem(y[2])]
                he.ganti_item(hero_Att[index2dheroAtt(y[1])].att)
                he.tambah_item(int(it.iAtt))
                print(
                    f'{heroItem[index2dheroI(y[1])].iAtt} diganti menjadi {y[2]}')
                herospec.pop(index2dspec(y[1]))
                herospec.append(heroSpec(he.nama, he.att, it.nama))
                del heroItem[index2dheroI(y[1])]
                heroItem.append(Item(he.nama, it.nama))
            elif y[0] == "MULAI MENYERANG":
                if len(heroItem) < jmlHero:
                    print(
                        "Tidak bisa menyerang karena belum semua hero memakai senjata")
                else:
                    lord_hp = lordHealth[0]
                    while lord_hp != 0:
                        for i in herospec:
                            lord_hp.isAttacked(i.attack)
                            if lord_hp.health < 0:
                                lord_hp.health = 0
                            print(
                                f'{i.nama} menyerang {lord_hp.namaLord} dengan senjata {i.item} sebesar {i.attack}, HP {lord_hp.namaLord} sekarang {lord_hp.health}')
                        if lord_hp.health == 0:
                            break


Main()
