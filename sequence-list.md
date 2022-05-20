# 序列  

python中，序列主要有列表、集合、元组、字典、字符串  

## 序列基本用法  

这里以list为例  

### 切片  

语法：list_name[start: end: step]

```python
a: list = [1,2,3,4,5]
print(a[:])  # [1, 2, 3, 4, 5]
print(a[0:3]) # [1, 2, 3]
print(a[0:5:2]) # [1, 3, 5]
print(a[:3]) # [1, 2, 3]
print(a[::2]) # [1, 3, 5] 每两个选择一个
print(a[::-1]) # [5, 4, 3, 2, 1]
```

### 序列相加  

相同类型的序列可以相加，序列中的元素可以不同  

```python
a: list = [1,2,3,4,5]
b: list = ['2',4,6,'8',10]
print(a + b) # [1, 2, 3, 4, 5, '2', 4, 6, '8', 10]
```

### 乘法  

使用数字n乘以一个序列会生成新的序列。新序列的内容为原来序列被重复n次的结果

```python
a: list = [1,2,3]
print(a * 3) # [1, 2, 3, 1, 2, 3, 1, 2, 3]
b: list = [None]
print(b * 4) # [None, None, None, None]
```

### 检查某个元素是否在序列中  

语法：value in sequence

```python
b: list = ['2',4,6,'8',10]
print('8' in b) # True
print(2 in b) # False
```

### 其他基本函数  

```python
a: list = [1,5,7,3,9]
num: list = [2,3,3,3]
```

|函数|作用|例子|输出|
:-:|:-:|:-:|:-:
|len()|计算序列长度|```print(len(a))```|5|
|max()|计算序列最大值|```print(max(a))```|9|
|min()|计算序列最小值|```print(min(a))```|1|
|reverse()|序列逆序|```a.reverse()```<br>```c = a```<br>```print(c)```|[9, 7, 5, 3, 1]|
|count()|指定元素出现的次数|print(num.count(3))|3|

## 列表（list）  

**注意：**  
**列表中的元素类型可以不同**  

### 创建列表  

```python
a = list([1,2,3,4])
print(a) # [1, 2, 3, 4]
```

```python
a = list(range(0, 20, 2))
print(a)
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
```

也可以使用列表推导式生成列表  
(1)生成指定范围的数值列表  

```python
list = [expression for var in range]
```

```python
import random
a: list = [random.randint(10, 100) for i in range(10)]
print(a) # [67, 22, 74, 43, 100, 42, 16, 35, 20, 39]
```

（2）根据已有列表生成指定要求的列表  

```python
newlist = [expression for var in list]
```

```pyhton
a: list = [1,5,7,3,9]
newlist = [float(i*0.5) for i in a]
print(newlist) # [0.5, 2.5, 3.5, 1.5, 4.5]
```

(3)从列表中选出符合条件的元素组成新的列表  

```python
newlist = [expression for var in list if condition]
```

```python
a: list = [1,5,7,3,9]
newlist = [float(i*0.5) for i in a if i >= 3]
print(newlist) # [2.5, 3.5, 1.5, 4.5]
```

### 创建二维列表  

(1)使用嵌套循环  

```python
a: list = []
for i in range(3):
    a.append([])
    for j in range(5):
        a[i].append(j)

print(a) # [[0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4]]
```

(2)使用推导式  

```python
a: list = [[j for j in range(5)] for i in range(3)]
print(a) # [[0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4]]
```

### 删除列表  

```python
a = list(range(0, 20, 2))
del a
```

### 遍历列表  

使用for循环和enumerate()函数可以实现同时输出索引值和元素内容，语法如下：  

```python
for index, item in enumerate(listname):
    # for statements
```

```python
a: list = ["num1", "num2", "num3"]
for i, name in enumerate(a):
    print(i, name)

'''
0 num1
1 num2
2 num3
'''
```

### 添加元素  

```python
a: list = [1,2,3]
b: list = [5,6,7]

# 末尾添加一个元素 
a.append(4)
print(a) # [1, 2, 3, 4]

# 列表末尾添加一个列表
a.extend(b)
print(a) # [1, 2, 3, 4, 5, 6, 7]

# 在特定位置插入元素  
a.insert(1, 29)
print(a) # [1, 29, 2, 3, 4, 5, 6, 7]
```

### 删除元素  

删除元素前最好判断该元素是否存在  

```python
a:list = [1,2,3,6,3,3]

# 按照索引删除
del a[-1]
print(a) # [1, 2, 3, 6, 3]

# 按照元素值删除
a.remove(3)  # 删除第一个3
print(a) # [1, 2, 6, 3]

# 用pop按照索引删除
a.pop(2)
print(a) # [1, 2, 3]

# 删除末尾的值
a.pop()
print(a) # [1, 2]
```

### 获取元素首次出现的下标  

```python
a:list = [1,2,3,6,3,3]
print(a.index(3)) # 2
```

### 对列表排序  

```python
a:list = [1,2,3,6,3,3]
a.sort(reverse=True)
print(a) # [6, 3, 3, 3, 2, 1]
a.sort()
print(a) # [1, 2, 3, 3, 3, 6]
```

```python
a: list = ['cat', 'Tom', 'Angela', 'pet']
a.sort(key=str.lower) # 排序时不区分大小写
print(a) # ['Angela', 'cat', 'pet', 'Tom']
a.sort()  # 排序时区分大小写
print(a) # ['Angela', 'Tom', 'cat', 'pet']
```

### 使用内置sorted()函数排序
  
**注意：**  
**使用该函数排序后，原列表顺序不变**  

```python
a: list = [1,5,7,3,9]
b = sorted(a)
print(a) # [1, 5, 7, 3, 9]
print(b) # [1, 3, 5, 7, 9]

c = sorted(a, reverse=True)
print(c) # [9, 7, 5, 3, 1]
```

### 一些复合操作示例  

```python
a = [1,2,3,4,5,6]
a.extend([a.pop(), a.pop()])
print(a) # [1, 2, 3, 4, 6, 5]

a.insert(1, a.pop(3))
print(a) # [1, 4, 2, 3, 6, 5]
```

### 复制列表  

赋值操作符只会将新的列表变量和旧的列表变量共享列表的引用  

```python
a = [1,2,3,4,5]
b = a
a.append(6)
print(b) # [1, 2, 3, 4, 5, 6]
```

实现真正的复制，需要用copy函数  

```python
a = [1,2,3,4,5]
b = a.copy()
a.append(6)
b.append(7)
print(a) # [1, 2, 3, 4, 5, 6]
print(b) # [1, 2, 3, 4, 5, 7]
```

## 参考  

Head First Python Chapter 2  
零基础学Python Chapter 4  
