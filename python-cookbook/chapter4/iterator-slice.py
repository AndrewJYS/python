import itertools

def count(n):
    while True:
        yield n
        n += 1

c = count(4)
for x in itertools.islice(c, 10, 15):
    print(x, end=' ') # 14 15 16 17 18


a = ['apple', 'array', 'banana', 'cherry', 'axis']
for w in itertools.dropwhile(lambda word: word.startswith('a'), a):
    print(w, end=' ') # banana cherry axis