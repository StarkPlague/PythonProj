# Diamond Problem
class A:
    def show(self):
        print("Ini kelas A")


class B(A):
    def show(self):
        print("Ini kelas B")


class C(A):
    def show(self):
        print("Ini kelas C")


class D(B, C, A):
    pass


d = D()
d.show()
