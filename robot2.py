rw = []
r = int(input("Masukkan Row: "))


for i in range(r):
    isi = input()
    rw.append(isi)
print(rw)

kolom = len(rw[0])
for row in rw:
    print(" ".join(row))
    
New_Cord = []
for i in rw:
    rw.append(i)
rw.reverse()

print(rw)