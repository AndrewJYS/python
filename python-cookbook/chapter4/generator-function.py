def countdowm(n):
    while n > 0:
        yield n
        n -= 1

c = countdowm(3) # <generator object countdowm at 0x000001D1ABF8DD60>
print(c)
print(next(c)) # 3
print(next(c)) # 2
print(next(c)) # 1
# print(next(c))


c = countdowm(3)
for item in c:
    print(item, end=' ') # 3 2 1

