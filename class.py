# class NamaKelas:
# pass  # dibuat jika masih bingung isi prototype


#kelas = NamaKelas
# Membuat prototype Hero
class Hero:
    pass


# Membuat objek dari kelas hero
hanabi = Hero()
print(hanabi)

# menambahkan atribut pada objek
hanabi.nama = "Hanabi"
print(hanabi.nama)

hanabi.role = "Marksman"
print(hanabi.role)

# Magic Function: Konstruktor


class Hiro:
    def __init__(self, namaHero, roleHero):
        self.nama = namaHero
        self.role = roleHero


inputnama = input()
inputrole = input()

hanabi = Hiro(inputnama, inputrole)
print(hanabi)
print(Hiro.nama)
#self: "apa yang melekat pada objek tersebut"
# contoh self.nama, self.role
