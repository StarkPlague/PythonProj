class Matakuliah:
    def __init__(self, n, u):
        self.nama = n
        self.umur = u

    def info(self):
        print('Nama: %s, Umur: %s' % (self.nama, self.umur))


class Dosen(Matakuliah):
    def __init__(self, n, u, m):
        Matakuliah.__init__(self, n, u)
        self.matkul = m

        print('menambahkan dosen: %s' % self.nama)

    def info(self):
        Matakuliah.info(self)
        print('Matkul: %s' % self.matkul)


class Mahasiswa(Matakuliah):
    def __init__(self, n, u, nil):
        Matakuliah.__init__(self, n, u)
        self.nilai = nil

        print('menambahkan mahasiswa: %s' % self.nama)

    def info(self):
        Matakuliah.info(self)
        print('Nilai: %s' % self.nilai)


dosen = Dosen('Naruto', 40, "Matematika")
mhs = Mahasiswa('Setiawan', 19, 69)


kampus = [dosen, mhs]

for i in kampus:
    i.info()
