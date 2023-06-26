
word = input()
index = int(input())
arr_word = []
arr_index = []


for i in word:  # Mengisi array dengan kata yang dipecah dari word
    arr_word.append(i)

for j in range(0, index):
    # Menambahkan kata yang di potong ke array index
    arr_index.append(arr_word[j])

arr_word.extend(arr_index)
for k in range(0, index):
    del arr_word[0]
print(arr_word)
