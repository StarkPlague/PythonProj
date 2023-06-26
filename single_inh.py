class Ortu:
    def ibu(self):
        print("ini adalah method ibu dari kelas Ortu")


class Anak(Ortu):
    def anak1(self):
        print("ini adalah method anak 1 anak dari Ortu")


obj = Anak()
obj.ibu()
obj.anak1()
