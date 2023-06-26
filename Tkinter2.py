from msilib.schema import RadioButton
from tkinter import *

root = Tk()
root.title("Aplikasi Kurir")
root.geometry("500x500")


def hitung():
    if radioJenis.get() == "r":
        harga = reguler*int(inputBerat.get())*int(inputJarak.get())
        if radioAsuransi.get() == "y":
            asuransi = 0.05*harga
            harga = harga + asuransi
        else:
            asuransi = 0

    else:
        harga = express*int(inputBerat.get())*int(inputJarak.get())
        if radioAsuransi.get() == "y":
            asuransi = 0.05*harga
            harga = harga + asuransi
        else:
            asuransi = 0

    lblHasil = Label(root, text=f'''
                     ____________________ TOTAL PERHITUNGAN ____________________
                     Nama : {inputNama.get()}
                     Jarak : {inputJarak.get()}
                     Berat : {inputBerat.get()}
                     Jenis : {radioJenis.get()}
                     Asuransi : {radioAsuransi.get()}
                     Total harga : {harga}''')
    lblHasil.grid(column=0, row=7)


reguler = 9000
express = 18000

lblNama = Label(root, text="Nama Pengirim: ")
lblJarak = Label(root, text="Jarak Pengiriman: ")
lblBerat = Label(root, text="Berat Barang: ")
lblJenis = Label(root, text="Jenis pengiriman: ")
lblAsuransi = Label(root, text="Asuransi: ")

lblNama.grid(column=0, row=1)
lblJarak.grid(column=0, row=2)
lblBerat.grid(column=0, row=3)
lblJenis.grid(column=0, row=4)
lblAsuransi.grid(column=0, row=5)

inputNama = Entry(root, width=10)
inputJarak = Entry(root, width=10)
inputBerat = Entry(root, width=10)

inputNama.grid(column=1, row=1)
inputJarak.grid(column=1, row=2)
inputBerat.grid(column=1, row=3)

radioJenis = StringVar()
radioJenis1 = Radiobutton(root, value="r",
                          variable=radioJenis, text="reguler")

radioJenis2 = Radiobutton(root, value="e",
                          variable=radioJenis, text="express")

radioJenis1.grid(column=1, row=4)
radioJenis2.grid(column=2, row=4)

radioAsuransi = StringVar()

radioAsuransi1 = Radiobutton(root, value="y",
                             variable=radioAsuransi, text="Ya")

radioAsuransi2 = Radiobutton(root, value="t",
                             variable=radioAsuransi, text="Tidak")

radioAsuransi1.grid(column=1, row=5)
radioAsuransi2.grid(column=2, row=5)

btn = Button(root, text="Hitung", command=hitung)
btn.grid(column=1, row=6)

root.mainloop()
