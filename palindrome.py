word = input()
arr_word = []
reversed_word = []

for i in word:
    arr_word.append(i)

for j in reversed(arr_word):
    reversed_word.append(j)


def check():
    sama = False
    for i in range(0, len(arr_word)):
        index = 0
        if arr_word[index] != reversed_word[index]:
            break
        else:
            index += 1
            sama = True
    return sama


print(check())
