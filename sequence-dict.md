# 字典  

**注意：**  
字典的键必须初始化，下述程序会报错  

```python
fruit = {}
fruit['e'] += 1
```

## 字典的创建和删除  

(1) 创建空字典  

```python
dictionary = {}
dictionary = dict()
```

(2)基本语法  

```python
dictionary = {key1: value1, key2: value2, ... , keyn: valuen}
```

```python
dictionary = {'num1': 1, 'num2': 2}
print(dictionary)  # {'num1': 1, 'num2': 2}
```

(3)通过映射函数创建字典  

```python
dictionary = dict(zip(list1, list2))
```

```python
a: list = ['num1', 'num2', 'num3']
b: list = [1,2,3]
dictionary = dict(zip(a, b))
print(dictionary) # {'num1': 1, 'num2': 2, 'num3': 3}
```

(4)给定键值对创建字典  

```python
dictionary = dict(key1=value1, key2=value2, ... , keyn=valuen)
```

```python
dictionary = dict(num1=1, num2=2)
print(dictionary) # {'num1': 1, 'num2': 2}
```

(5)使用字典推导式  

```python
import random
dictionary = {"num"+str(i):random.randint(10, 100) for i in range(1, 5)}
print(dictionary) # {'num1': 49, 'num2': 64, 'num3': 78, 'num4': 97}
```

(6) setdefault方法  

下述语句  

```python
found.setdefault(letter, 0)
found[letter] += 1
```

相当于  

```python
if letter not in found:
    found[letter] = 0
found[letter] += 1
```

## 通过键值访问字典  

```python
dictionary: dict = {'num1': 1, 'num2': 2}
print(dictionary['num1']) # 1
print(dictionary['num3'] if '' in dictionary else 'not found') # not found
print(dictionary.get('num1')) # 1
print(dictionary.get('num3')) # None
print(dictionary.get('num3', 'not found')) # not found
```

对比C++  

**注意：**  
**cout << a["num3"] << endl;实际上会为a["num3"]赋值，所以之后a.find("num3")不会返回a.end()，而如果先运行a.find("num3")，则不会为a["num3"]赋值**  

```c++
unordered_map<string, int> a;
a["num1"] = 1;
a.emplace("num2", 2);

cout << a["num1"] << endl; //output 1
cout << a["num3"] << endl; //output 0

cout << (a.find("num1") != a.end()? "found" : "not found") << endl; //found
cout << (a.find("num3") != a.end()? "found" : "not found") << endl; //found
cout << (a.find("3") != a.end()? "found" : "not found") << endl; //not found
cout << (a.find("3") != a.end()? "found" : "not found") << endl; //not found
```

## 遍历字典  

```python
dictionary: dict = {'num1': 1, 'num2': 2, 'num3': 3}
for kv in dictionary:
    print(kv)
'''
用for循环处理一个字典时，解释器只会处理字典的键
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
```

还可以指定输出时的字典顺序  

```python
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
```

## 添加，删除字典元素  

```python
dictionary: dict = {'num1': 1, 'num2': 2, 'num3': 3}
dictionary['num4'] = 4
print(dictionary) # {'num1': 1, 'num2': 2, 'num3': 3, 'num4': 4}
```

```python
dictionary: dict = {'num1': 1, 'num2': 2, 'num3': 3}
del dictionary['num2']
print(dictionary) # {'num1': 1, 'num3': 3}
```

对比C++，删除某个含有key的元素  

```c++
a.erase("num2");
cout << (a.find("num2") != a.end()? "found" : "not found") << endl; //not found
```

## 删除字典  

将定义的字典删除  

```python
dictionary: dict = {'num1': 1, 'num2': 2, 'num3': 3}
del dictionary
```

将字典中的元素全部删除，会返回空字典  

```python
dictionary: dict = {'num1': 1, 'num2': 2, 'num3': 3}
dictionary.clear()
print(dictionary) # {}
```

对比C++，将字典中的元素全部删除，会返回空字典  

```c++
unordered_map<string, int> a;
a["num1"] = 1;
a.emplace("num2", 2);
a.clear();
cout << (a.empty()? "True" : "False") << endl; // True
```

## 参考  

Head First Python Chapter 3  
零基础学Python Chapter 4  
挑战程序设计竞赛-2：算法和数据结构（第1版）  Chapter 9  
