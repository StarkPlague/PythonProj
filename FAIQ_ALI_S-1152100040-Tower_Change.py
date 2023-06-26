import math

print(".: Tower Change Taman Firdaus :.")

kata =  input("Masukkan kata: " )
char = list(kata)
a = [ord(x) for x in char]
b = []

for x in a[:len(a)]:
    if 65 <= x <= 90:
        b.append(3)
    elif 97 <= x <= 122:
        b.append(1)
    else:
        b.append(2)

hitung = sum(b)/math.pi
h = print("Anda membutuhkan lebar lahan minimal: ", round(hitung), "Tiles")


