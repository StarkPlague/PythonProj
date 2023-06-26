hero_ = []


class heroItem:
    def __init__(self, n, att, it):
        self.nama = n
        self.attack = att
        self.item = it


def index2dspec(i):
    for j, k in enumerate(herospec):
        if k.nama == i:
            return j
    return -1


x = 2
while x > 0:
    n = input()
    att = input()
    i = input()
    hero_.append(heroItem(n, att, i))
    x -= 1
    if x == 0:
        break
print(hero_)
