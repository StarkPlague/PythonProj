f = open("data siswa.txt", "w")
nama = input("Masukkan nama: ")
f.write("Data mahasiswa" + "\n" + nama)
f.close()