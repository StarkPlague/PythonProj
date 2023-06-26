'''
Fa'iq Ali Sutiono
Informatika
1152100040
'''
akun = []  # inisialisasi
uang = 1000000
barang = []
diamond = 0
dialog = ["Ya", "Yes", "y", "Y", "ya", "yes"]
App = [["GPS", "5000"], ["Job Seeker", "7000"],
       ["Rim - Kirim", "10000"]]
App_ = []


def find(l, elem):
    for row, i in enumerate(l):
        try:
            column = i.index(elem)
        except ValueError:
            continue
        return row, column
    return -1


while True:
    print("Selamat datang di aplikasiKu: \
        \n1. log-in \
        \n2. sign-in \
        \n3. log-out")
    pilihan = input("Silahkan pilih menu aplikasiKu: ")
    if pilihan == "3":
        print("Terima kasih banyak telah berkunjung ke aplikasiKu")
        break
    elif pilihan == "2":
        print("Silahkan daftar akun anda")
        userPass = []  # inisialisasi
        u = userPass.append(input("Silahkan masukan username: "))
        p = userPass.append(input("Silahkan masukan password: "))
        print("verifikasi username dan password")
        #userPass [0][1]
        # nesting list (list n dimenasi)
        akun.append(userPass)
        # [0][0] username [0][1] - data pertama
        # [1][0] username [1][1] - data kedua
        print("akun sesuai")
        print("akun berhasil dibuat, silahkan log-in")

    elif pilihan == "1":
        try:
            usernameLogin = input("silahkan masukkan username: ")
            passwordLogin = input("silahkan masukkan username: ")
            if usernameLogin and passwordLogin:
                U = list(find(akun, usernameLogin))
                P = list(find(akun, passwordLogin))
                print("cek apakah akun sudah ada / belum")
                if len(akun) <= 0:
                    print("Anda belum memiliki akun, silahkan sign-in")

                    # looping baris kolom
                    # cari akun yang sesuai
                    # tugas tutorial terakhir
                    # 1. implementasikan looping mencari userPass dalam akun
                elif U[0] == P[0]:
                    print("Akun sesuai")
                    while True:
                        print("="*40)
                        print("Selamat datang", akun[0]
                              [0], "di dashboard Aplikasiku:")
                        print("~"*40)
                        print("Diamond: ", diamond)
                        print("Uang: ", uang)
                        print("~"*40)
                        print(" 1. Jual\n 2. Beli\n 3. Top up diamond\n 4. Log-out")
                        no = input("pilih: ")
                        if no == "1":
                            cek = len(barang)
                            if cek == 0:
                                print("Anda tidak memiliki item")
                            else:
                                print("Anda memiliki item: ")
                                for i in range(len(barang)):
                                    print(
                                        i+1, ".", " Seharga ".join(barang[i]), "Diamond")
                                pilih = input(
                                    "Apakah anda ingin menjual aplikasi? ")
                                if pilih in dialog:
                                    try:
                                        pilih_item = int(
                                            input("Pilih item yang ingin dijual... "))
                                        if pilih_item > len(barang):
                                            print("item tidak ditemukan")
                                        else:
                                            print("Anda ingin menjual",
                                                  barang[pilih_item-1][0], "Seharga ", barang[pilih_item-1][1], "Diamond ? (Pajak berlaku)")
                                            ans = input("your answer: ")
                                            if ans in dialog:
                                                pajak = round(
                                                    1/3*int(barang[pilih_item-1][1])-50)
                                                print("Selamat, Aplikasi ",
                                                      barang[pilih_item-1][0], "telah terjual!, Diamond +", pajak)
                                                diamond += pajak
                                                barang.pop(pilih_item-1)
                                    except:
                                        print("item tidak ditemukan")
                                else:
                                    print("transaksi penjualan dibatalkan")
                        elif no == "2":
                            if len(App) < 1:
                                print("Stock aplikasi habis")
                            else:
                                print("App yang tersedia: ")
                                for i in range(len(App)):
                                    print(
                                        i+1, ".", " Seharga ".join(App[i]), "Diamond")
                                try:
                                    pilih = int(
                                        input("Silahkan pilih App yang ingin dibeli: "))
                                    if len(App) < pilih > len(App):
                                        print("Aplikasi tidak ditemukan")
                                    else:
                                        print("Anda yakin ingin membeli",
                                              App[pilih-1][0], "Seharga ", App[pilih-1][1], "Diamond ?")
                                        ans = input("your answer: ")
                                        if ans in dialog:
                                            if diamond < int(App[pilih-1][1]):
                                                print(
                                                    "Hmm.. Diamond kamu tidak mencukupi nih :(")
                                            else:
                                                print("Hore!, Transaksi ",
                                                      App[pilih-1][0], "kamu berhasil !")
                                                diamond -= int(App[pilih-1][1])
                                                barang.append(
                                                    [App[pilih-1][0], App[pilih-1][1]])
                                                App.pop(pilih-1)
                                        else:
                                            print("Transaksi dibatalkan")
                                except:
                                    print("Aplikasi tidak ditemukan")

                        elif no == "3":
                            dm = [["3000", "50000"], ["5000", "60000"],
                                  ["8500", "100000"], ["14000", "155000"]]
                            print(
                                "Pilih paket diamond yang di inginkan: \n 1. 3000 diamond - 50000\n 2. 5000 diamond - 60000\n 3. 8500 diamond - 100000\n 4. 14000 diamond - 155000")
                            try:
                                pilih = int(input("pilih: "))
                                if pilih not in range(1, 5):
                                    print("paket tidak ditemukan")
                                else:
                                    print("Beli",
                                          dm[pilih-1][0], "Diamond Seharga", "Rp", dm[pilih-1][1], "?")
                                    ans = input("your answer: ")
                                    if ans in dialog:
                                        uang -= int(dm[pilih-1][1])
                                        diamond += int(dm[pilih-1][0])
                                    else:
                                        print("Transaksi dibatalkan")
                            except:
                                print("paket tidak ditemukan")
                        elif no == "4":
                            break
                            continue
                        else:
                            print("Perintah tidak dikenali")
                else:
                    print("akun tidak sesuai, \
                        \nsilahkan masukan username dan password yang benar")
            else:
                print("Masukkan username dan password dengan benar")
        except:
            print("username atau password tidak terdaftar")
    else:
        print("perintah tidak dikenali")

        # TODO: kasus -> kalau user tidak menginput 1 / 2 / 3
