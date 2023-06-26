menu = {"makanan": ["Bakso", "Nasgor"], "Minuman":["fanta", "kopi"]}

print('Cari menu: ')
print("""1. Makanan
2. Minuman
3. keluar""")

while True: 
    pilih = int(input("pilih menu: "))

    if pilih == 1:
        food = input("nama makanan: ")
        if food in menu["makanan"]:
            print("Makanan ada di list")
        else:
            print("Makanan tidak tersedia")

    elif pilih == 2:
        drink = input("Nama minuman: ")
        if drink in menu["Minuman"]:
            print("Minuman tersedia")
        else:
            print("Minuman tidak tersedia")
    else:
        break

    
    


