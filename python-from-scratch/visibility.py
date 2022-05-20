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

class Class2:
    def __init__(self, num):
        self.__num = num

    @property
    def num(self):
        return self.__num

c2 = Class2(5)
print(c2.num) # 5
c2.num = 3 # 报错

