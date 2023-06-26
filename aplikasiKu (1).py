'''
Muhamad Soleh
Informatika
0302128902
'''

akun = [] #inisialisasi 

while True:
    print("Selamat datang di aplikasiKu: \
        \n1. log-in \
        \n2. sign-in \
        \n3. log-out")

    pilihan = int(input("Silahkan pilih menu aplikasiKu: "))
    if pilihan == 3:
        print("Terima kasih banyak telah berkunjung ke aplikasiKu")
        break
    elif pilihan == 2:
        print("Silahkan daftar akun anda")
        userPass = [] #inisialisasi
        userPass.append(input("Silahkan masukan username: "))
        userPass.append(input("Silahkan masukan password: "))
        print("verifikasi username dan password")
        #userPass [0][1]
        #nesting list (list n dimenasi)
        akun.append(userPass) 
        # [0][0] username [0][1] - data pertama
        # [1][0] username [1][1] - data kedua
        print("akun sesuai")
        print("akun berhasil dibuat, silahkan log-in")
    elif pilihan == 1:
        usernameLogin = input("Silahkan masukan username: ")
        passwordLogin = input("Silahkan masukan password: ")
        print("cek apakah akun sudah ada / belum")
        if len(akun) <= 0:
            print("Anda belum memiliki akun, silahkan sign-in")
        
        #looping baris kolom
        #cari akun yang sesuai
        #tugas tutorial terakhir 
        #1. implementasikan looping mencari userPass dalam akun
    
        elif usernameLogin == akun[0][0] and passwordLogin == akun[0][1]:
            print("Akun sesuai")
            print("Selamat datang di dashboard aplikasiKu: \
            \n1. jual\
            \n2. beli\
            \n3. top-up diamond\
            \n4. keluar")

            #TODO: implementasi menu jual dan beli
            #top up untuk mendapatkan diamond
            #diamond digunakan untuk membeli aplikasi
            #aplikasi dapat di jual
            #harga jual = 1/3 * harga beli - 50 
            #TODO: kasus -> kalau user tidak menginput 1 / 2 / 3 / 4

        else:
            print("akun tidak sesuai, \
                \nsilahkan masukan username dan password yang benar")
    #TODO: kasus -> kalau user tidak menginput 1 / 2 / 3


            
            

        


