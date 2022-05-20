def myfunc(*args, **kwargs):
    if args:
        for a in args:
            print(a, end=' ')
    if kwargs:
        for k, v in kwargs.items():
            print(k, v, sep='->', end=' ')
    print()

myfunc() #
myfunc(1, 2, 3) # 1 2 3
myfunc(1, 2, 3, a=10, b=20, c=30) # 1 2 3 a->10 b->20 c->30