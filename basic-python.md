# basic python

## 变量  

### 声明变量，定义变量  

变量声明:规定了变量的类型和名字。  
变量定义:除了规定了变量的类型和名字之外,还申请存储空间,也可能会为变量赋一个初始值。  

```c++
// c++
int a = 3;
string s = "string";
vector<int> vec = {1, 2, 3};
```

```python
# python
a: int = 3
b: str = "string"
ls: list = [1, 2, 3]
```

### 变量类型  

Python使用内置函数type()返回变量类型  

```python
>>> num = 6
>>> print(type(num))
<class 'int'>
>>> str = '3255'
>>> print(type(str))
<class 'str'>
```

而C++中使用typeid查看变量类型  

```c++
//#include<typeinfo>
int a = 8;
cout << typeid(a).name() << endl;
//输出 i，表示int
```

### 变量地址  

Python使用内置函数id()返回变量的内存地址  

```python
>>> num = 45
>>> print(id(num))
140711404645552
>>> num2 = num
>>> print(id(num2))
140711404645552
```

C++中使用&运算符  

```c++
int a = 8;
cout << &a << endl;
```

## 输入数据  

```c++
int carrots;
cin >> carrots; //输入12
cout << carrots; // output 12
```

```python
carrots = input("Please input an integer")
print(carrots)

carrots = float(input())
print(carrots)
```

## 基本数据类型  

### 整数类型  

C++中的基本整形包括：char, short, int, long, long long  

#### 整型字面值

整型字面值：指显式地书写的常量，如272，1776。C++和Python可以用3种不同的计数方式书写整数。  
Python：以 **0O或0o** 开头表示八进制数，用 **0x或0X** 开头表示十六进制数  
C++：以 **0** 开头表示八进制数，以 **0x或0X** 开头表示十六进制数  

#### 转义序列  

可以基于字符的八进制和十六进制编码来使用转义序列  

```c++
// C++
char ch1 = '\012'; //八进制的换行符
char ch2 = '\xa'; //十六进制的换行符
cout << ch1 << " " << ch2;
```

### 类型转换  

下面讨论C++中的常见类型转换  

1.初始化和赋值进行的转换  
C++中，将浮点数转为整数时，采取截取操作(3.86->3)  

```c++
float a = 3.86;
int b = a; //3
```

2.表达式中的转换  

```c++
short a = 20;
short b = 20;
short c = a + b;
```

上述第三条语句，C++取得a和b的值后，将他们转换成int，然后再将计算的结果转回short。这称为**整型提升**。原因是int是计算机最自然的类型，能提高运算速度。  

凡是运算涉及两个类型（比如一个float加上一个double）时，较小的类型会被转换成较大的类型（float->double），与结果赋给的变量类型无关；最后将结果赋值给变量时，按照变量的要求再做变换。具体情况参见C++检验表（C++ Primer Plus P.64）

### 字符串  

Python：在字符串前加上r，字符串将按原样输出  

```python
>>> str = r'egseg\nesrse'
>>> print(str)
egseg\nesrse
>>> str = 'egseg\nesrse'
>>> print(str)
egseg
esrse
```

## 运算符  

### 算术运算符  

Pyhton: // 整除；  / 除；  ** 幂；

```python
>>> print(7/3)
2.3333333333333335
>>> print(7//3)
2
>>> pow = 2**4
>>> print(pow)
16
>>> print(type(pow))
<class 'int'>              #注意返回的是int
```

C++：/ 除；   pow() 幂  
**注意：pow()返回值是double类型**  

```c++
cout << 7 / 3 << endl;  //2
cout << (double)7 / 3 << endl; // 2.33333
cout << 7 / 3.0 << endl; // 2.33333

cout << pow(2,4) << endl;
cout << typeid(pow(2,4)).name() << endl; // d : double
```

### 逻辑运算符  

|语言|逻辑与|逻辑或|逻辑非|
:-:|:-:|:-:|:-:  
|Python|and|or   |not|
|C++   |&& |\|\| |!  |  

### 位运算符  

|语言|位与|位或|位异或|位取反|左移位|右移位|
:-:    |:-:|:-:|:-:|:-:|:-:|:-:
|Python|&  |\| |^  |~  |<< |>>
|C++   |&  |\| |^  |~  |<< |>>

## python的内置bool()函数

如果给bool() 提供0，值None，空串或是空的内置数据结构，则返回False。其他所有对象都返回True  

```python
# False
print(bool(0))
print(bool(0.0))
print(bool(''))
print(bool([]))
print(bool({}))
print(bool(None))

# True
print(bool(-1))
print(bool(42))
print(bool(5.000001))
print(bool([1, 4]))
print(bool('seg'))
print(bool({'q':1, 'er': 2}))
```

## 参考  

C++ Primer Plus, Chapter 2, 3  
Head First Python Chapter 4  
零基础学Python Chapter 2  
Introduction to Programming with C++, 3rd edition, Chapter 2, 4  
