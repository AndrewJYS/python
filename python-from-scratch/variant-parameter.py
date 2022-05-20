def printVariables_1(*paratmers):
    for item in paratmers:
        print(item, end = ' ')

printVariables_1(1,4,5,6,3) #output 1 4 5 6 3

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