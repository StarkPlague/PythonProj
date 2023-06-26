def split(word):
    return[char for char in word]

word = input("Masukkan kode: ").lower()
word2 = split(word)
al = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
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
    elif z  > 122:
        eq = z - 122
        a = al[eq-1]
        hasil.append(a)

print("".join([str(h) for h in hasil]))
        

        




    
    