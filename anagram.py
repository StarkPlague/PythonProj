from itertools import combinations, permutations

# Mendapatkan semua permutasi dari [1, 2, 3]
perm = combinations([3, 3, 1])
comb = []
# Print semua permutasi
for i in perm:
    comb.append(i)
    print(i)


print(comb)
