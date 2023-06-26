f = open("tes.txt", "w")
pesan = input("Masukkan kata: ")
f.write(pesan)
f.close()

f1 = open("tes.txt", "r")
print(f1.read())
f1.close()

f2 = open("tes.txt", "a")
f2.write("{}\n".format(pesan))
f2.close()