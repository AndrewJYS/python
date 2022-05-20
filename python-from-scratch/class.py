class Numbers:
    cnt = 0;
    def __init__(self):
        Numbers.cnt += 1
        self.count = 0
        self.count += 1

list = []
for i in range(4):
    list.append(Numbers())
print(Numbers.cnt) # 4
print(list[3].count) # 1