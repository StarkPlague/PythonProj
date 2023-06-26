import operator
d = {1: 2,3: 4,4: 3,2: 1, 0: 0}
print("Original Dictionary: ",d)
sorted_d = dict(sorted(d.items(), key=operator.itemgetter(1)))
print("kecil ke terbesar: ", sorted_d)
sorted_d = dict(sorted(d.items(), key=operator.itemgetter(1),reverse=True))
print('Dictionary in descending order by value : ',sorted_d)