'''
   Simulasi Robot dalam Gudang
   pembuat : Fa'iq Ali Sutiono
   NIM : 1152100040
   Prodi Informatika
   Nama Aplikasi : robotGudang v1.0
   '''

# Mengembangkan hasil diskusi dengan pak Soleh pada pertemuan sebelumnya

# kita harus tau banyak baris
baris = int(input("Masukan ukuran baris: "))
# print(baris)

# inisialisasi list 2 Dimensi
list2D = []

for i in range(baris):
    isi_String = input()
    # print(isi_String)
    isi_list2D = isi_String.split()
    list2D.append(isi_list2D)

# print(list2D)

# untuk mengetahui banyak nya kolom
kolom = len(list2D[0])

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
        if list2D[i][j] == "L":
            # informasi robot
            print("Robot ditemukan")
            print("Posisi robot ada pada koordinat", j, ",", posisiBaris[i])
            # simpan informasi
            posisiRobot.append(j)
            posisiRobot.append(posisiBaris[i])
            print(posisiRobot)

        elif list2D[i][j] == "1":
            print("Barang ditemukan")
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

        elif list2D[i][j] == "-1":
            print("Lantai rusak ditemukan")
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

# Line dibawah ini saya ilustrasikan index 0 sebagai x dan 1 sebagai y berdasarkan garis bilangan
# Code dan algoritma yang digunakan hampir sama disetiap line, jadi saya hanya harus copas dan mengubah persamaan koordinat nya
# Saya improvisasi agar setiap pergerakkan akan mengupdate map sehingga memungkinkan handling robot secara real-time
# Kekurangan nya adalah hanya bisa menggunakan input map pada line, tidak bisa menggunakan map file


def scan(dir):  # Membuat fungsi scan
    # menggunakan fungsi find yang telah di buat dengan objek pencarian "L"
    x = find(list2D, "L")
    newpos = list(x)
    if dir == "u":  # Jika perintah adalah "u"
        newpos[0] = newpos[0] - 1  # Maka titik x dikurangi 1 agar kearah atas
        if newpos[0] < 0:  # Kondisional jika x kurang dari 0 atau keluar map
            print("Tidak scan barang, mencapai batas map")
        elif list2D[newpos[0]][newpos[1]] == "1":  # Jika koordinat X, Y adalah 1
            print("ada barang di atas")
        elif list2D[newpos[0]][newpos[1]] == "-1":  # Jika koordinat X, y adalah -1
            print("ada lantai rusak")
        else:  # Jika kosong
            print("tidak ada apa apa")
    elif dir == "d":
        try:  # mencoba dan error handling
            newpos[0] = newpos[0] + 1
            if list2D[newpos[0]][newpos[1]] == "1":
                print("ada barang di bawah")
            elif list2D[newpos[0]][newpos[1]] == "-1":
                print("ada lantai rusak")
            else:
                print("tidak ada apa apa")
        except:  # Jika keluar map
            print("Tidak bisa scan, mencapai batas map")
    elif dir == "l":
        newpos[1] = newpos[1] - 1
        if newpos[0] < 0:
            print("Tidak scan barang, mencapai batas map")
        elif list2D[newpos[0]][newpos[1]] == "1":
            print("ada barang di kiri")
        elif list2D[newpos[0]][newpos[1]] == "-1":
            print("ada lantai rusak")
        else:
            print("tidak ada apa apa")
    elif dir == "r":
        try:
            newpos[1] = newpos[1] + 1
            if list2D[newpos[0]][newpos[1]] == "1":
                print("ada barang di kanan")
            elif list2D[newpos[0]][newpos[1]] == "-1":
                print("ada lantai rusak")
            else:
                print("tidak ada apa apa")
        except:
            print("Tidak bisa scan, mencapai batas map")
    else:
        print("perintah tidak dikenali")


barang_ = []  # Membuat list baru sebagai "Tas" untuk menyimpan barang, list berisi 1 atau kosong yang mewakili ada dan tidak nya barang


def pickup(dir):
    if dir == "u":
        x = find(list2D, "L")
        newpos = list(x)
        # X = X -1 (Persamaan koordinat X) dan Y tetap karena hanya bergerak pada garis X
        newpos[0] = newpos[0] - 1
        if newpos[0] < 0:
            print("Tidak mengambil barang, mencapai batas map")
        elif list2D[newpos[0]][newpos[1]] == "0":
            print("tidak ada barang")
        elif list2D[newpos[0]][newpos[1]] == "-1":
            print("Hanya ada lantai rusak")
        else:
            list2D[newpos[0]][newpos[1]] = "0"
            if len(barang_) == 0:
                barang_.append("1")
            else:
                list2D[newpos[0]][newpos[1]] = "1"
                print("Hanya memuat satu barang")
    elif dir == "d":
        x = find(list2D, "L")
        newpos = list(x)
        try:
            newpos[0] = newpos[0] + 1
            if list2D[newpos[0]][newpos[1]] == "0":
                print("tidak ada barang")
            elif list2D[newpos[0]][newpos[1]] == "-1":
                print("Hanya ada lantai rusak")
            else:
                list2D[newpos[0]][newpos[1]] = "0"
                if len(barang_) == 0:
                    barang_.append("1")
                else:
                    list2D[newpos[0]][newpos[1]] = "1"
                    print("Hanya memuat satu barang")
        except:
            print("Tidak bisa mengambil barang, mencapai batas map")
    elif dir == "r":
        x = find(list2D, "L")
        newpos = list(x)
        try:
            newpos[1] = newpos[1] + 1
            if list2D[newpos[0]][newpos[1]] == "0":
                print("tidak ada barang")
            elif list2D[newpos[0]][newpos[1]] == "-1":
                print("Hanya ada lantai rusak")
            else:
                list2D[newpos[0]][newpos[1]] = "0"
                if len(barang_) == 0:
                    barang_.append("1")
                else:
                    list2D[newpos[0]][newpos[1]] = "1"
                    print("Hanya memuat satu barang")
        except:
            print("Tidak bisa mengambil barang, mencapai batas map")
    elif dir == "l":
        x = find(list2D, "L")
        newpos = list(x)
        newpos[1] = newpos[1] - 1
        if newpos[1] < 0:
            print("Tidak bisa mengambil barang, mencapai batas map")
        elif list2D[newpos[0]][newpos[1]] == "0":
            print("tidak ada barang")
        elif list2D[newpos[0]][newpos[1]] == "-1":
            print("Hanya ada lantai rusak")
        else:
            list2D[newpos[0]][newpos[1]] = "0"
            if len(barang_) == 0:
                barang_.append("1")
            else:
                list2D[newpos[0]][newpos[1]] = "1"
                print("Hanya memuat satu barang")
    else:
        print("perintah tidak dikenali")
    print('\n'.join(map(' '.join, list2D)))


def drop(dir):
    if dir == "u":
        x = find(list2D, "L")
        newpos = list(x)
        newpos[0] = newpos[0] - 1
        if newpos[0] < 0:
            print("Tidak bisa menaruh barang, mencapai batas map")
        elif list2D[newpos[0]][newpos[1]] == "1":
            print("ada barang lain")
        elif list2D[newpos[0]][newpos[1]] == "-1":
            print("ada lantai rusak")
        else:
            if len(barang_) == 1:
                list2D[newpos[0]][newpos[1]] = "1"
                barang_.pop(0)
            elif len(barang_) == 0:
                print("Tidak ada barang bawaan")

    elif dir == "d":
        x = find(list2D, "L")
        newpos = list(x)
        try:
            newpos[0] = newpos[0] + 1
            if list2D[newpos[0]][newpos[1]] == "1":
                print("ada barang lain")
            elif list2D[newpos[0]][newpos[1]] == "-1":
                print("ada lantai rusak")
            else:
                if len(barang_) == 1:
                    list2D[newpos[0]][newpos[1]] = "1"
                    barang_.pop(0)
                elif len(barang_) == 0:
                    print("Tidak ada barang bawaan")
        except:
            print("Tidak bisa menaruh barang, mencapai batas map")
    elif dir == "l":
        x = find(list2D, "L")
        newpos = list(x)
        newpos[1] = newpos[1] - 1
        if newpos[1] < 0:
            print("Tidak bisa menaruh barang, mencapai batas map")
        elif list2D[newpos[0]][newpos[1]] == "1":
            print("ada barang lain")
        elif list2D[newpos[0]][newpos[1]] == "-1":
            print("ada lantai rusak")
        else:
            if len(barang_) == 1:
                list2D[newpos[0]][newpos[1]] = "1"
                barang_.pop(0)
            elif len(barang_) == 0:
                print("Tidak ada barang bawaan")
    elif dir == "r":
        x = find(list2D, "L")
        newpos = list(x)
        try:
            newpos[1] = newpos[1] + 1
            if list2D[newpos[0]][newpos[1]] == "1":
                print("ada barang lain")
            elif list2D[newpos[0]][newpos[1]] == "-1":
                print("ada lantai rusak")
            else:
                if len(barang_) == 1:
                    list2D[newpos[0]][newpos[1]] = "1"
                    barang_.pop(0)
                elif len(barang_) == 0:
                    print("Tidak ada barang bawaan")
        except:
            print("tidak bisa menaruh barang, mencapai batas map")
    else:
        print("perintah tidak dikenali")
    print('\n'.join(map(' '.join, list2D)))


while True:
    mov = input("Masukkan perintah: ")
    if mov == "u":
        x = find(list2D, "L")
        newpos = list(x)
        list2D[newpos[0]][newpos[1]] = "0"
        newpos[0] = newpos[0] - 1
        if newpos[0] < 0:
            print("mencapai batas map")
            newpos[0] = newpos[0] + 1
            list2D[newpos[0]][newpos[1]] = "L"
        elif list2D[newpos[0]][newpos[1]] == "1":
            print("tidak bisa menginjak barang")
            newpos[0] = newpos[0] + 1
            list2D[newpos[0]][newpos[1]] = "L"
        elif list2D[newpos[0]][newpos[1]] == "-1":
            print("hati hati, lantai rusak")
            newpos[0] = newpos[0] + 1
            list2D[newpos[0]][newpos[1]] = "L"
        else:
            list2D[newpos[0]][newpos[1]] = "L"
        # Menampilkan/update map setiap kali ada pergerakan
        print('\n'.join(map(' '.join, list2D)))

    elif mov == "d":
        x = find(list2D, "L")
        newpos = list(x)
        list2D[newpos[0]][newpos[1]] = "0"
        try:
            newpos[0] = newpos[0] + 1
            if list2D[newpos[0]][newpos[1]] == "1":
                print("tidak bisa menginjak barang")
                newpos[0] = newpos[0] - 1
                list2D[newpos[0]][newpos[1]] = "L"
            elif list2D[newpos[0]][newpos[1]] == "-1":
                print("hati hati, lantai rusak")
                newpos[0] = newpos[0] - 1
                list2D[newpos[0]][newpos[1]] = "L"
            else:
                list2D[newpos[0]][newpos[1]] = "L"
        except:
            print("Mencapai batas map")
            newpos[0] = newpos[0] - 1
            list2D[newpos[0]][newpos[1]] = "L"
        print('\n'.join(map(' '.join, list2D)))

    elif mov == "l":
        x = find(list2D, "L")
        newpos = list(x)
        list2D[newpos[0]][newpos[1]] = "0"
        newpos[1] = newpos[1] - 1
        if newpos[1] < 0:
            print("mencapai batas map")
            newpos[1] = newpos[1] + 1
            list2D[newpos[0]][newpos[1]] = "L"
        elif list2D[newpos[0]][newpos[1]] == "1":
            print("tidak bisa menginjak barang")
            newpos[1] = newpos[1] + 1
            list2D[newpos[0]][newpos[1]] = "L"
        elif list2D[newpos[0]][newpos[1]] == "-1":
            print("hati hati, lantai rusak")
            newpos[1] = newpos[1] + 1
            list2D[newpos[0]][newpos[1]] = "L"
        else:
            list2D[newpos[0]][newpos[1]] = "L"
        print('\n'.join(map(' '.join, list2D)))

    elif mov == "r":
        x = find(list2D, "L")
        newpos = list(x)
        list2D[newpos[0]][newpos[1]] = "0"
        try:
            newpos[1] = newpos[1] + 1
            if list2D[newpos[0]][newpos[1]] == "1":
                print("tidak bisa menginjak barang")
                newpos[1] = newpos[1] - 1
                list2D[newpos[0]][newpos[1]] = "L"
            elif list2D[newpos[0]][newpos[1]] == "-1":
                print("hati hati, lantai rusak")
                newpos[1] = newpos[1] - 1
                list2D[newpos[0]][newpos[1]] = "L"
            else:
                list2D[newpos[0]][newpos[1]] = "L"
        except:
            print("Mencapai batas map")
            newpos[1] = newpos[1] - 1
            list2D[newpos[0]][newpos[1]] = "L"
        print('\n'.join(map(' '.join, list2D)))

    elif mov == "s":
        # Kondisional jika perintah adalah s maka kembali ke fungsi scan
        scan(input("Masukkan arah scan: "))
    elif mov == "pi":
        # Kondisional jika perintah adalah pi maka kembali ke fungsi pickup
        pickup(input("Where to pick? "))
    elif mov == "pu":
        drop(input("Where to put? "))
    elif mov == "w":  # perintah jika ingin menampilkan map
        print('\n'.join(map(' '.join, list2D)))
    elif mov == "q" or "selesai" or "quit":
        print("Thanks for your service, have a nice day..")
        exit()
    else:
        print("Perintah tidak dikenali")
