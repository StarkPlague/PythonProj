def split(word):
    return[char for char in word]

word = input("Masukkan kode: ")
word2 = split(word)
al = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
al2 = [ord(r) for r in al]
Al = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
Al2 = [ord(s) for s in Al]
asciii = [ord(x) for x in word2]
angka = []
huruf = []
angka2 = []
hasil = []

for x in asciii[:len(asciii)]:
    if 48 <= x <= 57:
        angka.append(chr(x))
    else:
        huruf.append(chr(x))
for i in angka:
    angka2.append(int(i))
for x in huruf:
    o_huruf = [ord(x) for x in huruf]
for y in o_huruf:
    tot = [y+sum(angka2) for y in o_huruf]
for z in tot:
    if 97 <= z <= 122:
        hasil.append(chr(z))
    elif 65 <= z <= 90:
        hasil.append(chr(z))
    elif z > 122:
        eq = z - 122
        a = Al[eq-1]
        hasil.append(a)
    elif z > 90:
        eq = z - 90
        a = al[eq-1]
        hasil.append(a)
        print(eq)
        print(a)
        
print("".join([str(h) for h in hasil]))

#mohon maaf pak ada bug yang tidak sempat saya selesaikan karena hal lain dan deadline
#bug terdapat pada line 35 yang mengganggu line 26
#jika eq pada line 35 > 97 maka value nya kembali ke ascii lowercase

        




    
    
