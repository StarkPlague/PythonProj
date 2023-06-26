class Hero:
    def __init__(self, n, a):
        self.nama = n
        self.att = a


hero = []
nmHero = input("Masukkan nama Hero ke : ")
fmHero = nmHero.split("%")
hero.append(Hero(fmHero[0], fmHero[1]))
obj = Hero()

print(vars(obj))
