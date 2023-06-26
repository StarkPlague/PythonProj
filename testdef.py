listangka = []
ganjil = 0
genap = 0
while True:
 angka = int(input("Masukkan angka: "))
 listangka.append(angka)
 P1 = input("selesai? ketik Ya untuk setuju dan Enter untuk melanjutkan ")
 if P1 == "Ya":
   for i in listangka:
     if not i %2:
       genap+=1
     else:
       ganjil+=1
   print("Total angka genap: ", genap)
   print("Total angka ganjil: ", ganjil)
   break
 else:
   angka
