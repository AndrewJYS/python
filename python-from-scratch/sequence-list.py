a = list([1,2,3,4])
print(a) # [1, 2, 3, 4]

a: list = [1,2,3,4,5]
print(a[:])  # [1, 2, 3, 4, 5]
print(a[0:3]) # [1, 2, 3]
print(a[0:5:2]) # [1, 3, 5]
print(a[:3]) # [1, 2, 3]
print(a[::2]) # [1, 3, 5]
print(a[::-1]) # [5, 4, 3, 2, 1]

a: list = [1,2,3,4,5]
b: list = ['2',4,6,'8',10]
print(a + b) # [1, 2, 3, 4, 5, '2', 4, 6, '8', 10]

a: list = [1,2,3]
print(a * 3) # [1, 2, 3, 1, 2, 3, 1, 2, 3]
b: list = [None]
print(b * 4) # [None, None, None, None]

b: list = ['2',4,6,'8',10]
print('8' in b) # True
print(2 in b) # False

a: list = [1,5,7,3,9]
print(len(a)) # 5
print(max(a)) # 9
print(min(a)) # 1
b = sorted(a)
print(b) # [1, 3, 5, 7, 9]
a.reverse()
c = a
print(c) # [9, 3, 7, 5, 1]
num: list = [2,3,3,3]
print(num.count(3)) # 3


a = list(range(0, 20, 2))
print(a) # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

a: list = ["num1", "num2", "num3"]
for i, name in enumerate(a):
    print(i, name)

a: list = [1,2,3]
b: list = [5,6,7]
a.append(4)
print(a) # [1, 2, 3, 4]
a.extend(b)
print(a) # [1, 2, 3, 4, 5, 6, 7]
a.insert(1, 29)
print(a) # [1, 29, 2, 3, 4, 5, 6, 7]


a:list = [1,2,3,6,3,3]
del a[-1]
print(a) # [1, 2, 3, 6, 3]
a.remove(3)
print(a) # [1, 2, 6, 3]
a.pop(2)
print(a) # [1, 2, 3]
a.pop()
print(a) # [1, 2]


a:list = [1,2,3,6,3,3]
print(a.index(3)) # 2

a:list = [1,2,3,6,3,3]
a.sort(reverse=True)
print(a) # [6, 3, 3, 3, 2, 1]
a.sort()
print(a) # [1, 2, 3, 3, 3, 6]

a: list = ['cat', 'Tom', 'Angela', 'pet']
a.sort(key=str.lower) # 排序时不区分大小写
print(a) # ['Angela', 'cat', 'pet', 'Tom']
a.sort()  # 排序时区分大小写
print(a) # ['Angela', 'Tom', 'cat', 'pet']

a: list = [1,5,7,3,9]
b = sorted(a)
print(a) # [1, 5, 7, 3, 9]
print(b) # [1, 3, 5, 7, 9]

c = sorted(a, reverse=True)
print(c) # [9, 7, 5, 3, 1]

import random
a: list = [random.randint(10, 100) for i in range(10)]
print(a) # [67, 22, 74, 43, 100, 42, 16, 35, 20, 39]

a: list = [1,5,7,3,9]
newlist = [float(i*0.5) for i in a]
print(newlist) # [0.5, 2.5, 3.5, 1.5, 4.5]

a: list = [1,5,7,3,9]
newlist = [float(i*0.5) for i in a if i >= 3]
print(newlist) # [2.5, 3.5, 1.5, 4.5]


a: list = []
for i in range(3):
    a.append([])
    for j in range(5):
        a[i].append(j)
print(a) # [[0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4]]

a: list = [[j for j in range(5)] for i in range(3)]
print(a) # [[0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4]]


a = [1,2,3,4,5,6]
a.extend([a.pop(), a.pop()])
print(a) # [1, 2, 3, 4, 6, 5]

a.insert(1, a.pop(3))
print(a) # [1, 4, 2, 3, 6, 5]

a = [1,2,3,4,5]
b = a
a.append(6)
print(b) # [1, 2, 3, 4, 5, 6]

a = [1,2,3,4,5]
b = a.copy()
a.append(6)
b.append(7)
print(a) # [1, 2, 3, 4, 5, 6]
print(b) # [1, 2, 3, 4, 5, 7]