
def immutable_object(s: str):
    s = "bfs"

s = "dfs"
print(s) # output dfs
immutable_object(s)
print(s) # output dfs

def mutable_object(ls: list):
    ls.append(2)

ls = [1,7]
print(ls) # output [1, 7]
mutable_object(ls)
print(ls) # output [1, 7, 2]


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