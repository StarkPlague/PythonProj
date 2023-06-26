data = {
    "D": ["Dada", 2500],
    "A": ["Ayam", 3500]
}

jumlah = int(input("Berapa banyak: "))

hasil = []
total_harga = []
for i in range(0, jumlah):
    jenis = input("Jenis apa: ")
    potong = int(input("Berapa potong: "))
    total = data[jenis][1]*potong
    total_harga.append(total)
    hasil.append([jenis, potong])


print(total_harga)
print(sum(total_harga))

# print(hasil[0][0]) #jenis
# print(hasil[0][1]) #banyak
