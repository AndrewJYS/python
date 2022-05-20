# function-advanced  

## 匿名函数（lambda）  

### 定义与基本用法  

Python中，匿名函数指的是没有名字的函数，应用在需要一个函数，但是又不想去命名这个函数，这种函数只使用一次。语法如下：  

```python
result = lambda [arg1 [, arg2, ..., argn]]: expression
```

result:用于调用lambda的表达式  
[arg1 [, arg2, ..., argn]]:可选参数，用于指定要传递的参数列表，多个参数用逗号分隔  
expression:必选参数，用于指定一个实现具体功能的表达式。如果有参数，则在表达式中使用这些参数。  

**注意：**  
**使用lambda表达式时，表达式只能有一个，即只能返回一个值，也不能出现其他非表达式语句，如for, while**  

用法如下：  

```python
import math
r: int = 10
result: float = lambda r: math.pi * r * r
print(result(r))  # output 314.1592653589793
```

### 在匿名函数中绑定变量的值  

lambda 表达式中用到的x 是一个自由变量，在运行时才进行绑定而不是定义的时候绑定。因此，lambda 表达式中x 的值应该是在执行时确定的，执行时x的值是多少就是多少  

```python
x = 10
a = lambda y: x + y
x = 20
b = lambda y: x + y
print(a(10)) # 30
print(b(10)) # 30
```

如果希望匿名函数在定义的时候绑定参数，则使用下述代码（给匿名函数的参数及时赋值）  

```python
x = 10
a = lambda y, x=x: x + y
x = 20
b = lambda y, x=x: x + y
print(a(10)) # 20
print(b(10)) # 30

funcs = [lambda x, n=n: x+n for n in range(5)]
for f in funcs:
    print(f(0), end=' ') # 0 1 2 3 4 
```

## 嵌套函数，闭包  

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

再举一个内部外部函数都有参数的例子（可能比较牵强的例子，但是**闭包的作用在于将只有单个方法的类转换成函数**）。简单来说，闭包就是一个函数，但是它还保存着额外的变量环境，使得这些变量可以在函数中使用。闭包的核心特性就是它可以记住定义闭包时的环境。下面的例子中，inner函数会记住outer函数的参数str_list，然后在随后的调用中使用该值。  

```python
def find_n_first(str_list: list, num: int):
    print(str_list[0: num])

def outer(str_list: list):
    def inner(*args, **kwargs):
        return find_n_first(str_list, *args, **kwargs)
    return inner

i = outer(['1','2','3','4','5'])
i(3)  # ['1', '2', '3']
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

### 编写只接受关键字参数的函数  

出现在\*后面的参数，只能作为关键词参数使用。通过这一性质，可以设计只通过关键字形式接受特定参数的函数  

```python
def recv(maxsize, *, block):
    'Receives a message'
    pass

recv(1024, True) # 报错
recv(1024, block=True) # Ok
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

Python Cookbook Chapter 7  
Head First Python Chapter 10  
零基础学Python Chapter 6  
