file = open("run.txt", "r")


class run():
    def __init__(self, data):
        self.data = data


run_ = run(file.readline())
print(run_.data)
