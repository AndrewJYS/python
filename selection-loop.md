# selection and loop  

## 分支语句  

针对下述语句  

```python
if a > b:
    r = a
else:
    r = b
```

Python可以简化为

```python
r = a if a > b else b
```

C++可以简化为  

```c++
int r = (a > b) ? a : b;
```

## 循环语句  

### for 循环  

Python中语法如下：  

```python
for 迭代变量 in 对象:
    循环体

for i in range(1, 10, 2):  # range(start, end, step)
    print(i, end = ' ')  #1 3 5 7 9

for i in range(10, 0, -2):
    print(i, end = ' ') # 10 8 6 4 2

string = "admin"
for ch in string:
    print(ch, end = " ")  #a d m i n
```

c++中语法如下：  

```c++
for (int i = 0; i < num; i++) {
    循环体
}

for (int i = 1; i < 10; i += 2) {
    cout << i << " ";
}

string s = "admin";
for (auto& ch : s) {
    cout << ch << " ";
}
```

## 推导式与生成器  

在sequence-dict, sequence-set, sequence-list.md中已经介绍了各种数据结构的推导式，这里简要介绍推导式和生成器的不同。

```python
for i in [x*3 for x in [1,2,3,4,5]]:
    print(i)
```

```python
for i in (x*3 for x in [1,2,3,4,5]):
    print(i)
```

上面两段代码的差异只有()和[]，但处理方式完全不同。[]提示这是list推导式，而()提示解释器这是生成器。必须等待列表推导式处理完5个数据（1，2，3，4，5）才能执行print()函数，也就是要将5个数据（1，2，3，4，5）全部放入内存后，才能执行print()。当数据量很大时，比如有10亿个数据，列表推导式可能会耗尽计算机所有的内存，最后报错。但是生成器不会，生成器只需要一个数据项的内存空间。每生成一个数据项，等待使用数据项的代码会立即执行，执行完毕后就会释放这个数据项的内存。  

## 生成器函数  

Python中增加yield关键字就是为了支持生成器函数的创建，能用return的地方都可以用yield。使用yield时，函数会自动变成一个生成器函数。下述程序中，如果把yield改成return，那么只会返回访问一条网址的结果，使用yield后，会将3条网址的访问信息全部返回。  

```python
import requests


def gen_from_urls(urls: tuple) -> tuple:
    for resp in (requests.get(url) for url in urls):
        yield len(resp.content), resp.status_code, resp.url


urls = ('http://talkpython.fm', 'http://pythonpodcast.com', 'http://python.org')
for resp_len, status, url, in gen_from_urls(urls):
    print(resp_len, '->', status, '->', url)
```

## 参考  

零基础学Python Chapter 3  
Head First Python Chapter 1, 12  
Introduction to Programming with C++, 3rd edition, Chapter 3, 5  
