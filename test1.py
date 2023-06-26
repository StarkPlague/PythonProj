baris = int(input("Masukan ukuran baris: "))
# print(baris)

# inisialisasi list 2 Dimensi
Map = []

for i in range(baris):
    isi_String = input()
    # print(isi_String)
    isi_list2D = isi_String.split()
    Map.append(isi_list2D)

# print(list2D)

# untuk mengetahui banyak nya kolom
kolom = len(Map[0])

# finalisasi masalah baris yang terbalik
posisiBaris = []
for i in range(baris):
    posisiBaris.append(i)

posisiBaris.reverse()
# print(posisiBaris)

# inisialisasi posisi barang
posisiRobot = []
posisiBarang = []
posisiLantaiRusak = []

# deteksi posisi robot, barang, dan lantai rusat
for i in range(baris):
    # kolom = len(list2D[i])
    for j in range(kolom):
        if Map[i][j] == "L":
            # informasi robot
            print("Logy ditemukan")
            print("Posisi robot ada pada koordinat", j, ",", posisiBaris[i])
            # simpan informasi
            posisiRobot.append(j)
            posisiRobot.append(posisiBaris[i])
            print(posisiRobot)

        elif Map[i][j] == "G":
            print("Pokemon ditemukan")
            print("Posisi barang ada pada koordinat", j, ",", posisiBaris[i])
            # simpan informasi
            posisiBarang.append(j)
            posisiBarang.append(posisiBaris[i])
            # print(posisiBarang)
            # jumlah barang
            jumlahBarang = len(posisiBarang)/2
            # update posisi barang menggunakan fungsi zip
            barang = zip(posisiBarang[::2], posisiBarang[1::2])
            # posisiBarang = [5,2,0,1]
            for a, b in barang:
                print(a, b)

        elif Map[i][j] == "#":
            print("Pohon ditemukan")
            print("Posisi Lantai rusak ada pada koordinat",
                  j, ",", posisiBaris[i])
            # simpan informasi
            posisiLantaiRusak.append(j)
            posisiLantaiRusak.append(posisiBaris[i])
            # print(posisiBarang)
            # jumlah barang
            jumlahLantaiRusak = len(posisiLantaiRusak)/2
            # update posisi barang menggunakan fungsi zip
            lantaiRusak = zip(posisiLantaiRusak[::2], posisiLantaiRusak[1::2])
            # posisiBarang = [5,2,0,1]
            for a, b in lantaiRusak:
                print(a, b)

# Tahapan berikutnya
# menggerakan robot
print("Robot siap di gerakkan")
newpos = []


def find(l, elem):
    for row, i in enumerate(l):
        try:
            column = i.index(elem)
        except ValueError:
            continue
        return row, column
    return -1
