# 集合  

集合用于存放不重复元素  

## 创建集合  

```python
a: set = set([1,3,3,4])
print(a) # {1, 3, 4}

a = set('aeioooouuu')
print(a) # {'i', 'e', 'a', 'o', 'u'}
```

对比c++  

```c++
unordered_set<int> a = {1,2,3,3};
for (auto& item: a)
    cout << item << " "; //3 2 1
```

## 添加元素  

```python
a: set = set([1,3,3,4])
a.add(5)
print(a) # {1, 3, 4, 5}
```

对比C++  

```c++
unordered_set<int> a = {1,2,3,3};
a.emplace(5);
for (auto p = a.begin(); p != a.end(); p++)
    cout << *p << " ";  //5 3 2 1
```

## 删除元素  

```python
a: set = set([1,3,3,4])
a.remove(3)
print(a) # {1, 4}
```

对比C++  

```c++
unordered_set<int> a = {1,2,3,3};
a.erase(3);
for (auto p = a.begin(); p != a.end(); p++)
    cout << *p << " ";  //5 2 1
```

## 集合运算  

```python
a: set = set([1,3,4])
b: set = set([1,5,6])

# 并集
c = a | b
print(c) # {1, 3, 4, 5, 6}

a.union(b)
print(a) # {1, 3, 4} 并不会改变a的值

# 交集
print(a & b) # {1}
print(a.intersection(b)) #{1}

# 差集
print(a - b) # {3, 4}
print(a.difference(b)) # {3, 4}
```

## 参考  

Head First Python Chapter 3  
零基础学Python Chapter 4  
挑战程序设计竞赛-2：算法和数据结构（第1版）  Chapter 9  
