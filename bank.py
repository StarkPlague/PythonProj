


class Tarikan():
    __saldo = 0
    
    def jumlah(self):
        self.jumlah

    def _Tarik(self, tarik):
        return self.__saldo - tarik
        print("berhasil menarik uang sebesar: ", self.jumlah)
        
    def _Setor(self, setor):
        return self.__saldo + setor

class Nasabah(Tarikan):
    pass


ambil = int(input())
ambil2 = Tarikan(ambil)
ambil2.Tarik()
