# 函数  

**注意**  
C++中应当为程序中每个函数提供函数原型  

## 局部，全局和静态局部变量

### 局部变量  

Python和C++一样，在函数内部定义的变量称为局部变量。参数实质上是局部变量，参数的作用域覆盖整个函数。  

```python
def f1(num1: int):
    num1 = 5

num1 = 4
print(num1)  // 4
f1(num1)
print(num1)  // 4
```

C++函数传递基础数据类型示例：  

```c++
void f1(int num1) {
    num1++;
}

int main() {
    int num1 = 4;
    cout << num1 << endl; // 4
    f1(num1);
    cout << num1 << endl; // 4
}
```

C++函数传递指针示例：  

```c++
void pointer(int* num) {  //num指针也是局部变量，调用函数pointer(p);后不会改变原来的指针p
    int* newPointer = new int(6);
    num = newPointer;
}

int main() {
    int* p = new int(12);
    pointer(p);
    cout << *p << endl;  // output 12

    return 0;
}
```

C++函数传递结构体示例：  

```c++
struct node {
    int a;
    node(int a): a(a){};
};

void changeNode(node nd) {
    nd.a = 2;
}

int main(){
    node one(1);
    cout << one.a << endl;  //output 1
    changeNode(one);
    cout << one.a << endl;  //output 1

    return 0;
}
```

C++函数传递对象示例：  

```c++
class class1 {
public:
    int num;
    class1() {
        num = 1;
    }
};

void changeClass(class1 c) {
    c.num = 2;
}

int main(){
    class1 c;
    cout << c.num << endl;  //output 1
    changeClass(c);
    cout << c.num << endl;  //output 1

    return 0;
}
```

### 全局变量  

C++中，一个全局变量的作用域从它被声明开始，直到程序末尾为止。  

**注意：**  
**随意使用全局变量并不是好的编程习惯，因为所有函数都能访问全局变量，也可以修改全局变量，这会加大调试难度，应该尽量避免使用全局变量，只有当常量永远不会改变时，使用全局变量是可行的**  

```c++
...
int main() {
    f2();
    f3();  // output 1
    return 0;
}

int y;

void f2() {
    y++;
}

void f3() {
    cout << y << endl;
}
```

Python: 如果在函数中定义了相同名称的变量，则必须使用global关键字来访问全局变量。 否则，函数将使用局部变量。下述代码输出如下：  
My favorite website is JournalDev.com  
My favorite website is Wikipedia.com  
My favorite website is Wikipedia.com  

```python
website = "JournalDev.com"

def print_website():
    global website
    print(f'My favorite website is {website}')

    website = 'Wikipedia.com'
    print(f'My favorite website is {website}')

print_website()
print(f'My favorite website is {website}')
```

### 静态局部变量  

C++中，当一个函数结束运行，其所有的局部变量都会被销毁。有时我们需要保留局部变量的值，以便下次调用时使用。静态局部变量会一直驻留在内存中。  

**注意：**  
**1.静态变量的初始化只在第一次调用时发生一次，因此下述代码在第二次运行f4()函数时，静态局部变量的声明不起作用**  
**2.当使用引用传递方式时，形参和实参的类型必须是相同的**  

```c++
...
int main() {
    f4();  // output 2
    f4();  // output 3
    return 0;
}

void f4() {
    static int x = 1;
    x++;
    cout << x << endl;
}
```

Python中没有static关键字可用于静态变量声明，但可以用模块来实现静态变量。  

```python
#先建立一个模块static_variable_pk.py，里面包含如下语句
static_var = 1

#在另一个程序中进行测试
import static_variable_pk as st

def static_test():
    st.static_var += 4
    print(st.static_var)

static_test()  # output 5
static_test()  # output 9
```

## 以引用方式传递参数  

参数可以通过引用的方式传递，使形式参数是实际参数的一个别名。  

```c++
void f(int& num) {
    num++;
}

int main() {
    int a = 6;
    cout << a << endl;  //output 6
    f(a);
    cout << a << endl;  //output 7
    return 0;
}
```

Python采用的是“传对象引用”的方式。可以变量中存储的值认为是值的内存地址，而不是它真正的值。会把这个内存地址传入函数，而不是传入真正的值。Python中对象有两种，“可更改”（mutable）与“不可更改”（immutable）对象。strings, tuples, 和numbers是不可更改的对象，而 list, dict, set 等则是可以修改的对象。解释器会查看对象引用指示的那个值的类型，如果是可变的，则会使用“按引用调用”语义；如果是不可变的，就会使用“按值调用”语义。

```python
def immutable_object(s: str):
    s = "bfs"

s = "dfs"
print(s) # output dfs
immutable_object(s)
print(s) # output dfs
```

上述字符串不变，是因为字符串是个不可变对象

```python
def mutable_object(ls: list):
    ls.append(2)

ls = [1,7]
print(ls) # output [1, 7]
mutable_object(ls)
print(ls) # output [1, 7, 2]
```

上述代码中，list是可变对象

```python
def double(arg):
    print('Before: ', arg)
    arg = arg * 2
    print('After: ', arg)

number = [1,2,3]
double(number)
print(number)
"""
Before:  [1, 2, 3]
After:  [1, 2, 3, 1, 2, 3]
[1, 2, 3]
"""
```

上述代码是需要注意的：**=右边的的代码先执行，然后创建的值将其对象引用赋给=左边的变量。执行代码arg * 2会创建一个新值，它会有一个新的引用，然后这个新对象引用赋给arg变量，覆盖函数代码组中arg存储的原先的对象引用。但是调用代码中老的对象引用仍然存在，它的值未变，所以仍然输出原先的列表。**这个过程有点像前面讨论的[C++函数传指针](#局部变量)，函数参数中的指针是临时变量，函数中改变了指针的值（不是指针指向的值），并不会对函数外的调用代码中的指针有影响。  

## 常量引用参数  

C++中，若参数在函数中不能改变，应该把这个变量设置为常量，告诉编译器这个数值不能改变。  

```c++
void f1(const int a) {
    //a++; //报错
}

void f2(const int& a) {
    //a++; //报错
}

int main() {
    int a = 1;
    f1(a);
    f2(a);

    return 0;
}
```

## 使用注解改进文档  

使用注解可以提高代码的可读性，比如可以增加函数的返回类型，增加参数的注解，增加函数功能的说明，**但是，这些注解并不会帮助检查类型，不会有任何其他的行为**

示例如下：  

```python
def search_for_letters(phrase: str, letters: str='aeiou') -> set:
    """Returns the set of 'letters' found in 'phrase'."""
    return set(letters).intersection(set(phrase))
```

通过help(functionName)可以查看函数文档  

```python
help(search_for_letters)

输出如下：
Help on function search_for_letters in module __main__:

search_for_letters(phrase: str, letters: str = 'aeiou') -> set
    Returns the set of 'letters' found in 'phrase'.
```

## 带有默认参数的函数  

（1）如果默认值是可变容器的话，比如说列表、集合或者字典，那么应该把None 作为默认值  
（2）如果不打算提供一个默认值，只是想编写代码来检测可选参数是否被赋予了某个特定的值，那么可以采用下面的惯用手法（不要用None, 0 或者False来检测）：  

```python
_no_value = object()
def spam(a, b=_no_value):
    if b is _no_value:
        print('No b value supplied')
    else:
        print('OK')

spam(1) # No b value supplied
spam(1, 3) # OK
```

### 默认参数绑定  

对默认参数的赋值只会在函数定义的时候绑定一次  

```python
x = 42
def spam(a, b=x):
    print(a, b)

spam(1) # 1 42
x = 32
spam(1) # 1 42
```

**注意：**  
**给默认参数赋值的应该总是不可变的对象，比如None、True、False、数字或者字符串，否则会陷入隐匿的问题中**  

## 批量调用函数  

假设有函数f1()  

```python
def f1(arg1: str, arg2: str, arg3: str):
    print(arg1, arg2, arg3)
```

而f1()每个参数又有不同的选项，如果想遍历这些参数的组合，批量调用函数f1()，可以用下面这种方式，排列组合参数，再用字典的方式传入参数  

```python
from itertools import product
argname = ['arg1', 'arg2', 'arg3']
arg1 = ['a1_1', 'a1_2']
arg2 = ['a2_1', 'a2_2']
arg3 = ['a3_1']
loop_val = [arg1, arg2, arg3]
for argval in product(*loop_val):
    f1(**dict(zip(argname, argval)))
```

输出如下：  

```python
a1_1 a2_1 a3_1
a1_1 a2_2 a3_1
a1_2 a2_1 a3_1
a1_2 a2_2 a3_1
```

## 参考  

Python Cookbook Chapter 7  
C++ Primer Plus, chapter 2, 7  
Head First Python Chapter 4  
零基础学Python Chapter 6  
Introduction to Programming with C++, 3rd edition, Chapter 6  
https://www.journaldev.com/22870/global-variables-python  
https://www.cnblogs.com/Xingtxx/p/11044255.html  
