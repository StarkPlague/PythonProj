from random import *

# Fa'iq Ali Sutiono
# 1152100040

listHeroMag = {
    1: {
        "hero": "Gord",
        "type": "Magic",
        "bAtt": 100,
        "mAtt": 100,
        "hp": 800,
        "def": 100,
        "skill": {
            "ulti": "Mystic Gush",
            "uAtt": 10,
            "uDef": 80}
    },
    2: {
        "hero": "Harley",
        "type": "Magic",
        "bAtt": 100,
        "mAtt": 200,
        "hp": 700,
        "def": 200,
        "skill": {
            "ulti": "Deadly Magic",
            "uAtt": 20,
            "uDef": 70}
    },
    3: {
        "hero": "Lunox",
        "type": "Magic",
        "bAtt": 100,
        "mAtt": 300,
        "hp": 600,
        "def": 300,
        "skill": {
            "ulti": "Order & Chaos",
            "uAtt": 30,
            "uDef": 60},
        "pasifAtt": 200,
    },
    4: {
        "hero": "Guinevere",
        "type": "Magic",
        "bAtt": 100,
        "mAtt": 400,
        "hp": 500,
        "def": 400,
        "skill": {
            "ulti": "Violet Requiem",
            "uAtt": 40,
            "uDef": 50}
    },
    5: {
        "hero": "Harith",
        "type": "Magic",
        "bAtt": 100,
        "mAtt": 500,
        "hp": 400,
        "def": 500,
        "skill": {
            "ulti": "Zaman Force",
            "uAtt": 50,
            "uDef": 40}
    },
    6: {
        "hero": "Valir",
        "type": "Magic",
        "bAtt": 100,
        "mAtt": 600,
        "hp": 300,
        "def": 600,
        "skill": {
            "ulti": "Vengeance Flame",
            "uAtt": 60,
            "uDef": 30}
    },
    7: {
        "hero": "Pharsa",
        "type": "Magic",
        "bAtt": 100,
        "mAtt": 700,
        "hp": 200,
        "def": 700,
        "skill": {
            "ulti": "Feathered Air Strike",
            "uAtt": 70,
            "uDef": 20},
        "pasifAtt": 200
    },
    8: {
        "hero": "Cecillion",
        "type": "Magic",
        "bAtt": 100,
        "mAtt": 800,
        "hp": 100,
        "def": 800,
        "skill": {
            "ulti": "Bats Feast",
            "uAtt": 80,
            "uDef": 10}
    }

}

listHerophy = {
    1: {
        "hero": "Saber",
        "type": "physical",
        "bAtt": 235,
        "pAtt": 400,
        "hp": 400,
        "def": 400,
        "skill": {
            "ulti": "Triple Sweep",
            "uAtt": 20,
            "uDef": 10},
        "pasifAtt": 200
    },
    2: {
        "hero": "Bennedeta",
        "type": "physical",
        "bAtt": 300,
        "pAtt": 500,
        "hp": 300,
        "def": 500,
        "skill": {
            "ulti": "Alecto: Final Blow",
            "uAtt": 30,
            "uDef": 15},
        "pasifAtt": 200
    },
    3: {
        "hero": "Chou",
        "type": "physical",
        "bAtt": 150,
        "pAtt": 300,
        "hp": 500,
        "def": 300,
        "skill": {
            "ulti": "The Way of Dragon",
            "uAtt": 40,
            "uDef": 20},
        "pasifAtt": 200
    }
}

dictHeroUlti = {

}

heroPhy = []
heroMag = []
Item = []
heroItem = []


class Hero():
    def __init__(self, hero, type, bAtt, hp, item,):
        self.hero = hero
        self.type = type
        self.bAtt = int(bAtt)
        self.hp = int(hp)
        self.item = item


class Physical(Hero):
    def __init__(self, hero, type, bAtt, hp, item, heroatt, Defense):
        super().__init__(hero, type, bAtt, hp, item)
        self.heroatt = heroatt
        self.Defense = Defense


class Magic(Hero):
    def __init__(self, hero, type, bAtt, hp, item, heroatt, Defense):
        super().__init__(hero, type, bAtt, hp, item)
        self.heroatt = heroatt
        self.Defense = Defense


class Skill():
    def __init__(self, skill, att, sdefense):
        self.skill = skill
        self.att = att
        self.sdefense = sdefense


class item_():
    def __init__(self, item, damage):
        self.nama = item
        self.damage = damage


def buat_skill():
    for i in listHeroMag:
        dictHeroUlti[listHeroMag[i]["hero"]] = Skill(
            listHeroMag[i]["skill"]["ulti"], listHeroMag[i]["skill"]["uAtt"], listHeroMag[i]["skill"]["uDef"])
    for i in listHerophy:
        dictHeroUlti[listHerophy[i]["hero"]] = Skill(
            listHerophy[i]["skill"]["ulti"], listHerophy[i]["skill"]["uAtt"], listHerophy[i]["skill"]["uDef"])


def daftar_heromagic():
    print(f"Daftar nama hero magic\n$$$$$$$$$$$$$$$$$$$$")
    for i in listHeroMag:
        print(listHeroMag[int(i)]["hero"])


def daftar_herophysic():
    print(f"Daftar nama hero magic\n$$$$$$$$$$$$$$$$$$$$")
    for i in listHerophy:
        print(listHerophy[int(i)]["hero"])


def daftar_ulti(dict):
    print(f"Daftar nama skill hero magic\n$$$$$$$$$$$$$$$$$$$$")
    for i in dict:
        print(dict[int(i)]["hero"],
              "Memiliki skill", dict[int(i)]["ulti"])


mag = []
phy = []
merge = []

hero_fight = []


def pilih_hero(dicti, dicti_):
    jml = range(0, len(dicti))
    smp = sample(jml, 3)
    for i in smp:
        hero = dicti[int(i+1)]["hero"]
        mag.append(hero)
        merge.append(hero)
    jml = range(0, len(dicti_))
    smp_ = sample(jml, 3)
    for j in smp_:
        hero = dicti_[int(j+1)]["hero"]
        phy.append(hero)
        merge.append(hero)


def buat_item():
    item = 1
    while True:
        print(f'item ke - {item}\nMasukan attribut item / berhenti')
        inputitem = input()
        if inputitem == "Berhenti":
            beli_item()
            break
        splititem = inputitem.split("#")
        Item.append(item_(splititem[0], int(splititem[1])))
        item += 1


items = []
hero_item = []


def beli_item():
    jml = range(0, len(Item))
    smp = sample(jml, len(Item))
    for i in smp:
        items.append(Item[i])
    itemmag = items[0:2]
    itemphy = items[3:5]
    jml = range(0, len(listHeroMag))
    smp = sample(jml, 3)
    for i in smp:
        j = 0
        hero = listHeroMag[int(i+1)]["hero"]
        type = listHeroMag[int(i+1)]["type"]
        bAtt = listHeroMag[int(i+1)]["bAtt"]
        hp = listHeroMag[int(i+1)]["hp"]
        defend = listHeroMag[int(i+1)]["def"]
        mAtt = listHeroMag[int(i+1)]["mAtt"]
        mag.append(Magic(hero, type, bAtt, hp,
                   items[int(i)], mAtt, defend))
        j += 1
    jml = range(0, len(listHerophy))
    smp_ = sample(jml, 3)
    for j in smp_:
        k = 0
        hero = listHerophy[int(j+1)]["hero"]
        type = listHerophy[int(j+1)]["type"]
        bAtt = listHerophy[int(j+1)]["bAtt"]
        hp = listHerophy[int(j+1)]["hp"]
        defend = listHerophy[int(j+1)]["def"]
        pAtt = listHerophy[int(j+1)]["pAtt"]
        phy.append(Physical(hero, type, bAtt, hp,
                   items[int(j)], pAtt, defend))
        k += 1
        merge.append(hero)
    jml = range(0, 3)
    smp = sample(jml, 3)
    for i in smp:
        print("3 Magic vs 3 Physic")
        print(f'{mag[i].hero}\nVS\n{phy[i].hero}')
        hero_fight.append([mag[i], phy[i]])


def battle():
    print("Battle di mulai")
    roundall = 0
    round1 = 0
    roundx = 1
    round2 = 0
    roundy = 1
    round3 = 0
    roundz = 1
    listHeroPasif = ["Lunox", "Pharsa", "Saber", "Bennedeta", "Chou"]

    for i in range(2):
        damage1 = hero_fight[0][round1].bAtt + \
            hero_fight[0][round1].item.damage
        hero_fight[0][roundx].Defense -= damage1
        if hero_fight[0][roundx].Defense < 0:
            hero_fight[0][roundx].hp += hero_fight[0][roundx].Defense
            hero_fight[0][roundx].Defense -= hero_fight[0][roundx].Defense
            if hero_fight[0][roundx].hp < 0:
                hero_fight[0][roundx].hp -= hero_fight[0][roundx].hp
        print(
            f'{hero_fight[0][round1].hero} menyerang {hero_fight[0][roundx].hero} dengan basic attack + item {hero_fight[0][round1].item.nama} sebesar {damage1} {hero_fight[0][round1].type} defense {hero_fight[0][roundx].hero} menjadi {hero_fight[0][roundx].Defense} hp {hero_fight[0][roundx].hero} menjadi {hero_fight[0][roundx].hp}')
        if hero_fight[0][roundx].hp < 0:
            hero_fight[0][roundx].hp -= hero_fight[0][roundx].hp
            print(
                f'================= {hero_fight[0][round1].hero} WIN ======================')
            break
        round1 += 1
        roundx -= 1
    for i in range(2):
        damage2 = hero_fight[0][round2].heroatt + \
            dictHeroUlti[hero_fight[0][round2].hero].att
        hero_fight[0][roundy].Defense += dictHeroUlti[hero_fight[0]
                                                      [roundy].hero].sdefense
        roundall += 1
        if hero_fight[0][round2].hero in listHeroPasif:
            damage2 += 200
            hero_fight[0][roundy].Defense -= damage2
            if hero_fight[0][roundy].Defense < 0:
                hero_fight[0][roundy].hp += hero_fight[0][roundy].Defense
                hero_fight[0][roundy].Defense -= hero_fight[0][roundy].Defense
                if hero_fight[0][roundy].hp < 0:
                    hero_fight[0][roundy].hp -= hero_fight[0][roundy].hp
            print(
                f'{hero_fight[0][round2].hero} menyerang {hero_fight[0][roundy].hero} dengan {hero_fight[0][round2].type} attack + Ultimate {dictHeroUlti[hero_fight[0][round2].hero].skill} + pasif sebesar {damage2} {hero_fight[0][round2].type} defense {hero_fight[0][roundy].hero} menjadi {hero_fight[0][roundy].Defense} hp {hero_fight[0][roundy].hero} menjadi {hero_fight[0][roundy].hp}')\

        elif hero_fight[0][round2].hero not in listHeroPasif:
            hero_fight[0][roundy].Defense -= damage2
            if hero_fight[0][roundy].Defense < 0:
                hero_fight[0][roundy].hp += hero_fight[0][roundy].Defense
                hero_fight[0][roundy].Defense -= hero_fight[0][roundy].Defense
                if hero_fight[0][roundy].hp < 0:
                    hero_fight[0][roundy].hp -= hero_fight[0][roundy].hp
            print(
                f'{hero_fight[0][round2].hero} menyerang {hero_fight[0][roundy].hero} dengan {hero_fight[0][round2].type} attack + Ultimate {dictHeroUlti[hero_fight[0][round2].hero].skill} sebesar {damage2} {hero_fight[0][round2].type} defense {hero_fight[0][roundy].hero} menjadi {hero_fight[0][roundy].Defense} hp {hero_fight[0][roundy].hero} menjadi {hero_fight[0][roundy].hp}')\

            if hero_fight[0][1].hp == 0:
                print(
                    f'================= {hero_fight[0][1].hero} MENINGGAL DENGAN TENANG ======================')
                break
            elif hero_fight[0][0].hp == 0:
                print(
                    f'================= {hero_fight[0][0].hero} MENINGGAL DENGAN TENANG ======================')
                break
            roundall += 1
        round2 += 1
        roundy -= 1
    if roundall == 2 and hero_fight[0][1].hp == 0:
        print(
            f'================= {hero_fight[0][1].hero} MENINGGAL DENGAN TENANG ======================')
    elif roundall == 2 and hero_fight[0][0].hp == 0:
        print(
            f'================= {hero_fight[0][0].hero} MENINGGAL DENGAN TENANG ======================')

    if hero_fight[0][1].hp > hero_fight[0][0].hp:
        print(
            f'============== {hero_fight[0][1].hero} WIN ==============')
    else:
        print(
            f'============== {hero_fight[0][0].hero} WIN ==============')


def battle2():
    roundall = 0
    round1 = 0
    roundz = 1
    roundx = 1
    roundx2 = 1

    round2 = 0
    roundw = 1
    roundy = 1
    roundy2 = 1
    listHeroPasif = ["Lunox", "Pharsa", "Saber", "Bennedeta", "Chou"]

    for i in range(2):
        damage1 = hero_fight[roundz][round1].bAtt + \
            hero_fight[roundz][round1].item.damage
        hero_fight[roundx2][roundx].Defense -= damage1
        if hero_fight[roundx2][roundx].Defense < 0:
            hero_fight[roundx2][roundx].hp += hero_fight[roundx2][roundx].Defense
            hero_fight[roundx2][roundx].Defense -= hero_fight[roundx2][roundx].Defense
            if hero_fight[roundx2][roundx].hp < 0:
                hero_fight[roundx2][roundx].hp -= hero_fight[roundx2][roundx].hp
        print(
            f'{hero_fight[roundz][round1].hero} menyerang {hero_fight[roundx2][roundx].hero} dengan basic attack + item {hero_fight[roundz][round1].item.nama} sebesar {damage1} {hero_fight[roundz][round1].type} defense {hero_fight[roundx2][roundx].hero} menjadi {hero_fight[roundx2][roundx].Defense} hp {hero_fight[roundx2][roundx].hero} menjadi {hero_fight[roundx2][roundx].hp}')
        if hero_fight[roundx2][roundx].hp < 0:
            hero_fight[roundx2][roundx].hp -= hero_fight[roundx2][roundx].hp
            print(
                f'================= {hero_fight[roundz][round1].hero} WIN ======================')
            break

        round1 += 1
        roundx -= 1

    for i in range(2):
        damage2 = hero_fight[roundw][round2].heroatt + \
            dictHeroUlti[hero_fight[roundw][round2].hero].att
        hero_fight[roundy2][roundy].Defense += dictHeroUlti[hero_fight[roundy2]
                                                            [roundy].hero].sdefense
        roundall += 1
        if hero_fight[roundw][round2].hero in listHeroPasif:
            damage2 += 200
            hero_fight[roundy2][roundy].Defense -= damage2
            if hero_fight[roundy2][roundy].Defense < 0:
                hero_fight[roundy2][roundy].hp += hero_fight[roundy2][roundy].Defense
                hero_fight[roundy2][roundy].Defense -= hero_fight[roundy2][roundy].Defense
                if hero_fight[roundy2][roundy].hp < 0:
                    hero_fight[roundy2][roundy].hp -= hero_fight[roundy2][roundy].hp
            print(
                f'{hero_fight[roundw][round2].hero} menyerang {hero_fight[roundy2][roundy].hero} dengan {hero_fight[roundw][round2].type} attack + Ultimate {dictHeroUlti[hero_fight[roundw][round2].hero].skill} + pasif sebesar {damage2} {hero_fight[roundw][round2].type} defense {hero_fight[roundy2][roundy].hero} menjadi {hero_fight[roundy2][roundy].Defense} hp {hero_fight[roundy2][roundy].hero} menjadi {hero_fight[roundy2][roundy].hp}')\

        elif hero_fight[roundw][round2].hero not in listHeroPasif:
            hero_fight[roundy2][roundy].Defense -= damage2
            if hero_fight[roundy2][roundy].Defense < 0:
                hero_fight[roundy2][roundy].hp += hero_fight[roundy2][roundy].Defense
                hero_fight[roundy2][roundy].Defense -= hero_fight[roundy2][roundy].Defense
                if hero_fight[roundy2][roundy].hp < 0:
                    hero_fight[roundy2][roundy].hp -= hero_fight[roundy2][roundy].hp
            print(
                f'{hero_fight[roundw][round2].hero} menyerang {hero_fight[roundy2][roundy].hero} dengan {hero_fight[roundw][round2].type} attack + Ultimate {dictHeroUlti[hero_fight[roundw][round2].hero].skill} sebesar {damage2} {hero_fight[roundw][round2].type} defense {hero_fight[roundy2][roundy].hero} menjadi {hero_fight[roundy2][roundy].Defense} hp {hero_fight[roundy2][roundy].hero} menjadi {hero_fight[roundy2][roundy].hp}')\

            if hero_fight[1][1].hp == 0:
                print(
                    f'================= {hero_fight[1][1].hero} MENINGGAL DENGAN TENANG ======================')
                break
            elif hero_fight[1][0].hp == 0:
                print(
                    f'================= {hero_fight[1][0].hero} MENINGGAL DENGAN TENANG ======================')
                break
            roundall += 1
        round2 += 1
        roundy -= 1
    if roundall == 2 and hero_fight[1][1].hp == 0:
        print(
            f'================= {hero_fight[1][1].hero} MENINGGAL DENGAN TENANG ======================')
    elif roundall == 2 and hero_fight[1][0].hp == 0:
        print(
            f'================= {hero_fight[1][0].hero} MENINGGAL DENGAN TENANG ======================')

    if hero_fight[1][1].hp > hero_fight[1][0].hp:
        print(
            f'============== {hero_fight[1][1].hero} WIN ==============')
    else:
        print(
            f'============== {hero_fight[1][0].hero} WIN ==============')


def battle3():
    roundall = 0

    round1 = 0
    roundz = 2
    roundx = 1
    roundx2 = 2

    round2 = 0
    roundw = 2
    roundy = 1
    roundy2 = 2
    listHeroPasif = ["Lunox", "Pharsa", "Saber", "Bennedeta", "Chou"]

    for i in range(2):
        damage1 = hero_fight[roundz][round1].bAtt + \
            hero_fight[roundz][round1].item.damage
        hero_fight[roundx2][roundx].Defense -= damage1
        if hero_fight[roundx2][roundx].Defense < 0:
            hero_fight[roundx2][roundx].hp += hero_fight[roundx2][roundx].Defense
            hero_fight[roundx2][roundx].Defense -= hero_fight[roundx2][roundx].Defense
            if hero_fight[roundx2][roundx].hp < 0:
                hero_fight[roundx2][roundx].hp -= hero_fight[roundx2][roundx].hp
        print(
            f'{hero_fight[roundz][round1].hero} menyerang {hero_fight[roundx2][roundx].hero} dengan basic attack + item {hero_fight[roundz][round1].item.nama} sebesar {damage1} {hero_fight[roundz][round1].type} defense {hero_fight[roundx2][roundx].hero} menjadi {hero_fight[roundx2][roundx].Defense} hp {hero_fight[roundx2][roundx].hero} menjadi {hero_fight[roundx2][roundx].hp}')
        if hero_fight[roundx2][roundx].hp < 0:
            hero_fight[roundx2][roundx].hp -= hero_fight[roundx2][roundx].hp
            print(
                f'================= {hero_fight[roundz][round1].hero} WIN ======================')
            break

        round1 += 1
        roundx -= 1

    for i in range(2):
        damage2 = hero_fight[roundw][round2].heroatt + \
            dictHeroUlti[hero_fight[roundw][round2].hero].att
        hero_fight[roundy2][roundy].Defense += dictHeroUlti[hero_fight[roundy2]
                                                            [roundy].hero].sdefense
        roundall += 1
        if hero_fight[roundw][round2].hero in listHeroPasif:
            damage2 += 200
            hero_fight[roundy2][roundy].Defense -= damage2
            if hero_fight[roundy2][roundy].Defense < 0:
                hero_fight[roundy2][roundy].hp += hero_fight[roundy2][roundy].Defense
                hero_fight[roundy2][roundy].Defense -= hero_fight[roundy2][roundy].Defense
                if hero_fight[roundy2][roundy].hp < 0:
                    hero_fight[roundy2][roundy].hp -= hero_fight[roundy2][roundy].hp
            print(
                f'{hero_fight[roundw][round2].hero} menyerang {hero_fight[roundy2][roundy].hero} dengan {hero_fight[roundw][round2].type} attack + Ultimate {dictHeroUlti[hero_fight[roundw][round2].hero].skill} + pasif sebesar {damage2} {hero_fight[roundw][round2].type} defense {hero_fight[roundy2][roundy].hero} menjadi {hero_fight[roundy2][roundy].Defense} hp {hero_fight[roundy2][roundy].hero} menjadi {hero_fight[roundy2][roundy].hp}')\

        elif hero_fight[roundw][round2].hero not in listHeroPasif:
            hero_fight[roundy2][roundy].Defense -= damage2
            if hero_fight[roundy2][roundy].Defense < 0:
                hero_fight[roundy2][roundy].hp += hero_fight[roundy2][roundy].Defense
                hero_fight[roundy2][roundy].Defense -= hero_fight[roundy2][roundy].Defense
                if hero_fight[roundy2][roundy].hp < 0:
                    hero_fight[roundy2][roundy].hp -= hero_fight[roundy2][roundy].hp
            print(
                f'{hero_fight[roundw][round2].hero} menyerang {hero_fight[roundy2][roundy].hero} dengan {hero_fight[roundw][round2].type} attack + Ultimate {dictHeroUlti[hero_fight[roundw][round2].hero].skill} sebesar {damage2} {hero_fight[roundw][round2].type} defense {hero_fight[roundy2][roundy].hero} menjadi {hero_fight[roundy2][roundy].Defense} hp {hero_fight[roundy2][roundy].hero} menjadi {hero_fight[roundy2][roundy].hp}')\

            if hero_fight[2][1].hp == 0:
                print(
                    f'================= {hero_fight[2][1].hero} MENINGGAL DENGAN TENANG ======================')
                break
            elif hero_fight[2][0].hp == 0:
                print(
                    f'================= {hero_fight[2][0].hero} MENINGGAL DENGAN TENANG ======================')
                break
            roundall += 1
        round2 += 1
        roundy -= 1
    if roundall == 2 and hero_fight[2][1].hp == 0:
        print(
            f'================= {hero_fight[2][1].hero} MENINGGAL DENGAN TENANG ======================')
    elif roundall == 2 and hero_fight[2][0].hp == 0:
        print(
            f'================= {hero_fight[2][0].hero} MENINGGAL DENGAN TENANG ======================')

    if hero_fight[2][1].hp > hero_fight[2][0].hp:
        print(
            f'============== {hero_fight[2][1].hero} WIN ==============')
    else:
        print(
            f'============== {hero_fight[2][0].hero} WIN ==============')


buat_skill()

while True:
    print(f"SELAMAT DATANG DI MAGIC VS PHYSIC\nPilihan:\n 1. Lihat daftar hero Magic\n 2. Lihat daftar hero Physic\n 3. Lihat skill hero Magic\n 4. Lihat skill hero Physic\n 5. Pilih hero & buat item\n 6. Beli item\n 7. Battle\n 8. Keluar")
    i = input("Masukkan pilihan: ")
    if i == "1":
        daftar_heromagic(listHeroMag)
    elif i == "2":
        daftar_herophysic(listHerophy)
    elif i == "3":
        daftar_ulti(listHeroMag)
    elif i == "4":
        daftar_ulti(listHerophy)
    elif i == "5":
        buat_item()
    elif i == "6":
        for i in mag:
            print(
                f'{i.hero} membeli item {i.item.nama}')
        for i in phy:
            print(
                f'{i.hero} membeli item {i.item.nama}')
    elif i == "7":

        battle()
        battle2()
        battle3()
    elif i == "8":
        break

# Masih ada kekurangan di bagian random item dan "press any key to continue" tidak di sematkan.
# Mohon maaf atas mepet waktu penguploadan tugas
