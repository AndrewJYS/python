# 字符串  

**注意：**
**C++：例如"beijing"字符串长度为7，但需要8个字节存储**  

## 拼接字符串  

Python中使用+运算符可以对多个字符串拼接  

```python
s: str = "123" + "124" + "125"
print(s) # 123124125
```

C++中语法不同：  

```c++
string s = "123";
s.append("124").append("125");
cout << s << endl; //123124125
```

## 截取字符串  

python中语法如下：  

```python
string[start : end : step]
```

```python
s = "0123456789"
print(s[0:8:2]) # 0246
```

C++中语法如下：  

```c++
string s = "0123456789";
cout << s.substr(4) << endl; //456789
cout << s.substr(4,3) << endl;  //456
```

## 分割字符串  

Python中语法如下：  

```python
str.split(sep, maxsplit)  
# sep用于指定分割符
# maxsplit可选，指定分割的次数
# 返回值：分割后的字符串列表
## 如果不指定任何参数，则默认采用空白符进行分割，此时无论有几个空格或者空白符都作为一个分割符。
```

```python
s = "0 1 2 3 4 5 6 7 8  9"
print(s.split()) # ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
print(s.split(' ')) #  ['0', '1', '2', '3', '4', '5', '6', '7', '8',' ', '9']
print(s.split(' ', 3)) # ['0', '1', '2', '3 4 5 6 7 8  9']
```

另一种分割方法是使用list转换，可以把字符串中的每个字符分隔开  

```python
s = "1 3 4  5 ' !"
print(list(s)) # ['1', ' ', '3', ' ', '4', ' ', ' ', '5', ' ', "'", ' ', '!']
```

## 合并字符串  

合并字符串和拼接字符串不同，他会将多个字符串采用固定的分割符连接在一起  

```python
strnew = string.join(iterable)
# strnew: 合并后的新字符串 
# string：用于指定合并时的字符串
# iterable：可迭代对象，该迭代对象中的所有元素（字符串表示）将被合并为一个新的字符串
```

```python
s: str = '123'
newS: str = "*".join(s)
print(newS) # 1*2*3

ls: list = ["1","2","3"]
newl: str = "*".join(ls)
print(newl) # 1*2*3
```

## 查找子串位置  

```python
s: str = "0123456789"
print(s.find("12")) # 1
print(s.find('90')) # -1
```

对比C++  

```c++
s = "0123456789";
cout << s.find("12") << endl; // output 1
cout << (s.find("90", 8) == string::npos) << endl; // output 1
//string::npos(not a position)
```

## 大小写转换  

**注意：**  
**string作为不可变对象，在使用upper()和lower()方法后不会改变原来的值**  

```python
s: str = "abcd"
s.upper()
print(s) # abcd
print(s.upper()) # ABCD
```

## 正则表达式  

### 在python中使用正则表达式语法  

Python中使用正则表达式时，是当作模式字符串使用的，所以要对特殊字符进行转义。但由于模式字符串可能包含大量的特殊字符和反斜杠，因此推荐下述写法（字符串前添加r/R）：  

```python
s = r'\bm\w*\b'
```

### 匹配字符串  

导入re模块，可以使用下述三个函数进行匹配  
(1) match()：从字符串开头进行匹配，如果起始位置匹配成功，返回match对象，否则返回None  
(2) search()：在整个字符串中搜索第一个匹配的值  
(3) findall()：在整个字符串中搜索所有匹配的字符串，返回匹配的字符串的列表  

```python
import re
pattern: str = r'mr_\w+'
string: str = "MR_SHOP mr_shop"
match = re.match(pattern, string, re.I)
print(match) # <re.Match object; span=(0, 7), match='MR_SHOP'>
string: str = "..MR_SHOP mr_shop"
match = re.match(pattern, string, re.I)
print(match) # None

pattern: str = r'mr_\w+'
string: str = "MR_SHOP mr_shop"
match = re.search(pattern, string, re.I)
print(match) # <re.Match object; span=(0, 7), match='MR_SHOP'>
match = re.search(pattern, string)
print(match) # <re.Match object; span=(8, 15), match='mr_shop'>

pattern: str = r'mr_\w+'
string: str = "MR_SHOP mr_shop"
match = re.findall(pattern, string, re.I)
print(match) # ['MR_SHOP', 'mr_shop']
```

### 使用正则表达式分割字符串  

```python
import re
pattern1 = r'\s@'
pattern2 = r'\s*@'
pattern3 = r's*@*'
string = "@11 @12  @13"
ls: list = re.split(pattern1, string)
print(ls) # ['@11', '12 ', '13']
ls: list = re.split(pattern2, string)
print(ls) # ['', '11', '12', '13']
```

## 参考  

零基础学Python  Chapter 5  
Introduction to Programming with C++, 3rd edition, Chapter 10  
