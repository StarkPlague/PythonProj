def index2d(i):
    for j, k in enumerate(l):
        if k.nama == i:
            return j
    return -1


l = [["e", 2]]

a = l[index2d(2)]
print(a)
