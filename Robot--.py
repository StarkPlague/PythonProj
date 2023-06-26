"""
Robot angkut gudang
By Raihan Desfitra 
NRP 1152100019
Prodi Informatika
Aplikasi robotAngkutV0.25
"""

import os #untuk clear command

#TODO: mengatur ukuran lantai, dapat dilakukan tanpa def
def create(ukuran):
    if len(ukuran) != 2: 
        ukuran.append(ukuran[0]) 
        #Jika input dari user hanya berupa 1 data maka copy dan paste sebagai data kedua

    #cek jika input yang user masukan adalah angka atau bukan, masuan jika angka
    for i in ukuran:
        if i.isnumeric():
            size.append(i)

#TODO: Melihat lantai sekarang, akan terupdate jika memindahkan sesuatu dengan command
def view():
    

    #memulai dari akhir (Panjang lantai -1, karena python memulai data dari 0) ke -1 (karena -1 akan dihiraukan, dan akan ke 0) dengan langkah -1 (agar menurun)
    for i in range(len(lantai)-1,-1,-1):
        output = []
        #memasukan isi Y ke list untuk di print dengan fungsi join
        for j in lantai[i]:
            if j == "-1":
                output.append(j + " ") #jia -1 maka hilangkan spasi di awal agar sebaris
            else:
                output.append(" " + j + " ") #jika bukan tambah spasi di awal dan akhir agar sebaris

        print(" ".join(output)) #jadikan string list tersebut
    #ulang hingga habis

#TODO: cek jika terdapat barang atau lantai rusak di arah yang dituju
def move_Check(position,direction):
    #cek sesuai direksi yang diminta 
    #dan mengembalikan data yang dibutuhkan apabila dapat berjalan menujur arah tersebut atau tidak
    if direction == "u":
        #jika arah tersebut diluar map/gudang
        if position[1] + 1 > int(size[0]) - 1: 
            return [False]

        #kembalikan [True,isi di lantai yang ingin di tuju] jika lantai yang dituju adalah 0 atau -1
        #kembalikan [False,1] jika bertemu barang
        return [[True,lantai[position[1] + 1][position[0]]] if lantai[position[1] + 1][position[0]] == "0" or lantai[position[1] + 1][position[0]] == "-1" else [False,"1"]][0]

    elif direction == "d":
        #jika arah tersebut diluar map/gudang
        if position[1] - 1 < 0:
            return [False]

        #kembalikan [True,isi di lantai yang ingin di tuju] jika lantai yang dituju adalah 0 atau -1
        #kembalikan [False,1] jika bertemu barang
        return [[True,lantai[position[1] - 1][position[0]]] if lantai[position[1] - 1][position[0]] == "0" or lantai[position[1] - 1][position[0]] == "-1" else [False,"1"]][0]

    elif direction == "l":
        #jika arah tersebut diluar map/gudang
        if position[0] - 1 < 0:
            return [False]

        #kembalikan [True,isi di lantai yang ingin di tuju] jika lantai yang dituju adalah 0 atau -1
        #kembalikan [False,1] jika bertemu barang
        return [[True,lantai[position[1]][position[0] - 1]] if lantai[position[1]][position[0] - 1] == "0" or lantai[position[1]][position[0] - 1] == "-1" else [False,"1"]][0]

    elif direction == "r":
        #jika arah tersebut diluar map/gudang
        if position[0] + 1 > int(size[1]) - 1:
            return [False]

        #kembalikan [True,isi di lantai yang ingin di tuju] jika lantai yang dituju adalah 0 atau -1
        #kembalikan [False,1] jika bertemu barang
        return [[True,lantai[position[1]][position[0] + 1]] if lantai[position[1]][position[0] + 1] == "0" or lantai[position[1]][position[0] + 1] == "-1" else [False,"1"]][0]

#TODO: scan arah yang diminta apabila terdapat lantai rusak atau barang
def scan(location,direction):
    #cek sesuai direksi yang diminta
    #jika terdapat barang atau lantai rusak, atau kosong akan dikembalikan dengan id masing masing,
    #dengan arah tertentu untuk memberi tahu user bahwa sudah me-cek arah tersebut
    if direction in ["u","up","atas"]:
        if location[1] + 1 > int(size[0]) - 1:
            return None
        #kembalikan [isi dari lokasi lantai yang di cek, dan arahnya]
        return [[y,"up"] for y in lantai[location[1] + 1]][location[0]]

    elif direction in ["d","down","bawah"]:
        if location[1] - 1 < 0:
            return None

        #kembalikan [isi dari lokasi lantai yang di cek, dan arahnya]
        return [[y,"down"] for y in lantai[location[1] - 1]][location[0]]

    elif direction in ["l","left","kiri"]:
        if location[0] - 1 < 0:
            return None

        #kembalikan [isi dari lokasi lantai yang di cek, dan arahnya]
        return [[y,"left"] for y in lantai[location[1]]][location[0] - 1]

    elif direction in ["r","right","kanan"]:
        if location[0] + 1 > int(size[1]) - 1:
            return None

        #kembalikan [isi dari lokasi lantai yang di cek, dan arahnya]
        return [[y,"right"] for y in lantai[location[1]]][location[0] + 1]

#TODO: membawa barang jika ada di arah yang ditentukan user
def pickup(location,direction):
    #cek apabila terdapat barang di arah yang user minta
    #jika ada kembalikan True, jika tidak False, dengan keduanya mengembalikan string arah yang di cek
    #dan lokasi barang jika ada untuk diubah di map/gudang
    if direction in ["u","up","atas"]:
        if location[1] + 1 > int(size[0]) - 1:
            return [False,"up"]

        #kembalikan [True,arah,dan lokasi barang] jika terdapat barang, kembalikan [False, arah] jika tidak ada
        return [[True,"up",[location[1] + 1,location[0]]] if lantai[location[1] + 1][location[0]] == "1" else [False,"up"]][0]

    elif direction in ["d","down","bawah"]:
        if location[1] - 1 < 0:
            return [False,"down"]

        #kembalikan [True,arah,dan lokasi barang] jika terdapat barang, kembalikan [False, arah] jika tidak ada
        return [[True,"down",[location[1] - 1,location[0]]] if lantai[location[1] - 1][location[0]] == "1" else [False,"down"]][0]

    elif direction in ["l","left","kiri"]:
        if location[0] - 1 < 0:
            return [False,"left"]
            
        #kembalikan [True,arah,dan lokasi barang] jika terdapat barang, kembalikan [False, arah] jika tidak ada
        return [[True,"left",[location[1],location[0] - 1]] if lantai[location[1]][location[0] - 1] == "1" else [False,"left"]][0]

    elif direction in ["r","right","kanan"]:
        if location[0] + 1 > int(size[1]) - 1:
            return [False,"right"]

        #kembalikan [True,arah,dan lokasi barang] jika terdapat barang, kembalikan [False, arah] jika tidak ada
        return [[True,"right",[location[1],location[0] + 1]] if lantai[location[1]][location[0] + 1] == "1" else [False,"right"]][0]

#TODO: menaruh barang ke arah yang ditentukan user
def put_down(location,direction):
    #cek apabila arah yang ditentukan user dapat ditaruh barang atau tidak
    #jika iya, mengembalikan True dan lokasinya untuk ditaruh
    #jika tidak, mengembalikan False dan alasan mengapa tidak bisa beserah arak yang usah di cek
    if direction in ["u","up","atas"]:
        if location[1] + 1 >= len(lantai):
            return [False,"thing","up"]

        #kembalikan [True,dan lokasi barang] jika bisa, kembalikan [False,alasan tidak bisa, arah] jika tidak bisa
        return [[True,[location[1] + 1,location[0]]] if lantai[location[1] + 1][location[0]] == "0" else [False,["tile cracked" if lantai[location[1] + 1][location[0]] == "-1" else "object"][0],"up"]][0]
    
    elif direction in ["d","down","bawah"]:
        if location[1] - 1 < 0:
            return [False,"thing","up"]
        
        #kembalikan [True,dan lokasi barang] jika bisa, kembalikan [False,alasan tidak bisa, arah] jika tidak bisa
        return [[True,[location[1] - 1,location[0]]] if lantai[location[1] - 1][location[0]] == "0" else [False,["tile cracked" if lantai[location[1] - 1][location[0]] == "-1" else "object"][0],"down"]][0]
    
    elif direction in ["l","left","kiri"]:
        if location[0] - 1 < 0:
            return [False,"thing","up"]
        
        #kembalikan [True,dan lokasi barang] jika bisa, kembalikan [False,alasan tidak bisa, arah] jika tidak bisa
        return [[True,[location[1],location[0] - 1]] if lantai[location[1]][location[0] - 1] == "0" else [False,["tile cracked" if lantai[location[1]][location[0] - 1] == "-1" else "object"][0],"left"]][0]
    
    elif direction in ["r","right","kanan"]:
        if location[0] + 1 >= len(lantai[0]):
            return [False,"thing","up"]
        
        #kembalikan [True,dan lokasi barang] jika bisa, kembalikan [False,alasan tidak bisa, arah] jika tidak bisa
        return [[True,[location[1],location[0] + 1]] if lantai[location[1]][location[0] + 1] == "0" else [False,["tile cracked" if lantai[location[1]][location[0] + 1] == "-1" else "object"][0],"right"]][0]

#TODO: memindahkan lokasi robot di map/gudang, dapat dilakukan tanpa fungsi
def robot_move_to(location_from,location_to,rusak):
    if rusak:
        lantai[location_from[1]][location_from[0]] = "-1" 
        lantai[location_to[1]][location_to[0]] = "X"
    else:
        lantai[location_from[1]][location_from[0]] = "0" 
        lantai[location_to[1]][location_to[0]] = "X"

#TODO: memotong user input menjadi list agar mudah dibaca dan dimengerti program
def ParseMSG(msg):
    #index untuk kalimat keberabaan string dari input user dan string untuk menyimpannya kembali ke list
    index = 0
    string = [[]]

    #cek jika terdapat spasi atau koma untuk memutuskan ke beradaan selanjutnya dan menambah string untuk identifikasi bahwa itu kalimat selanjutnya
    for i in msg:
        if i == " " or i == ",":
            index += 1
            string.append([])
            continue

        string[index].append(i) #masukan ke list string

    output_list = [x for x in string if x] #cek ulang list apabila terdapat list kosong
    output_text = ["".join(n) for n in output_list] #menjadikan satu string yang tadinya terpisah

    return output_text #kembalikan hasil cek berupa list

#TODO: Membaca file txt yang diberikan untuk dijadikan lokasi lokasi di map
def read_file(filename):
    #Cek jika file ada
    if os.path.exists(filename):
        #buka, baca, dan tutup filenya
        data = open(filename) ; data_string = data.read() ; data.close() ; data = data_string

        index = 0 #lokasi X
        data_asli = [[]] #list 2 dimensi untuk menyimpan lokasi lokasi
        for i in data: #cek setiap data
            if i == "\n": #jika enter atau \n maka itu data baru
                index += 1
                data_asli.append([])
                continue
            elif i == " " or i == ",": #pisahkan angka dengan spasi atau koma
                continue
            data_asli[index].append(i) #masukan angka ke list 2 dimensi 

        data_list = [] #format para data agar mudah dibaca
        data_list.append(data_asli[0]); del data_asli[0] #ukuran map, masukan ke list dan hapus dari list sebelumnya agar mudah di ingat
        data_list.append(data_asli[0]); del data_asli[0] #lokasi robot, masukan ke list dan hapus dari list sebelumnya agar mudah di ingat

        data_list.append([]) #membuat list untuk setiap lokasi barang
        for i in range(len(data_asli[0])): #loop sebanyak data lokasi barang dan satukan
            if i%2 == 0: #cek jika ini data yang disatukan atau bukan
                continue
            data_list[2].append(data_asli[0][:2]) #satukan data dan masukan ke list untuk lokasi barang
            del data_asli[0][:2] #hapus agar mudah di di ingat
        del data_asli[0] #hapus dari list agar mudah di ingat
        data_list.append([]) #membuat list untuk setiap lokasi lantai rusak
        for i in range(len(data_asli[0])): #loop sebanyak data lokasi lantai rusak dan satukan
            if i%2 == 0: #cek jika ini data yang disatukan
                continue
            data_list[3].append(data_asli[0][:2]) #satukan data dan masukan ke list untuk lokasi lantai rusak
            del data_asli[0][:2] #hapus dari list agar mudah di ingat
        del data_asli[0] #hapus dari list agar mudah di ingat
        data_list[1] = [x for x in data_list[1] if x] #cek jika terdapat list kosong
        data_list[2] = [x for x in data_list[2] if x] #cek jika terdapat list kosong
        return data_list #kembalikan data yang sudah di prosess
    else:
        return None #kembalikan None jika tidak ditemukan filenya

os.system("cls" if os.name == "nt" else "clear") #menghapus isi cmd/terminal untuk lebih rapih

#untuk mengabaikan error "KeyboardInteruption" yang mungkin akan dikira error besar oleh orang biasa
try:
    #variable untuk digunakan nantinya
    Robot = []
    size = []
    lantai = []

    Barang = {"Barang":[],"Rusak":[]}

    membawa_barang = False
    berada_lantai_rusak = False

    #meminta user jika ingin menggunakan map/gudang dari input atau file
    memilih_file = input("Apakah anda ingin memasukan map melalui file ? (tidak/iya) ")
    memilih_file = ParseMSG(memilih_file) #mengubahnya menjadi list agar mudah dibaca
    memilih_file = [x for x in memilih_file if x] #pengecekan ulang, hanya untuk lebih percaya diri

    #lakukan terus hingga user memasukan input
    while not memilih_file:
        memilih_file = input("Apakah anda ingin memasukan map melalui file ? (tidak/iya) ")
        memilih_file = ParseMSG(memilih_file)
        memilih_file = [x for x in memilih_file if x]

    #jika tidak, maka program akan meminta input dari user untuk map/gudang
    if memilih_file[0].lower() in ["x","tidak","no"]:
        ukuran = input("Silahkan masukan ukuran map (X,Y) : ") #meminta X,Y dari lantai
        ukuran = ParseMSG(ukuran) #membuatnya menjadi list agar mudah dibaca
        ukuran = [x for x in ukuran if x.isnumeric()] #hanya memasukan angka dan tidak lebih
        ukuran = ukuran[:2] #jika lebih dari 2 data, maka tidak digunakan sisanya

        #meminta ulang hingga data di isi
        while not ukuran:
            ukuran = input("Silahkan masukan ukuran map (X,Y) : ")
            ukuran = ParseMSG(ukuran)
            ukuran = [x for x in ukuran if x.isnumeric()]
            ukuran = ukuran[:2]

        #memasukan data ke list yang akan digunakan untuk membuat map/gudang dari user input
        create(ukuran)
        lock = [] #variable sementara untuk input user untuk map/gudang
        print("Silahkan masukan letak letak map")
        #ulang sebanyak X
        for i in range(int(size[0])):
            lokasi = input() #meminta input
            lokasi = ParseMSG(lokasi) #diubah menjadi lsit agar mudah dibaca
            if len(lokasi) > int(size[1]): #jika kosong atau lebih dari Y maka hapus
                lokasi = [x for x in lokasi if x.isnumeric()] #hanya memasukan angka dan tidak yang lain
                lokasi = lokasi[:int(size[1])] #menghapus sisanya

            lock.append(lokasi) #masukan ke variable sementara

        lock.reverse() #balik lokasi list, dengan awal menjadi akhir dan akhir menjadi awal
        lantai = lock #masukan ke lantai untuk digunakan nantinya

    #jika iya, maka program akan meminta nama file, harap file berada 1 folder bersama dengan program
    elif memilih_file[0].lower() in ["y","iya","yes"]:
        #pengingat
        print("Pastikan isi file berupa\n<Ukuran X gudang> <Ukuran Y gudang>\n<lokasi robot(x,y)>\n<Lokasi barang(x,y x,y)>\n<lokasi lantai rusak (x,y x,y)>")
        nama_file = input("Nama file (.txt): ") #meminta nama file
        if ".txt" not in nama_file: #jika lupa menambahkan .txt di akhir, tambahkan
            nama_file = nama_file + ".txt"

        data = read_file(nama_file) #dapatkan lokasi lokasi dari file yang sudah di prosess

        #jika file ada
        if data:
            data[0].reverse() #balik data agar dapat dimulai dari kiri bawah sebagai 0,0
            create(data[0]) #buat lantai kosong sebesar data yang diberikan
            for x in range(int(data[0][0])): #loop sebanyak ukuran X
                lantai.append([]) #tambahkan list untuk X
                for y in range(int(data[0][1])): #loop sebanyak ukuran Y
                    if x == int(data[1][1]) and y == int(data[1][0]): #jika lokasi sama dengan lokasi robot di data
                        lantai[x].append("X")
                    else: #jika tidak kosongkan
                        lantai[x].append("0")
            for lokasiBarang in data[2]: #loop setiap lokasi barang di data dan mengubah lokasi tersebut dengan data 1 sebagai barang
                lantai[int(lokasiBarang[1])][int(lokasiBarang[0])] = "1"
                Barang["Barang"].append(lokasiBarang)
            for lokasiRusak in data[3]:
                lantai[int(lokasiRusak[1])][int(lokasiRusak[0])] = "-1" #loop setiap lokasi barang di data dan mengubah lokasi tersebut dengan data -1 sebagai lantai rusak
                Barang["Rusak"].append(lokasiRusak)
            
        else: #file tidak ditemukan
            print("File yang diberikan tidak ditemukan, silahkan buat file txt dengan nama tersebut")
            print("Silahkan memulai ulang program")
            print("Shutting down...")
            exit()

    #jika tidak ingin memulai atau tidak sengaja memulai
    elif memilih_file[0].lower() in ["cancel","exit"]:
        print("Shutting down...")
        exit()

    #jika terdapat data masuk yang bukan iya atau tidak maka keluar dari program, karena ditakutkan user salah pilih file
    else:
        print("Maaf perintah tidak ditemukan")
        print("Silahkan memulai ulang program")
        print("Shutting down....")
        exit()

    #memulai dari akhir (Panjang lantai -1, karena python memulai data dari 0) ke -1 (karena -1 akan dihiraukan, dan akan ke 0) dengan langkah -1 (agar menurun)
    #mendapatkan lokasi robot, barang, dan lantai rusak di map
    Robot = [[y,x] for y in range(len(lantai[0])) for x in range(len(lantai)-1,-1,-1) if lantai[x][y].lower() == "x"][0]
    Barang["Barang"] = [[y,x] for y in range(len(lantai[0])) for x in range(len(lantai)-1,-1,-1) if lantai[x][y] == "1"]
    Barang["Rusak"] = [[y,x] for y in range(len(lantai[0])) for x in range(len(lantai)-1,-1,-1) if lantai[x][y] == "-1"]

    #memulai loop hingga user meminta untuk dihentikan
    while True: 
        print(berada_lantai_rusak)
        #meminta input dari user untuk apa yang akan dilakukan
        user_input = input("C:\\Robot> ")
        args = ParseMSG(user_input) #dijadikan list agar mudah dibaca
        if len(args) < 1: continue; #jika user tidak menulis apapun, untuk tidak mengeluarkan error
        cmd = args[0]; args.pop(0) #gunakan data pertama pada list sebagai perintah user kepada robot, dan hapus data pertama tersebut

        #TODO: Jika user ingin keluar dari program
        if cmd.lower() in ["q","quit","keluar","exit","quit()","keluar()","exit()"]:
            print("Shutting down...")
            break #Menhentikan loop
        
        #TODO: jika user ingin robot untuk bergerak ke atas, cek jika dapat dilakukan atau tidak, dan bergerak setelahnya
        elif cmd.lower() in ["u","up","atas","keatas","above","up()","atas()","keatas()","above()"]:
            check_output = move_Check(Robot,"u") #cek jika dapat bergerak ke arah tersebut
            if check_output[0]:
                old_robot = Robot #data lama untuk mengetahui lokasi robot sekarang
                Robot = [Robot[0],Robot[1] + 1] #data baru untuk mengetahui lokasi robot yang ingin dituju
                robot_move_to(old_robot,Robot,berada_lantai_rusak) #pindahkan robot
                print("Moving up")
                if berada_lantai_rusak: #jika lantai sebelumnya rusak
                    berada_lantai_rusak = not berada_lantai_rusak
                if check_output[1] == "-1": #jika tujuan adalah lantai rusak
                    berada_lantai_rusak = not berada_lantai_rusak

            else:
                print("It seems i can't go that way") #jika terdapat barang diarah yang dituju

            continue

        #TODO: jika user ingin robot untuk bergerak ke bawah, cek jika dapat dilakukan atau tidak, dan bergerak setelahnya
        elif cmd.lower() in ["d","down","bawah","kebawah","below","down()","bawah()","kebawah()","below()"]:
            check_output = move_Check(Robot,"d") #cek jika dapat bergerak ke arah tersebut
            if check_output[0]:
                old_robot = Robot #data lama untuk mengetahui lokasi robot sekarang
                Robot = [Robot[0],Robot[1] - 1] #data baru untuk mengetahui lokasi robot yang ingin dituju
                robot_move_to(old_robot,Robot,berada_lantai_rusak) #pindahkan robot
                print("Moving down")
                if berada_lantai_rusak: #jika lantai sebelumnya rusak
                    berada_lantai_rusak = not berada_lantai_rusak
                if check_output[1] == "-1": #jika tujuan adalah lantai rusak
                    berada_lantai_rusak = not berada_lantai_rusak
                

            else:
                print("It seems i can't go that way")

            continue

        #TODO: jika user ingin robot untuk bergerak ke kiri, cek jika dapat dilakukan atau tidak, dan bergerak setelahnya
        elif cmd.lower() in ["l","left","kiri","kekiri","left()","kiri()","kekiri()"]:
            check_output = move_Check(Robot,"l") #cek jika dapat bergerak ke arah tersebut
            if check_output[0]:
                old_robot = Robot #data lama untuk mengetahui lokasi robot sekarang
                Robot = [Robot[0] - 1,Robot[1]] #data baru untuk mengetahui lokasi robot yang ingin dituju
                robot_move_to(old_robot,Robot,berada_lantai_rusak) #pindahkan robot
                print("Moving left")
                if berada_lantai_rusak: #jika lantai sebelumnya rusak
                    berada_lantai_rusak = not berada_lantai_rusak
                if check_output[1] == "-1": #jika tujuan adalah lantai rusak
                    berada_lantai_rusak = not berada_lantai_rusak

            else:
                print("It seems i can't go that way")

            continue

        #TODO: jika user ingin robot untuk bergerak ke kanan, cek jika dapat dilakukan atau tidak, dan bergerak setelahnya
        elif cmd.lower() in ["r","right","kanan","kekanan","right()","kanan()","kekanan()"]:
            check_output = move_Check(Robot,"r") #cek jika dapat bergerak ke arah tersebut
            if check_output[0]:
                old_robot = Robot #data lama untuk mengetahui lokasi robot sekarang
                Robot = [Robot[0] + 1,Robot[1]] #data baru untuk mengetahui lokasi robot yang ingin dituju
                robot_move_to(old_robot,Robot,berada_lantai_rusak) #pindahkan robot
                print("Moving right")
                if berada_lantai_rusak: #jika lantai sebelumnya rusak
                    berada_lantai_rusak = not berada_lantai_rusak
                if check_output[1] == "-1": #jika tujuan adalah lantai rusak
                    berada_lantai_rusak = not berada_lantai_rusak

            else:
                print("It seems i can't go that way")

            continue

        #TODO: untuk melihat lokasi di map/gudang
        elif cmd.lower() in ["w"]:
            view()
            continue

        #TODO: cek jika terdapat sesuatu di arah yang ditentukan user, dan akan mengeluarkan output apakah sesuatu tersebut
        elif cmd.lower() in ["s","scan","scan()"]:
            if len(args) > 0 and args[0]: #jika user input arah sebelum diminta
                scan_output = scan(Robot,args[0].lower()) #mengembalikan hasil scan

            else:
                direction = input("C:\\Robot\\Direction> ") #meminta arah ke user
                #jika user tidak mengisi dan tidak sesuai maka ulangi
                while not direction or direction not in ["r","l","u","d","right","left","up","down","kanan","kiri","atas","bawah"]:
                    direction = input("C:\\Robot\\Direction> ")
                    
                direction = ParseMSG(direction) #jadikan list agar mudah dibaca

                #jika tetap tidak kosong dan user benar input arah
                if len(direction) > 0 and direction[0]:
                    scan_output = scan(Robot,direction[0].lower()) #mengembalikan hasil scan

            #output ke user apa yang ditemukan dan arah yang si cek
            if scan_output[0] is "1":
                print("There is an object to my",scan_output[1])

            elif scan_output[0] is "-1":
                print("There is a broken tiles to my",scan_output[1])

            elif scan_output[0] is "0":
                print("There is nothing on my", scan_output[1])

            else:
                print("It seems the scan outside the map")
            continue

        #TODO: mengambil barang di arah yang user input, jika tidak ada atau tidak bisa maka akan di output alasannya
        elif cmd.lower() in ["pi","pickup","pickup()"]:
            if len(args) > 0 and args[0]: #jika user memasukan arah sebelum diminta
                pickup_output = pickup(Robot,args[0].lower()) #mengembalika hasil jika dapat ditaruh

            else:
                direction = input("C:\\Robot\\Direction> ") #meminta arah ke user
                #jika input kosong atau tidak sesuai, ulangi
                while not direction or direction not in ["r","l","u","d","right","left","up","down","kanan","kiri","atas","bawah"]:
                    direction = input("C:\\Robot\\Direction> ")

                direction = ParseMSG(direction) #jadikan list agar mudah dibaca

                #jika tetap tidak kosong dan user benar input arah
                if len(direction) > 0 and direction[0]:
                    pickup_output = pickup(Robot,direction[0].lower()) #mengembalikan hasil jika dapat ditaruh

            #jika tidak membara barang dan terdapat barang maka bawa barang tersebut
            #jika tidak terdapat barang maka output kan ke user
            #jika membawa barang dan terdapat barang, output ke user tidak dapat membawa lebih dari 1
            if pickup_output[0] and not membawa_barang:
                print("Picked up the object to my ",pickup_output[1])
                membawa_barang = not membawa_barang
                lantai[pickup_output[2][0]][pickup_output[2][1]] = "0"

            elif not pickup_output[0]:
                print("There is nothing to pick up on my ", pickup_output[1])

            elif membawa_barang and pickup_output[0]:
                print("Cant picked up anymore object")

            else:
                print("It seems the command direction is outside the map")

            continue

        #TODO: menaruh barang ke arah user input, jika terdapat lantai rusak atau barang tidak akan ditaruh dan akan output alasannya
        elif cmd.lower() in ["pu","put","put()"]:
            if len(args) > 0 and args[0]: #jika user memasukan arah sebelum diminta
                put_output = put_down(Robot,args[0].lower()) #mengembalikan jika dapat ditaruh dan lokasi yang akan ditaruh 

            else:
                direction = input("C:\\Robot\\Direction> ") #meminta arah ke user
                #jika user tidak mengisi atau tidak sesuai, maka ulangi
                while not direction or direction not in ["r","l","u","d","right","left","up","down","kanan","kiri","atas","bawah"]:
                    direction = input("C:\\Robot\\Direction> ")

                direction = ParseMSG(direction) #jadikan list agar mudah dibaca

                #jika tetap tidak kosong dan user benar input arah
                if len(direction) > 0 and direction[0]: 
                     put_output = put_down(Robot,direction[0].lower()) #mengembalikan jika dapat ditaruh dan lokasi yang akan ditaruh 

            #jika membawa barang dan dapat menaruh barang, taruh
            #jika tidak membawa barang dan dapat menaruh maka output ke user
            #jika tidak dapat menaruh output ke user
            if put_output[0] and membawa_barang:
                print("Putting down the object")
                membawa_barang = not membawa_barang
                lantai[put_output[1][0]][put_output[1][1]] = "1"

            elif put_output[0] and not membawa_barang:
                print("Im sorry, im not carrying anything")

            elif not put_output[0]:
                print("It seems theres some ", put_output[1]," on my ",put_output[2])

            else:
                print("It seems the scan outside the map")
                
            continue
        
        #TODO: untuk membersihkan cmd/terminal
        elif cmd.lower() in ["cls","clear"]:
            os.system("cls" if os.name == "nt" else "clear")
            continue

        #TODO: jika user bingung akan semua perintah di program ini
        elif cmd.lower() in ["help","tolong","h"]:
            print("List of command:")
            output = []
            output.append("- up")
            output.append("- down")
            output.append("- left")
            output.append("- right")
            output.append("- w")
            output.append("- scan <direction>")
            output.append("- pickup <direction>")
            output.append("- put <direction>")
            output.append("- clear")
            output.append("- exit")
            print("\n".join(output))
            continue

        #TODO: jika user memasukan program yang tidak ada maka akan output untuk tidak error dan mengulang ke loop selanjutnya
        else:
            print(f"'{cmd}' is not recognized as an internal or external command, please use 'help'")
            continue

 
except KeyboardInterrupt: #jika user melakukan CTRL + C, dan tidak akan mengeluarkan error yang mungkin membuat takut user
    print("exit\nShutting down...")