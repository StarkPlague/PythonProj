#melihatkan item di 1 tipe

import decimal

movement,magic,attack,defense = {},{},{},{}

temp = open("./items/Movement.txt")
temps = temp.read().split("\n")
temp.close()



for i in temps:
    movement[i.split(";")[0]] = int(i.split(";")[1])

temp = open("./items/Magic.txt")
temps = temp.read().split("\n")
temp.close()

for i in temps:
    magic[i.split(";")[0]] = int(i.split(";")[1])

temp = open("./items/Attack.txt")
temps = temp.read().split("\n")
temp.close()

for i in temps:
    attack[i.split(";")[0]] = int(i.split(";")[1])

temp = open("./items/Defense.txt")
temps = temp.read().split("\n")
temp.close()

for i in temps:
    defense[i.split(";")[0]] = int(i.split(";")[1])

repeat = "Tampilkan data item"

print("menu dalam program ini")
menu = f"1.{repeat} Movement\n2.{repeat} Magic\n3.{repeat} Attack\n4.{repeat} Defense\n5.Tampilkan total harga seluruh item\n"
menu = menu + f"6.Tampilkan rata-rata harga seluruh item\n7.Tampilkan total harga item tertentu\n8.Tampilkan rata-rata harga item tertentu\n9.keluar aplikasi"

print(menu)
pilihan_user = input()

while pilihan_user not in ["1","2","3","4","5","6","7","8","9"]:
    print(menu)
    pilihan_user = input()

if pilihan_user == "1":
    for i,v in movement.items():
        print(i,v,"gold")
elif pilihan_user == "2":
    for i,v in magic.items():
        print(i,v,"gold")
elif pilihan_user == "3":
    for i,v in attack.items():
        print(i,v,"gold")
elif pilihan_user == "4":
    for i,v in defense.items():
        print(i,v,"gold")
elif pilihan_user == "5":
    total = 0
    for i,v in movement.items():
        total += v
    for i,v in magic.items():
        total += v
    for i,v in attack.items():
        total += v
    for i,v in defense.items():
        total += v
    print("Total harga seluruh item adalah " + str(total) + " gold")
elif pilihan_user == "6":
    total = 0
    barang = 0
    for i,v in movement.items():
        total += v
        barang += 1
    for i,v in magic.items():
        total += v
        barang += 1
    for i,v in attack.items():
        total += v
        barang += 1
    for i,v in defense.items():
        total += v
        barang += 1
    total = float("{:.2f}".format(decimal.Decimal(total/barang)))
    print("Total harga seluruh item adalah " + str(total) + " gold")
elif pilihan_user == "7":
    print("Silahkan pilih jenis item")
    print("(Movement/Magic/Attack/Defense)")
    user_input = input()
    while user_input.lower() not in ["movement","magic","attack","defense"]:
        print("Silahkan pilih jenis item")
        print("(Movement/Magic/Attack/Defense)")
        user_input = input()
    total = 0
    if user_input.lower() == "movement":
        for i,v in movement.items():
            total += v
    elif user_input.lower() == "magic":
        for i,v in magic.items():
            total += v
    elif user_input.lower() == "attack":
        for i,v in attack.items():
            total += v
    elif user_input.lower() == "defense":
        for i,v in defense.items():
            total += v
    print("Total harga jenis " + user_input + " adalah " + str(total) + " gold")
elif pilihan_user == "8":
    print("Silahkan pilih jenis item")
    print("(Movement/Magic/Attack/Defense)")
    user_input = input()
    while user_input.lower() not in ["movement","magic","attack","defense"]:
        print("Silahkan pilih jenis item")
        print("(Movement/Magic/Attack/Defense)")
        user_input = input()
    total = 0
    barang = 0
    if user_input.lower() == "movement":
        for i,v in movement.items():
            total += v
            barang += 1
    elif user_input.lower() == "magic":
        for i,v in magic.items():
            total += v
            barang += 1
    elif user_input.lower() == "attack":
        for i,v in attack.items():
            total += v
            barang += 1
    elif user_input.lower() == "defense":
        for i,v in defense.items():
            total += v
            barang += 1
    total = float("{:.2f}".format(decimal.Decimal(total/barang)))
    print("Total harga jenis " + user_input + " adalah " + str(total) + " gold")
elif pilihan_user == "9":
    exit()