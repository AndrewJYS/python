s: str = "123" + "124" + "125"
print(s) # 123124125

s = "0123456789"
print(s[0:8:2]) # 0246

s = "0 1 2 3 4 5 6 7 8  9"
print(s.split()) # ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
print(s.split(' ')) #  ['0', '1', '2', '3', '4', '5', '6', '7', '8',' ', '9']
print(s.split(' ', 3)) # ['0', '1', '2', '3 4 5 6 7 8  9']

s = "1 3 4  5 ' !"
print(list(s)) # ['1', ' ', '3', ' ', '4', ' ', ' ', '5', ' ', "'", ' ', '!']


s: str = '123'
newS: str = "*".join(s)
print(newS) # 1*2*3
ls: list = ["1","2","3"]
newl: str = "*".join(ls)
print(newl) # 1*2*3

s: str = "0123456789"
print(s.find("12")) # 1
print(s.find('90')) # -1

s: str = "abcd"
s.upper()
print(s) # abcd
print(s.upper()) # ABCD

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


import re
pattern1 = r'\s@'
pattern2 = r'\s*@'
pattern3 = r's*@*'
string = "@11 @12  @13"
ls: list = re.split(pattern1, string)
print(ls) # ['@11', '12 ', '13']
ls: list = re.split(pattern2, string)
print(ls) # ['', '11', '12', '13']