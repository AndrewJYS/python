# 迭代器和生成器  

## 可迭代对象  

大多数情况下，我们会用for语句访问可迭代对象的元素，但是，如果要对底层迭代机制做更精细的控制，可以调用可迭代对象的\_\_iter()\_\_函数，获取迭代器对象，然后对迭代器对象使用\_\_next()\_\_函数逐一获取元素。下面三个代码段的作用相同。  

```python
a: list = [1,2,3,4]
try:
    it = a.__iter__()
    while True:
        item = it.__next__()
        print(item, end=' ')
except StopIteration:
    print()
    pass
```

```python
a: list = [1,2,3,4]
try:
    it = iter(a)
    while True:
        item = next(it)
        print(item, end=' ')
except StopIteration:
    print()
    pass
```

```python
a: list = [1,2,3,4]
for item in a:
    print(item, end=' ')
```

### 反向迭代  

调用reversed()内置函数会返回反向的迭代器对象，用法与iter相同。下面三个代码段的作用相同。  

```python
a: list = [1,2,3,4]
try:
    it = a.__reversed__()
    while True:
        item = it.__next__()
        print(item, end=' ')
except StopIteration:
    print()
    pass
```

```python
a: list = [1,2,3,4]
try:
    it = reversed(a)
    while True:
        item = next(it)
        print(item, end=' ')
except StopIteration:
    print()
    pass
```

```python
for item in reversed(a):
    print(item, end=' ')
```

## 用生成器创建迭代模式  

使用生成函数可以创建新的迭代模式  

**注意：**
**调用生成函数会返回迭代器对象**  

```python
def countdowm(n):
    while n > 0:
        yield n
        n -= 1

c = countdowm(3) # <generator object countdowm at 0x000001D1ABF8DD60>
print(c)
print(next(c)) # 3
print(next(c)) # 2
print(next(c)) # 1

c = countdowm(3)
for item in c:
    print(item, end=' ') # 3 2 1 
```

**注意：**  
**使用生成器函数，可以实现管道机制。这样，调用生成器函数时返回一个迭代器，我们对迭代器操作，每一次从生成器管道中提取一份数据，内存只需开辟一份数据的空间，尤其是在处理大批量数据时不会占用过多的内存**  

## 构建自定义容器的迭代方式  

假设我们自定义了一个容器，容器内部包含了某种可迭代对象，现在要根据这个可迭代对象定义容器的迭代行为。我们应该重载容器对象的\_\_iter()\_\_方法。  

**注意：**  
**Python 的迭代协议要求\_\_iter\_\_()返回一个特殊的迭代器对象，由该对象实现的\_\_next\_\_()方法来完成实际的迭代。**  

```python
class Node:
    def __init__(self, value):
        self._value = value
        self._children = []
    
    def __iter__(self):
        return iter(self._children)
    
    def add_child(self, node):
        self._children.append(node)

root = Node(0)
# 省略初始化其他子节点的代码
for c in root:
    #会迭代root对象的_children中的元素
```

### 利用自定义__iter__()构建新的迭代模式  

利用定义好的容器迭代方式，可以封装更复杂的迭代方式，比如定义节点的深度遍历模式  

```python
class Node:
    # 省略重复代码
    def depth_first(self):
        yield self
        for c in self:
            yield from c.depth_first()
    
root = Node(0)
# 省略初始化其他子节点的代码

for ch in root.depth_first():
    print(ch) # 打印深度优先遍历序列
```

## 对迭代器切片  

### itertools.islice()

使用itertools.islice()对迭代器对象进行切片，这个函数会返回一个新的迭代器对象，它可以产生的新的需要的元素。  

```python
import itertools

def count(n):
    while True:
        yield n
        n += 1

c = count(4)
for x in itertools.islice(c, 10, 15):
    print(x, end=' ') # 14 15 16 17 18 
```

### 跳过可迭代对象的前一部分元素  

可以使用itertools.dropwhile()函数。要使用它，只要提供一个函数和一个可迭代对象即可。该函数返回的迭代器会丢**弃掉序列中的前面几个元素**，只要它们在所提供的函数中返回True 即可。**这之后，序列中剩余的全部元素都会产生出来。**  

```python
a = ['apple', 'array', 'banana', 'cherry', 'axis']
for w in itertools.dropwhile(lambda word: word.startswith('a'), a):
    print(w, end=' ') # banana cherry axis 
```

## 同时迭代多个序列  

### zip用作“并行迭代”  

使用zip函数：zip(a, b)的工作原理是创建出一个迭代器，该迭代器可产生出元组(x, y)，这里的x 取自序列a，而y 取自序列b。当其中某个输入序列中没有元素可以继续迭代时，整个迭代过程结束。  

```python
a = [1,2,3,4]
b = [2,3,4,5]
for x, y in zip(a,b):
    print(x, y, end='    ') # 1 2    2 3    3 4    4 5    
```

zip()可以接受多于2 个序列作为输入  

**注意：**  
**zip()创建出的结果只是一个迭代器。如果需要将配对的数据保存为列表，那么请使用list()函数**  

### chain用作“串行迭代”  

```python
from itertools import chain
for x in chain(a, b, c):
    print(x, end=' ') # 1 2 3 4 2 3 4 5 3 4 5 6 
```

## 参考  

Python Cookbook, Chapter 4  
