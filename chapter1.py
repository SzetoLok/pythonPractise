# x=10
# y=20
# z=int(input('enter a number:'))
# a=input('enter a character:')
# print('a value:',a)
# print(type(a))
# print('z value:',z)
# print(type(z))
# print(x+y+z)

import math


def half():
    a=int(input('enter a number1:'))
    b=int(input('enter a number2:'))
    total=(a+b)/2
    print('total: ', total)

# half()
def square():
    a=int(input('enter a number1:'))
    b=int(input('enter a number2:'))
    c=int(input('enter a number3:'))
    d=int(input('enter a number4:'))
    first=a+b
    second=c+d
    print('first: ', first)
    print('second: ', second)
    total=first*second
    print('total: ', total)
# square()    

def float_square():
    a=float(input('enter a number1:'))
    b=float(input('enter a number2:'))
    c=float(input('enter a number3:'))
    d=float(input('enter a number4:'))
    first=a+b
    second=c+d
    print('first: ', first)
    print('second: ', second)
    total=first*second
    print('total: ', total)

# float_square()    

def empty_square():
    a=float(input())
    b=float(input())
    c=float(input('enter a number3:'))
    d=float(input('enter a number4:'))
    first=a+b
    second=c+d
    print('first: ', first)
    print('second: ', second)
    total=first*second
    print('total: ', total)

# empty_square()

def q1():
    a=int(input('enter a number1:'))
    b=int(input('enter a number2:'))
    c=int(input('enter a number3:'))
    d=int(input('enter a number4:'))
    first=a+b
    second=c-d
    print('first: ', first)
    print('second: ', second)
    total=(first/second)*d
    print('total: ', total)
    
# q1()

def q3():
    a=int(input('enter a number1:'))
    b=int(input('enter a number2:'))
    c=int(input('enter a number3:'))
    
    first= (pow(a,2)+pow(b,2))/(pow(a,2)-pow(b,2))
    second= math.sqrt((pow(a,2)+pow(b,2)))
    third = a - (b+c)*(3*a-c)
    print('first: ', first)
    print('second: ', second)
    print('third: ', third)

q3()