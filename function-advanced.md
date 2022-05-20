# function-advanced  

## 嵌套函数  

Python中，函数代码组中，可以是任意代码，这也包括定义另一个函数的代码，通常称为嵌套或内部函数。还可以从外部函数返回内部函数，实际上，返回的是一个函数对象。  

```python
def outer():
    def inner():
        print('This is inner')

    print('this is outer, invoking inner')
    inner()

outer()
"""
this is outer, invoking inner
This is inner
"""
```

如果一个函数含有多行，那么使用嵌套函数，将一部分代码放入内部函数中会很有意义。这个技术更常见的一种语法是，外围函数使用return语句返回嵌套函数作为它的返回值，修饰符就采用这种方法创建。  

```python
def outer():
    def inner():
        print('This is inner')

    print('this is outer, invoking inner')
    return inner

i = outer() # this is outer, invoking inner
i() # This is inner
```

## 可变参数  

这里只讨论Python中的可变参数  

### *paramter  

这种形式接受任意多个实际参数并将其放到一个元组中。  

```python
def printVariables_1(*paratmers):
    for item in paratmers:
        print(item, end = ' ')

printVariables_1(1,4,5,6,3) #output 1 4 5 6 3 
```

### **parameter  

这种形式表示接收任意多个类似关键字参数一样的显式赋值的实际参数，并将其放到一个字典中。  

```python
def printVariables_2(**kwargs):
    for key, value in kwargs.items():
        print(key, ": ", value)

printVariables_2(num1=1, num2=2, num3=3)
'''
output:
num1 :  1
num2 :  2
num3 :  3
'''
```

### 结合起来  

```python
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
```

## 函数修饰符  

（1）修饰符是一个函数  
（2）修饰符会取被修饰函数为参数  
（3）修饰符返回一个新函数  
（4）修饰符需要确保它返回的函数于被修饰函数有同样的参数（个数和类型都相同）。原因是，一个修饰符应用到一个现有函数时，对这个现有函数的所有调用都会替换成**调用修饰符返回的函数**。如果**被修饰函数**有n个参数，而修饰符的内部函数（也就是返回的函数）中会调用被修饰函数，那么就要通过内部函数传递参数给被调用函数。因此，内部函数的参数与被修饰函数的参数必须相等  

除此以外，还有两点需要注意，下面checker.py中做了注释  

```python
# checker.py
from flask import session
from functools import wraps  # 导入必要模块

def check_logged_in(func):
    @wraps(func) # 在修饰符中修饰wrapper函数
    def wrapper(*args, **kwargs):
        if 'logged_in' in session:
            return func(*args, **kwargs)
        return 'You are NOT logged in.'
    return wrapper
```

```python
# 详细代码见 head-for-python\chapter10\simple_webapp.py

@app.route('/page1')
@check_logged_in
def page1() -> str:
    return 'This is page 1.'
```

## 参考  

Head First Python Chapter 10  
零基础学Python Chapter 6  
