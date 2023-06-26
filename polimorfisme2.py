class Uang:  # OVERLOADING ()
    def __init__(self, nominal, logo):
        self.nominal = nominal
        self.logo = logo
        print("Uang : {}, logo: {}". format(self.nominal, self.logo))

    def info(self):
        print("Uang dengan nominal: ", self.nominal)


class Kertas(Uang):
    def __init__(self, bahan):
        # Memanggil konstruktor ini dengan super()
        super().__init__(1000, "Pattimura")
        self.bahan = bahan

    def info(self, noSeri):
        print("Uang dengan nominal: ", self.nominal)
        print("Uang dengan bahan: ", self.bahan)
        print("Uang dengan No Seri: ", noSeri)


uang1 = Kertas("Kapas")
uang1.info(12345)
