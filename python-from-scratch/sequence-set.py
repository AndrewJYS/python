a: set = set([1,3,3,4])
print(a) # {1, 3, 4}

a = set('aeioooouuu')
print(a) # {'i', 'e', 'a', 'o', 'u'}


a: set = set([1,3,3,4])
a.add(5)
print(a) # {1, 3, 4, 5}


a: set = set([1,3,3,4])
a.remove(3)
print(a) # {1, 4}

a: set = set([1,3,4])
b: set = set([1,5,6])
c = a | b
print(c) # {1, 3, 4, 5, 6}
print(a & b) # {1}
print(a - b) # {3, 4}

a: set = set([1,3,4])
b: set = set([1,5,6])
a.union(b)
print(a) # {1, 3, 4}
print(a.difference(b)) # {3, 4}
print(a.intersection(b)) #{1}