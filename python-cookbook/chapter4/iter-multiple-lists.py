a = [1,2,3,4]
b = [2,3,4,5]
c = [3,4,5,6]
for x, y in zip(a,b):
    print(x, y, end='    ') # 1 2    2 3    3 4    4 5

from itertools import chain
for x in chain(a, b, c):
    print(x, end=' ') # 1 2 3 4 2 3 4 5 3 4 5 6