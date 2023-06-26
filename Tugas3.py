# FA'IQ ALI SUTIONO
# 1152100040

Role_Akun = {
    "Jungler01": [],
    "Roamer01": [],
    "Offlaner01": [],
    "Midlaner01": []
}

AllHero = []
RoleDict = {

}
SubRoleDefault = ["Jungler01", "Offlaner01", "Roamer01", "Midlaner01"]

RoleDefault = ["Jungler", "Offlaner", "Roamer", "Midlaner"]

Jungler = ["Physical", "Magic"]
Offlaner = ["Physical", "Support"]
Midlaner = ["Magic", "Support"]
Roamer = ["Physical", "Magic", "Support"]


class Hero():
    def __init__(self, role, nama, dm, bp, tiket, tipe, power):
        self.__role = role
        self.__nama = nama
        self.__dm = dm
        self.__bp = bp
        self.__tiket = tiket
        self.__tipe = tipe
        self.__power = power

    @property
    def info_hero(self):
        if self.__tipe == "Physical":
            return "Hero Physical \nNama : {} \nDm: {} \nBP : {} \nTiket : {} \nPhysical Power : {}".format(self.__nama, self.__dm, self.__bp, self.__tiket, self.__power) + "\n"
        elif self.__tipe == "Magic":
            return "Hero Magic \nNama : {} \nDm: {} \nBP : {} \nTiket : {} \nMagic Power : {}".format(self.__nama, self.__dm, self.__bp, self.__tiket, self.__power) + "\n"
        elif self.__tipe == "Support":
            return "Hero Support \nNama : {} \nDm: {} \nBP : {} \nTiket : {} \nHP Healing : {}".format(self.__nama, self.__dm, self.__bp, self.__tiket, self.__power) + "\n"
        else:
            print("Error")

    def global_info(self):
        self.info_hero()


class Role():
    def __init__(self):
        pass

    def add_hero(self, nama, namarole, tipe):
        self.nama = nama
        self.role = namarole
        self.tipe = tipe

        if self.role in SubRoleDefault:
            if self.tipe == "Physical" or "Magic":
                Role_Akun[self.role].append(self.nama)
                print("berhasil menambahkan hero" + "\n")
                AllHero.append(self.nama)
            elif self.tipe == "Physical" or "Support":
                Role_Akun[self.role].append(self.nama)
                print("berhasil menambahkan hero" + "\n")
                AllHero.append(self.nama)
            elif self.tipe == "Magic" or "Support":
                Role_Akun[self.role].append(self.nama)
                print("berhasil menambahkan hero" + "\n")
                AllHero.append(self.nama)
            elif self.tipe == "Magic" or "Support" or "Physical":
                Role_Akun[self.role].append(self.nama)
                print("berhasil menambahkan hero" + "\n")
                AllHero.append(self.nama)
            else:
                print("Gagal menambahkan hero" + "\n")
        else:
            print("Gagal menambahkan hero" + "\n")

    def list_hero(self):
        if len(AllHero) == 0:
            print("Belum ada hero di akun MLBB" + "\n")
        else:
            for key, value in Role_Akun.items():
                print(key, ":")
                for i in value:
                    print("\t" + i)

    def search_hero(self, nama):
        if nama in AllHero:
            print(f"Hero ditemukan")
        else:
            print("Hero tidak ditemukan")


class Akun():
    def __init__(self):
        pass

    def add_role(self, namarole, jenisrole):
        if jenisrole in RoleDefault:
            self.namarole = namarole
            self.jenisrole = jenisrole
            Role_Akun[self.namarole] = []
            SubRoleDefault.append(self.namarole)
            print(
                f'Role baru berhasil ditambahkan\nNama: {self.namarole}\nJenis: {self.jenisrole}' + "\n")
        else:
            print("Gagal menambahkan role" + "\n")


AkunFunc = Akun()
RoleFunc = Role()
SpecialChar = ["!", "@", "#", "$", "%", "^", "&",
               "*", "(", ")", "_", "-", "=", "+", "?", "/"]
while True:
    print(f'Selamat datang di Mobile Legends Bang Bang\nSilahkan masukkan perintah')
    command = input("Perintah anda : ")
    if command == "EXIT":
        break
    else:
        split = command.split()
        if split[0] == "ADD" and split[1] == "ROLE":
            if split[2] in RoleDefault:
                print(f"Role dengan nama {split[2]} sudah ada di akun MLBB")
            else:
                AkunFunc.add_role(split[2], split[3])
                split[2] = split[3]
        elif split[0] == "ADD" and split[1] == "HERO":
            if split[3] in AllHero:
                print(
                    f"Hero dengan nama {split[3]} sudah ada di dalam akun MLBB" + "\n")
            else:
                RoleFunc.add_hero(split[3], split[2], split[7])
                if split[3] in AllHero:
                    Hero_ = Hero(split[2], split[3], int(split[4]),
                                 int(split[5]), int(split[6]), split[7], int(split[8]))
                    print(Hero_.info_hero)
                else:
                    print("Gagal menambahkan hero")
        elif split[0] == "LIST":
            RoleFunc.list_hero()
        elif split[0] == "SEARCH" and split[1] == "HERO":
            RoleFunc.search_hero(split[2])
