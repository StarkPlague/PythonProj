# NAMA: Fa'iq Ali Sutiono
#NRP: 1152100040
# UAS


from re import L
from pandas import *


def index_2d(myList, v):
    for i, x in enumerate(myList):
        if v in x:
            return (i, x.index(v))


def find(l, elem):
    for row, i in enumerate(l):
        try:
            column = i.index(elem)
        except ValueError:
            continue
        return row, column
    return -1


ghokemon = []
wall = -1
r, c, g, t = input().split()
Map = []
arah = "ka"
for i in range(int(r)):
    isi_String = input()
    isi_Map = isi_String.split()
    Map.append(isi_Map)

ghok = [int(i) for i in g]
tr = [int(i) for i in t]
a = []
gk_data = []
t = []

for i in range(ghok[0]):
    rwcl = []
    rw, cl, gk, tp, st = input().split()
    rwcl.append([int(rw), int(cl)])
    rwcl.append([gk, tp, st])
    gk_data.append(rwcl)
for i in range(tr[0]):
    rw, cl, tp = input().split()
    t.append([int(rw), int(cl)])  # ind 0
    t.append([cl, tp])  # ind 1
print(DataFrame(gk_data))
print(DataFrame(Map))
print(gk_data)
print(t)

mov = input("Masukkan perintah: ")
x_ = find(Map, "L")
newpos_ = list(x_)
print(newpos_)
while newpos_[0] > 0:
    x = find(Map, "L")
    newpos = list(x)
    if newpos[0] < 0:
        break
    Map[newpos[0]][newpos[1]] = "."
    newpos[0] = newpos[0] - 1
    if newpos[0] < 0:
        newpos[1] = newpos[1] - 1
        Map[newpos[0]][newpos[1]] = "L"
    elif Map[newpos[0]][newpos[1]] == "?":
        print("prioritas arah berubah")
        if arah == "ka":
            arah = "ki"
        elif arah == "ki":
            arah = "ka"
        newpos[0] = newpos[0] + 1
        Map[newpos[0]][newpos[1]] = "L"
    elif Map[newpos[0]][newpos[1]] == "T":
        if len(ghokemon) > 0:
            print("BATTLE", ghokemon[0])
            ghokemon.remove(ghokemon[0])
        else:
            print("NO BATTLE")
            break
        newpos[0] = newpos[0] + 1
        Map[newpos[0]][newpos[1]] = "L"
    else:
        Map[newpos[0]][newpos[1]] = "L"
        l = find(Map, "L")
        newpos_ = list(l)
        y = list(find(gk_data, newpos_))
        print(gk_data[y[0]][1])
        print(DataFrame(Map))
        ghokemon.append(gk_data[y[0]][1])

# Mohon maaf atas kekuarangan nya.
