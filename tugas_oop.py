class Heroku:
    jumlah = 0

    def __init__(self, name, power, health):
        self.name = name
        self.power = power
        self.health = health
        Heroku.jumlah += 1

    # void function, method tanpa return && arguments
    def get_name(self):
        print(self.name)

    # method dengan arguments
    def push_power(self, power):
        self.power += power

    # method dengan return
    def get_power(self):
        return self.power


class Lord(Heroku):
    hp = 5000

    def attacked(self, health, power):
        self.health = health
        self.power = power
        self.health = int(input())
        hp = self.health - self.power
        return hp
    print(hp)


hero1 = Heroku("miya", 300, 200)
hero2 = Heroku("alucard", 200, 300)

# Returns
hero1.get_name()        # get name from object hero1
hero1.push_power(225)   # push power to hero1
print(hero1.power)
print(hero1.get_power())  # get power from object hero1
