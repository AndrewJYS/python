a: list = [1,2,3,4]


try:
    it = a.__iter__()
    while True:
        item = it.__next__()
        print(item, end=' ')
except StopIteration:
    print()
    pass


try:
    it = iter(a)
    while True:
        item = next(it)
        print(item, end=' ')
except StopIteration:
    print()
    pass


for item in a:
    print(item, end=' ')


try:
    it = a.__reversed__()
    while True:
        item = it.__next__()
        print(item, end=' ')
except StopIteration:
    print()
    pass


try:
    it = reversed(a)
    while True:
        item = next(it)
        print(item, end=' ')
except StopIteration:
    print()
    pass


for item in reversed(a):
    print(item, end=' ')