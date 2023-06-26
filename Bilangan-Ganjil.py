# Bilangan_Ganjil?
# Fa'iq Ali Sutiono - IF-A
# 1152100040
def inputan():
    N1 = float(input("masukkan angka: "))
    pembagi = 2

    if N1 % pembagi > 0:
        print("Bilangan Ganjil")
        pertanyaan()
    else:
        print("Bilangan Genap")
        pertanyaan()


def pertanyaan():
    Q1 = input("Ada lagi?: (Ya/Tidak)")
    if Q1 == "Ya":
        inputan()
    else:
        print("Terima kasih")


inputan()
