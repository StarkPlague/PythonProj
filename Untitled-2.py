def input_matrix(panjang, lebar):
    matrix = []

    for x in range(panjang):
        matrix.append([])

        for y in range(lebar):
            deskripsi = "Masukkan angka matrix baris {} kolom {}: ".format(x+1, y+1)
            angka = int(input(deskripsi))
            matrix[x].append(angka)

    return matrix

def pertambahan_matrix(mat_a, mat_b):
    if len(mat_a) != len(mat_b) or len(mat_a[0]) != len(mat_b[0]):
        raise RuntimeError ("ordo matrix tidak sama")

    hasil = []
    for baris in range(len(mat_a)):
        hasil.append([])
        for kolom in range(len(mat_a[0])):
            hasil[baris].append(mat_a[baris][kolom] + mat_b[baris][kolom])
            
    return hasil

def print_matrix(matrix):
    for baris in matrix:
        for kolom in baris:
            print(("{:4}").format(kolom), end="")
        print()

print('Program pertambahan matrix')
h = int(input('Masukkan banyak baris: '))
w = int(input('Masukkan banyak kolom: '))

mat_a = input_matrix(h, w)
print('Matrix A:')
print_matrix(mat_a)

mat_b = input_matrix(h, w)
print('Matrix B:')
print_matrix(mat_b)

hasil = pertambahan_matrix(mat_a, mat_b)
if hasil != None:
    print('Matrix hasil:')
    print_matrix(hasil)



