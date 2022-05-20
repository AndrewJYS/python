from itertools import permutations, combinations, combinations_with_replacement

a = [1,2,2]
for p in permutations(a):
    print(p)

for c in combinations(a, 2):
    print(c)

for cr in combinations_with_replacement(a, 3):
    print(cr)