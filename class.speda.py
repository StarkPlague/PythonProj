
class sepeda:
    gear = 0

    def getGear(self):
        return self.gear

    def setGear(self, tambahGear):
        self.gear = self.gear+tambahGear


class SepedaGunung(sepeda):
    def setGear(self, tambahGear):
        super().setGear(tambahGear)
        self.gear = 2*super().getGear()


sepeda1 = SepedaGunung()
sepeda1.setGear(2)

print(sepeda1.getGear())

sepeda1.setGear(3)
print(sepeda1.getGear())
