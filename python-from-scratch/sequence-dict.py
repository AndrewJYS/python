dictionary: dict = {'num1': 1, 'num2': 2}
print(dictionary)  # {'num1': 1, 'num2': 2}

a: list = ['num1', 'num2', 'num3']
b: list = [1,2,3]
dictionary: dict = dict(zip(a, b))
print(dictionary) # {'num1': 1, 'num2': 2, 'num3': 3}


dictionary: dict = dict(num1=1, num2=2)
print(dictionary) # {'num1': 1, 'num2': 2}


dictionary: dict = {'num1': 1, 'num2': 2}
print(dictionary['num1']) # 1
print(dictionary['num3'] if '' in dictionary else 'not found') # not found
print(dictionary.get('num1')) # 1
print(dictionary.get('num3')) # None
print(dictionary.get('num3', 'not found')) # not found

dictionary: dict = {'num1': 1, 'num2': 2, 'num3': 3}
for kv in dictionary:
    print(kv)
'''
num1
num2
num3
'''

dictionary: dict = {'num1': 1, 'num2': 2, 'num3': 3}
for item in dictionary.items():
    print(item)
'''
('num1', 1)
('num2', 2)
('num3', 3)
'''

dictionary: dict = {'num1': 1, 'num2': 2, 'num3': 3}
for key, value in dictionary.items():
    print(key, value)
'''
num1 1
num2 2
num3 3
'''

dictionary = {'e': 2, 'a': 1, 'i': 0, 'o': 6, 'u': 0}
for k, v in dictionary.items():
    print(k, v)
'''
e 2
a 1
i 0
o 6
u 0
'''

dictionary = {'e': 2, 'a': 1, 'i': 0, 'o': 6, 'u': 0}
for k, v in sorted(dictionary.items()):
    print(k, v)
'''
a 1
e 2
i 0
o 6
u 0
'''

dictionary: dict = {'num1': 1, 'num2': 2, 'num3': 3}
dictionary['num4'] = 4
print(dictionary) # {'num1': 1, 'num2': 2, 'num3': 3, 'num4': 4}

dictionary: dict = {'num1': 1, 'num2': 2, 'num3': 3}
del dictionary['num2']
print(dictionary) # {'num1': 1, 'num3': 3}

import random
dictionary = {"num"+str(i):random.randint(10, 100) for i in range(1, 5)}
print(dictionary) # {'num1': 49, 'num2': 64, 'num3': 78, 'num4': 97}

dictionary: dict = {'num1': 1, 'num2': 2, 'num3': 3}
del dictionary

dictionary: dict = {'num1': 1, 'num2': 2, 'num3': 3}
dictionary.clear()
print(dictionary) # {}