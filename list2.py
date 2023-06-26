
todo = []
def add():
    t = input("Masukkan item:")
    todo.append(t)
def show():
    angka = 1
    for i in todo:
        print(angka, ".", i)
        angka += 1

def hps():
    u = str(input("masukkan item yang mau dihapus: "))
    todo.remove(u)

while True:
    print('To Do List')
    print('1. Lihat to do List')
    print('2. Tambah list')
    print('3. Hapus list')
    print('4. Keluar')
    
    choose = int(input())

    if choose == 1:
        show()
    elif choose == 2:
        add()
    elif choose == 3:
        hps()
    else:
        break


