# 面向对象编程  

## 创建数据成员并访问  

数据成员指类中定义的变量，即属性，根据定义位置，可以分为**类属性**和**实例属性**。类属性指定义在类中，并且在函数体外的属性，类属性可以在类的所有实例之间共享值，类似于C++中类的静态成员变量。实例属性是指定义在类的方法中的属性，只作用于当前是实例中。  

```python
class Numbers:
    cnt = 0;  # 类属性
    def __init__(self):
        Numbers.cnt += 1
        self.count = 0 # 实例属性
        self.count += 1

list = []
for i in range(4):
    list.append(Numbers())
print(Numbers.cnt) # 4
print(list[3].count) # 1
```

## 自定义标准行为__repr__()  

\_\_repr\_\_()是在Object类中定义的标准行为，所有python的类都会继承Object类。通过重写\_\_repr\_\_()方法，可以自定义对象的输出形式  

```python
class CountFromBy:
    def __init__(self, v: int=0, i: int=1) -> None:
        self.val = v
        self.incr = i

    def increase(self) -> None:
        self.val += self.incr

a = CountFromBy(10, 10) # <__main__.CountFromBy object at 0x00000160EC448400>
print(a) # 10
```

```python
class CountFromBy:
    def __init__(self, v: int=0, i: int=1) -> None:
        self.val = v
        self.incr = i

    def increase(self) -> None:
        self.val += self.incr

    def __repr__(self) -> str:
        return str(self.val)

a = CountFromBy(10, 10)
print(a) # 10
a.increase()
print(a) # 20
```

## 访问限制  

### 可见性  

为了保证类中某些成员不会被外部访问，可以在成员名前添加下划线，双下划线，或首尾加双下划线。  
(1)前置单下划线：protected，只允许类本身和子类访问。**但是不能通过from module import \*语句导入**  
(2)首尾双下划线：特殊方法，一般是系统定义名字  
(3)前置双下划线：private，只允许该类本身访问，且不能通过类的实例访问。**但是可以通过“类的实例名._类名__XXX”的方式访问**  

**注意：**  
**C++和Python的protected定义有略微不同，C++更严格，不能通过类的实例访问**  

```python
class Class1:
    num1 = 0
    _num2 = 0
    __num3 = 0

    def __init__(self):
        self.num4 = 0
        self._num5 = 0
        self.__num6 = 0

c = Class1()
print(c.num1)
print(c._num2)
print(c._Class1__num3)
print(c.__num3) # 报错
print(c.num4)
print(c._num5)
print(c._Class1__num6)
print((c.__num6)) # 报错
```

```c++
class class1 {
public:
    class1() {...}

    int num1;
protected:
    int num2;
private:
    int num3;
};

int main() {
    class1 c;
    cout << c.num1 << endl;
    cout << c.num2 << endl;  // 报错
    cout << c.num3 << endl;  // 报错
    return 0;
}
```

### 设置可读但不可更改的属性  

```python
class Class2:
    def __init__(self, num):
        self.__num = num

    @property
    def num(self):
        return self.__num

c2 = Class2(5)
print(c2.num) # 5
c2.num = 3 # 报错
```

## 继承  

```python
class GeometricObject:
    def info(self):
        print("GeometricObject")

    def superFunc(self):
        print("Geometric")

class Triangle(GeometricObject):
    def info(self):
        print("Triangle")

triangle = Triangle()
triangle.info() # Triangle
triangle.superFunc() # Geometric
```

对比C++  

```c++
class GeometricObject {
public:
    void info() {
        cout << "GeometricObject" << endl;
    }
};

class Triangle: public GeometricObject {
public:
    void info() {
        cout << "Triangle" << endl;
    }
};

int main() {
    GeometricObject* g = new GeometricObject();
    g->info();  // GeometricObject
    GeometricObject* g2 = new Triangle();
    g2->info(); // GeometricObject

    return 0;
}
```

## 参考  

Head First Python Chapter 8  
零基础学Python  Chapter 7  
Introduction to Programming with C++, 3rd edition, Chapter 10, 15  
