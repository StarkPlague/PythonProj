# 1.0 dictionary
e = dict()
e["indo"] = "jakarta"

# 1.1 untuk print value
for i in e.values():
    print(i)

# 1.2 untuk print key
for i in e.keys():
    print(i)

f = ("budi", "layi")

# 2.0 konversi tupple ke list
a = []

for i in f:
    a.append(i)
print(a)


# 3.0 sett (tidak bisa duplikat item)
z = set()


z.add("meja")
z.add("meja")  # duplikat
z.add("kursi")

print(z)
