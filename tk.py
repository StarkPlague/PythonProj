from tkinter import *
from tkinter.font import *

root = Tk()

# Mengubah background
root.config(background="dark red")

gantifont = Font(font="Normal 20", family="Roboto")

label = Label(text="Info gan", font=gantifont,
              background="dark red", fg="white")

root.geometry("500x500")
label.pack()

label.grid(row=0, column=0)

# Entri digunakan untuk menginput sebuah data

data = Entry(font="Normal 20", bd=10)
data.grid


def perintah():
    print(data.get())

    data.delete


button = Button(text="pencet", font="Normal 10",
                activebackground="green", command=perintah)

button.grid(row=1, column=1)

teks = Text(width=20, height=20, bd=10, font=gantifont)

teks.grid(row=2, column=2)

root.mainloop()
