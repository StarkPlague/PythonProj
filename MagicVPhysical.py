#
#   Raihan Desfitra 1152100019 
#   PBO Tugas 2
#

#import
import os
import random

#Fungsi untuk menghapus dan pause karena sering dipakai
#Menggunakan fungsi lambda untuk memendekan karena akan sering dipakai
clear = lambda: os.system("cls" if os.name in ("nt","dos") else "clear") #membersihkan console
pause = lambda: os.system("pause") #mehentikan console sementara
crossline = lambda: print("⎯"*50) #garis potong agar terlihat indah
crossline2x = lambda: print("⎯"*75) #garis potong agar terlihat indah

#data hero, dapat diganti kapan saja disini
data_hero = [
    {
        "nama":"Gord",
        "basicAttack":100,
        "hp":800,
        "attackPower":100, #Atau Magic/Physical attack
        "defensePower":100, #Atau Magic/Physical defense
        "tipe":"Magic", #"Magic" atau "Physical" untuk mengkategorikan
        "skill": {
            "nama":"Mystic Gush",
            "attackPower":10,
            "defensePower":80
        }
    },{
        "nama":"Harley",
        "basicAttack":100,
        "hp":700,
        "attackPower":200, #Atau Magic/Physical attack
        "defensePower":200, #Atau Magic/Physical defense
        "tipe":"Magic", #"Magic" atau "Physical" untuk mengkategorikan
        "skill": {
            "nama":"Deadly Magic",
            "attackPower":20,
            "defensePower":70
        }
    },{
        "nama":"Lunox",
        "basicAttack":100,
        "hp":600,
        "attackPower":300, #Atau Magic/Physical attack
        "defensePower":300, #Atau Magic/Physical defense
        "tipe":"Magic", #"Magic" atau "Physical" untuk mengkategorikan
        "skill": {
            "nama":"Order & Chaos",
            "attackPower":30,
            "defensePower":60
        },
        "pasif":{
            "attackPower":200,
            "defensePower":0
        }
    },{
        "nama":"Guinevere",
        "basicAttack":100,
        "hp":500,
        "attackPower":400, #Atau Magic/Physical attack
        "defensePower":400, #Atau Magic/Physical defense
        "tipe":"Magic", #"Magic" atau "Physical" untuk mengkategorikan
        "skill":{
            "nama":"Violet Requiem",
            "attackPower":40,
            "defensePower":50
        }
    },{
        "nama":"Harith",
        "basicAttack":100,
        "hp":400,
        "attackPower":500, #Atau Magic/Physical attack
        "defensePower":500, #Atau Magic/Physical defense
        "tipe":"Magic", #"Magic" atau "Physical" untuk mengkategorikan
        "skill":{
            "nama":"Zaman Force",
            "attackPower":50,
            "defensePower":40
        }
    },{
        "nama":"Valir",
        "basicAttack":100,
        "hp":300,
        "attackPower":600, #Atau Magic/Physical attack
        "defensePower":600, #Atau Magic/Physical defense
        "tipe":"Magic", #"Magic" atau "Physical" untuk mengkategorikan
        "skill":{
            "nama":"Vangeane Flame",
            "attackPower":60,
            "defensePower":30
        }
    },{
        "nama":"Pharsa",
        "basicAttack":100,
        "hp":200,
        "attackPower":700, #Atau Magic/Physical attack
        "defensePower":700, #Atau Magic/Physical defense
        "tipe":"Magic", #"Magic" atau "Physical" untuk mengkategorikan
        "skill":{
            "nama":"Featherd Air Strike",
            "attackPower":70,
            "defensePower":20
        },
        "pasif":{
            "attackPower":200,
            "defensePower":0
        }
    },{
        "nama":"Cecillion",
        "basicAttack":100,
        "hp":100,
        "attackPower":800, #Atau Magic/Physical attack
        "defensePower":800, #Atau Magic/Physical defense
        "tipe":"Magic", #"Magic" atau "Physical" untuk mengkategorikan
        "skill":{
            "nama":"Bats Feast",
            "attackPower":80,
            "defensePower":10
        }
    },{
        "nama":"Saber",
        "basicAttack":100,
        "hp":400,
        "attackPower":400, #Atau Magic/Physical attack
        "defensePower":400, #Atau Magic/Physical defense
        "tipe":"Physical", #"Magic" atau "Physical" untuk mengkategorikan
        "skill":{
            "nama":"Tripple Sweep",
            "attackPower":20,
            "defensePower":10
        },
        "pasif":{
            "attackPower":200,
            "defensePower":0
        }
    },{
        "nama":"Benedetta",
        "basicAttack":100,
        "hp":300,
        "attackPower":500, #Atau Magic/Physical attack
        "defensePower":500, #Atau Magic/Physical defense
        "tipe":"Physical", #"Magic" atau "Physical" untuk mengkategorikan
        "skill":{
            "nama":"Alecto: Final Blow",
            "attackPower":30,
            "defensePower":15
        },
        "pasif":{
            "attackPower":200,
            "defensePower":0
        }
    },{
        "nama":"Chou",
        "basicAttack":100,
        "hp":500,
        "attackPower":300, #Atau Magic/Physical attack
        "defensePower":300, #Atau Magic/Physical defense
        "tipe":"Physical", #"Magic" atau "Physical" untuk mengkategorikan
        "skill":{
            "nama":"The way of Dragon",
            "attackPower":40,
            "defensePower":20
        },
        "pasif":{
            "attackPower":200,
            "defensePower":0
        }
    }
]

#variable global untuk warning atau error
warn_and_info_message = ""

#variable data hero
Heroes = {"Physical":[],"Magic":[]} #Data hero akan dijadikan kelas dan disimpan objeknya disini
Enemy = {"Magic":[],"Physical":[]} #Saat pemilihan musuh akan disimpan disini
Item = [] #Saat membuat item, akan disimpan disini

#Kelas

#kelas hero
class Hero:
    def __init__(self, nama, bAttack, Hp, skill):
        self.nama = nama
        self.bAttack =int(bAttack)
        self.hp = Hp
        self.skill = Skills(skill["nama"],skill["attackPower"],skill["defensePower"])
        self.item = []
    
    def basicAttack(self): #untuk menyatukan damage basic attack dengan item yang digunakan
        return self.bAttack + self.item.power

#kelas magic hero
class MagicHero(Hero):
    def __init__(self, nama, bAttack, Hp, skill, Power, Defense):
        super().__init__(nama, bAttack, Hp, skill)
        self.power = int(Power)
        self.defense = int(Defense)

#kelas physical hero
class PhysicalHero(Hero):
    def __init__(self, nama, bAttack, Hp, skill, Power, Defense):
        super().__init__(nama, bAttack, Hp, skill)
        self.power = int(Power)
        self.defense = int(Defense)

#kelas item
class Items:
    def __init__(self, nama, Power):
        self.nama = nama
        self.power = int(Power)

#kelas skill
class Skills:
    def __init__(self, Nama, Power, Defense):
        self.nama = Nama
        self.power = Power
        self.defense = Defense

#Fungsi

#Pembuatan hero dari data
for index,x in enumerate(data_hero):
    if x["tipe"].lower() == "physical": #Untuk mengetahui apakah hero physical atau magic
        #Buat kelas dengan data hero
        hero = PhysicalHero(x["nama"],x["basicAttack"],x["hp"],x["skill"],x["attackPower"],x["defensePower"])
        #jika memiliki pasif, tambahkan (digunakan jika data diubah)
        if "pasif" in x:
            hero.pasif = x["pasif"]
        #masukan kedalam dictionary untuk disimpan dan refensi saat ingin digunakan
        Heroes["Physical"].append(hero)
    elif x["tipe"].lower() == "magic":#Untuk mengetahui apakah hero physical atau magic
        #buat kelas dengan data hero
        hero = MagicHero(x["nama"],x["basicAttack"],x["hp"],x["skill"],x["attackPower"],x["defensePower"])
        #jika memiliki pasif, tambahkan (digunakan jika data diubah)
        if "pasif" in x:
            hero.pasif = x["pasif"]
        #masukan kedalam dictionary untuk disimpan dan refensi saat ingin digunakan
        Heroes["Magic"].append(hero)
        

#Daftar hero magic
def MagicHeroList():
    crossline()
    #dapat dihilangkan spasinya karena hanya untuk mengindahkan
    print("Magic hero".center(50))

    for x in Heroes["Magic"]:
        print("".join(x.nama).center(50))
    crossline()
    pause()

#Daftar hero physical
def PhysicalHeroList():
    crossline()
    #dapat dihilangkan spasinya karena hanya untuk mengindahkan
    print("Physical Hero".center(50))
    for x in Heroes["Physical"]:
        print("".join(x.nama).center(50))
    crossline()
    pause()

#Daftar skill magic
def MagicSkillList():
    crossline()
    #dapat dihilangkan spasinya karena hanya untuk mengindahkan
    print("Magic Hero Skills".center(50))

    for x in Heroes["Magic"]:
        msg_skillset = x.nama + " memiliki skill " + x.skill.nama
        print(msg_skillset.center(50))
        if hasattr(x, "pasif"): #jika memiliki pasif, print juga
            msg_pasifset = x.nama + " memiliki skill Pasif"
            print(msg_pasifset.center(50))
    crossline()
    pause()

#Daftar skill physical
def PhysicalSkillList():
    crossline()
    #dapat dihilangkan spasinya karena hanya untuk mengindahkan
    print("Physical Hero Skills".center(50))

    for x in Heroes["Physical"]:
        msg_skillset = x.nama + " memiliki skill " + x.skill.nama
        print(msg_skillset.center(50))
        if hasattr(x, "pasif"): #jika memiliki pasif, print juga
            msg_pasifset = x.nama + " memiliki skill Pasif"
            print(msg_pasifset.center(50))
    crossline()
    pause()

#Pemilihan hero dan Pembuatan item
def HeroChoosing():
    #mengambil 3 random hero dari magic, dan memutar-mutar hero physical untuk menjadi lawan
    Mage_enemy = random.sample(Heroes["Magic"],3)
    Physical_enemy = Heroes["Physical"]
    random.shuffle(Physical_enemy)
    #masukan kedalam Enemy untuk referensi dan dapat diubah tanpa merusak data awal
    for i in Mage_enemy:
        Enemy["Magic"].append(i)
    for i in Physical_enemy:
        Enemy["Physical"].append(i)
    
    crossline()
    spaceLeft = 0
    #untun mengindahkan
    for index in range(3):
        if spaceLeft < len(Enemy["Magic"][index].nama):
            spaceLeft = len(Enemy["Magic"][index].nama) + 3
        if spaceLeft < len(Enemy["Physical"][index].nama):
            spaceLeft = len(Enemy["Physical"][index].nama) + 3

    output_text = ["|","|","|"] #text yang akan keluar, karena dibuat kesamping, maka disimpan dulu sebelum di print

    for index in range(3): 
        # "NamaMagic hero |" dan ditambah ke string sebelumnya di output
        output_text[0] = output_text[0] + Enemy["Magic"][index].nama.center(spaceLeft) + "|"
        # "NamaPhysical hero |" dan ditambah ke string sebelumnya di output
        output_text[2] = output_text[2] + Enemy["Physical"][index].nama.center(spaceLeft) + "|"
        #karena nama terpanjang selalu ganjil, maka digunakain ini
        #Dapat merusak hasil secara output jika digunakan untuk genap juga 
        output_text[1] = output_text[1] + "V S".center(spaceLeft) + "|"

    #hanya untuk mengindahkan
    print("Magic VS Physical".center(50))
    #Print semuanya sesuai rotasi [0] = magic hero [1] = "V S" [2] = Physical hero
    print("".join(output_text[0]).center(50))
    print("".join(output_text[1]).center(50))
    print("".join(output_text[2]).center(50))
    crossline()
    pause()

#Pembelian item setelah dibuat
def ItemCreation():
    global warn_and_info_message
    if not Enemy["Magic"]: #jika user tidak menentukan hero yang akan bertarung
        warn_and_info_message = "Pilih menu nomor 5 untuk memilih hero yang akan bertarung"
        return
    crossline()
    print("Membuat item hingga berhenti")
    while True:
        print("Item ke-" + str(len(Item) + 1))
        print("Masukan Atribut item (Nama item#Damage)/berhenti")
        if warn_and_info_message: print(warn_and_info_message); warn_and_info_message = ""
        pilihan_user = input("> ")
        #agar user memasukan hanya karakter yang diinginkan
        if all(x.isalpha() or x.isspace() or x.isnumeric() or x == "#" for x in pilihan_user):
            if pilihan_user.lower() in ("berhenti"):
                break
            elif not pilihan_user:
                warn_and_info_message = "Masukan sesuai format : Nama item#Damage"
                continue
            pilihan_user = pilihan_user.split("#")
            Item.append(Items(pilihan_user[0],pilihan_user[1]))
        else:
            warn_and_info_message = "Masukan sesuai format : Nama item#Damage"
    #jika user hanya memasukan kurang dari 6, maka akan reset, dan 
    #user harus memasukan ulang dari item pertama
    if len(Item) < 6:
        warn_and_info_message = "Tidak ada item untuk di beli"
        del Item[:]
        crossline()
        pause()
        return
    random.shuffle(Item) #item yang telah dibuat diputar putar
    number_order = [0,1,2] #posisi item yang akan diambil hero
    random.shuffle(number_order) #diputar putar agar lebih random
    for index,x in enumerate(Enemy["Magic"]): #masukan item ke objek hero
        x.item = Item[number_order[index]]
    random.shuffle(number_order) #diputar putar agar lebih random
    for index,x in enumerate(Enemy["Physical"]): #masukan item ke objek hero
        x.item = Item[number_order[index] + 3]
    Item.clear() #menghapus item jika masih ada
    clear()
    crossline()
    #dapat dihapus spasinya jika tidak dinginkan
    print("Hero Membeli Item".center(50))
    
    for x in Enemy["Magic"]:
        msg_itemset = x.nama + " membeli item " + x.item.nama
        print(msg_itemset.center(50))
    
    for x in Enemy["Physical"]:
        msg_itemset = x.nama + " membeli item " + x.item.nama
        print(msg_itemset.center(50))

    crossline()
    pause()

#Menyerang dengan basic attack
def battle_basicAttack(penyerang_tipe,pelindung_tipe,index):
    output = ["","",""]
    output[0] = "\033[1m{}\033[0m menyerang \033[1m{}\033[0m dengan basic attack + item \033[1m{}\033[0m".format(Enemy[penyerang_tipe][index].nama, Enemy[pelindung_tipe][index].nama, Enemy[penyerang_tipe][index].item.nama)
    damage_doned_to_shield = 0
    damage_doned_to_hp = 0
    if Enemy[pelindung_tipe][index].defense - Enemy[penyerang_tipe][index].basicAttack() < 0:
        damage_left = Enemy[penyerang_tipe][index].basicAttack() - Enemy[pelindung_tipe][index].defense
        damage_doned_to_shield = Enemy[pelindung_tipe][index].defense
        Enemy[pelindung_tipe][index].defense = 0
        Enemy[pelindung_tipe][index].hp -= damage_left
        damage_doned_to_hp = damage_left
    else:
        Enemy[pelindung_tipe][index].defense -= Enemy[penyerang_tipe][index].basicAttack()
        damage_doned_to_shield = Enemy[penyerang_tipe][index].basicAttack()
    output[1] = "{}  ❤️ {}  🛡️ {}  ⚔️ {}".format(Enemy[penyerang_tipe][index].nama, str(Enemy[penyerang_tipe][index].hp), str(Enemy[penyerang_tipe][index].defense), str(Enemy[penyerang_tipe][index].basicAttack()))
    if damage_doned_to_hp:
        output[2] = "{}  ❤️ {} -{}  🛡️ {} -{}".format(Enemy[pelindung_tipe][index].nama, str(Enemy[pelindung_tipe][index].hp), damage_doned_to_hp, str(Enemy[pelindung_tipe][index].defense), damage_doned_to_shield)
    else:
        output[2] = "{}  ❤️ {}  🛡️ {} -{}".format(Enemy[pelindung_tipe][index].nama, str(Enemy[pelindung_tipe][index].hp), str(Enemy[pelindung_tipe][index].defense), damage_doned_to_shield)
    print(output[0] + "\n" + output[1].center(75) + "\n" + output[2].center(75))

#menyerang dengan skill dan pasif
def battle_skillAttack(penyerang_tipe,pelindung_tipe,index):
    output = ["","",""]
    damage_doned_to_shield = 0
    damage_doned_to_hp = 0
    deffense = 0
    if hasattr(Enemy[penyerang_tipe][index],"pasif"):
        output[0] = "\033[1m{}\033[0m menyerang \033[1m{}\033[0m dengan magic attack + ultimate \033[1m{}\033[0m + pasif".format(Enemy[penyerang_tipe][index].nama, Enemy[pelindung_tipe][index].nama, Enemy[penyerang_tipe][index].skill.nama)
        dammage = Enemy[penyerang_tipe][index].power + Enemy[penyerang_tipe][index].skill.power + Enemy[penyerang_tipe][index].pasif["attackPower"]
        deffense = Enemy[penyerang_tipe][index].skill.defense
    else:
        output[0] = "\033[1m{}\033[0m menyerang \033[1m{}\033[0m dengan magic attack + ultimate \033[1m{}\033[0m".format(Enemy[penyerang_tipe][index].nama, Enemy[pelindung_tipe][index].nama, Enemy[penyerang_tipe][index].skill.nama)
        dammage = Enemy[penyerang_tipe][index].power + Enemy[penyerang_tipe][index].skill.power
    if Enemy[pelindung_tipe][index].defense - dammage < 0:
        damage_left = dammage - Enemy[pelindung_tipe][index].defense
        damage_doned_to_shield = Enemy[pelindung_tipe][index].defense
        Enemy[pelindung_tipe][index].defense = 0
        Enemy[pelindung_tipe][index].hp -= damage_left
        damage_doned_to_hp = damage_left
    else:
        Enemy[pelindung_tipe][index].defense -= dammage
        damage_doned_to_shield = dammage
    if Enemy[pelindung_tipe][index].hp < 0:
        Enemy[pelindung_tipe][index].hp = 0
    Enemy[penyerang_tipe][index].defense += deffense
    if deffense > 0:
        output[1] = "{}  ❤️ {} | 🛡️ {} +{}  ⚔️ {}".format(Enemy[penyerang_tipe][index].nama, str(Enemy[penyerang_tipe][index].hp), str(Enemy[penyerang_tipe][index].defense), deffense, str(dammage))
    else:
        output[1] = "{}  ❤️ {} | 🛡️ {}  ⚔️ {}".format(Enemy[penyerang_tipe][index].nama, str(Enemy[penyerang_tipe][index].hp), str(Enemy[penyerang_tipe][index].defense), str(dammage))
    if damage_doned_to_hp > 0 and damage_doned_to_shield > 0:
        output[2] = "{}  ❤️ {} -{}  🛡️ {} -{}".format(Enemy[pelindung_tipe][index].nama, str(Enemy[pelindung_tipe][index].hp), damage_doned_to_hp, str(Enemy[pelindung_tipe][index].defense), damage_doned_to_shield)
    elif damage_doned_to_hp > 0 and Enemy[pelindung_tipe][index].defense == 0:
        output[2] = "{}  ❤️ {} -{}  🛡️ {}".format(Enemy[pelindung_tipe][index].nama, str(Enemy[pelindung_tipe][index].hp), damage_doned_to_hp, str(Enemy[pelindung_tipe][index].defense))
    else:
        output[2] = "{}  ❤️ {}  🛡️ {} -{}".format(Enemy[pelindung_tipe][index].nama, str(Enemy[pelindung_tipe][index].hp), str(Enemy[pelindung_tipe][index].defense), damage_doned_to_shield)
    print(output[0] + "\n" + output[1].center(75) + "\n" + output[2].center(75))

#Memulai battle
def StartBattle():
    global warn_and_info_message
    if not Enemy["Magic"]: #jika melakukan battle saat tidak memilih hero
        warn_and_info_message = "Pilih menu nomor 5 untuk memilih hero yang akan bertarung"
        return
    #melakukan pertarungan
    for index in range(3):
        crossline2x()
        battle_basicAttack("Magic","Physical",index) #fungsi untuk print dan menghitung nyawa/defense 
        if Enemy["Physical"][index].hp <= 0 : #jika Physical hero hp habis
            print("\033[1m{}\033[0m Died".format(Enemy["Physical"][index].nama).center(75))
            crossline2x()
            print("\033[1m{}\033[0m WIN".format(Enemy["Magic"][index].nama).center(75))
            crossline2x()
            pause()
            continue
        battle_basicAttack("Physical","Magic",index)
        if Enemy["Magic"][index].hp <= 0: #jika magic hero hp habis
            print("\033[1m{}\033[0m Died".format(Enemy["Magic"][index].nama).center(75))
            crossline2x()
            print("\033[1m{}\033[0m WIN".format(Enemy["Physical"][index].nama).center(75))
            crossline2x()
            pause()
            continue
        battle_skillAttack("Magic","Physical",index)
        if Enemy["Physical"][index].hp <= 0 : #jika Physical hero hp habis
            print("\033[1m{}\033[0m Died".format(Enemy["Physical"][index].nama).center(75))
            crossline2x()
            print("\033[1m{}\033[0m WIN".format(Enemy["Magic"][index].nama).center(75))
            crossline2x()
            pause()
            continue
        battle_skillAttack("Physical","Magic",index)
        #saat battle selesai tetapi keduaya masih memiliki nyawa dan defense
        #jika defense Magic hero lebih besar, menang
        if Enemy["Magic"][index].hp > 0:
            if Enemy["Magic"][index].defense > 0:
                if Enemy["Magic"][index].defense > Enemy["Magic"][index].defense:
                    crossline2x()
                    print("\033[1m{}\033[0m WIN".format(Enemy["Magic"][index].nama).center(75))
                else:
                    crossline2x()
                    print("\033[1m{}\033[0m WIN".format(Enemy["Physical"][index].nama).center(75))
            elif Enemy["Magic"][index].hp > Enemy["Physical"][index].hp:
                crossline2x()
                print("\033[1m{}\033[0m WIN".format(Enemy["Magic"][index].nama).center(75))
            else:
                crossline2x()
                print("\033[1m{}\033[0m WIN".format(Enemy["Physical"][index].nama).center(75))
        else:
            print("\033[1m{}\033[0m Died".format(Enemy["Magic"][index].nama).center(75))
            crossline2x()
            print("\033[1m{}\033[0m WIN".format(Enemy["Physical"][index].nama).center(75))
        crossline2x()
        pause()
        continue
    #hapus data di Enemy untuk melakukan pemilihan ulang
    del Enemy["Magic"][:]
    del Enemy["Physical"][:]

#Variable untuk menu
#melakukan key run dengan fungsi agar tidak perlu memanggil lagi dengan banyak if
#di menu
MainMenu_Pilihan = [{
            "text":"Lihat daftar hero magic",
            "run":MagicHeroList
        },{
            "text":"Lihat daftar hero physical",
            "run":PhysicalHeroList
        },{
            "text":"Lihat skill hero magic",
            "run":MagicSkillList
        },{
            "text":"Lihat skill hero physical",
            "run":PhysicalSkillList
        },{
            "text":"Pemilihan hero",
            "run":HeroChoosing
        },{
            "text":"Membuat item",
            "run":ItemCreation
        },{
            "text":"Battle!",
            "run":StartBattle
    }]

#Menu
def MainMenu():
    
    global warn_and_info_message

    crossline()

    menu_Title_msg = "Selamat datang di MAGIC V PHYSICAL"

    print(menu_Title_msg.center(50))
    
    #print pilihan
    for index,x in enumerate(MainMenu_Pilihan):
        print(str(index + 1)," | ",x["text"] + ".")
    print(str(len(MainMenu_Pilihan) + 1), " | ", "Keluar")

    crossline()

    #jika terjadi kesalahan, print untuk mengetahui kesalahan
    if warn_and_info_message: print(warn_and_info_message); warn_and_info_message = ""

    pilihan_user = input("> ")
    if not pilihan_user: #jika pilihan user kosong, loop ulang
        return True

    if pilihan_user in (str(len(MainMenu_Pilihan) + 1)): #jika panjang menu (7) + 1 (8) adalah pilihan, keluar
        clear()
        print("Terima kasih")
        return False
    #Mempermudah pemanggilan fungsi tanpa memakan banyak kode
    elif pilihan_user.isnumeric() and int(pilihan_user) > 0 and int(pilihan_user) <= len(MainMenu_Pilihan):
        clear()
        MainMenu_Pilihan[int(pilihan_user) - 1]["run"]()
        return True
    else:
        warn_and_info_message = "Command tidak ditemukan"
        return True

#loop
while True:
    clear()
    if not MainMenu():
        pause()
        break
