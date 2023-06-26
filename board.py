board = [
    ["A", "B", "C", "D"],
    ['C', 'F', 'S', 'S'],
    ['A', 'D', 'E', 'E']
]


def quests(arr, word):
    total = len(arr)
    list = []
    for i in word:
        list.append(i)
    for i in arr:
        for j in i:
            for k in range(0, total):
                if j in list:
                    try:
                        i.remove(j)
                        list.remove(j)
                    except:
                        print("false")

    if len(list) == 0:
        print("True")


quests(board, "SEE`E")
