def compare(a,b):
    if (a>b):
        print("a is greater than b")
    elif (a==b):
        print("a is equal to b")   
    else:
        print('a is smaller than b.')

    print("a:",a)
    print("b:",b)

# compare(300,300)
def compareAndReturn(a,b):
    print('a: ', a)
    print('b: ', b)

    if (a>b):
        print('c: ', a-b)
    else:
       print('c: ', b-a)

# compareAndReturn(99,999)

def grade(score):
    if (score>100):
        grade= 'NA'
    elif (score >= 90):
        grade = 'A'
    elif (score >= 80):
        grade = 'B'
    elif (score >= 70):
        grade = 'C'
    elif (score >= 60):
        grade = 'D'
    else:
        grade = 'F'
    print(score, ' is classified as ', grade)

# grade(99)
# grade(89)
# grade(79)
# grade(69)
# grade(59)
# grade(999)
# grade(11)
# grade(76)
# grade(98)
# grade(35)
# grade(989)
# grade(98)

def discount(price):
    discount=1
    if (price<0):
        print('price is negative!!!')
        return 
    elif (1000 > price):
        discount=1
    elif (price >= 1000 and 4999 >= price):
        discount = 0.9
    elif (9999 >= price):
        discount =  0.8
    else:
        discount =  0.7

    # price*=discount
    price = int(round(price*discount,0))
    print("final price: ", price)

# discount(80)
# discount(3000)
# discount(8888)
# discount(11000)
# discount(-80)
def q1(x,y):
    if (x>=y):
        print(x, ' x is bigger than or equal to y: ', y)
    else:
        print(y, ' y is bigger than x: ', x )
# q1(4,5)
# q1(5,5)
# q1(6,5)
# q1(-4,-5)

def q2(x,y):
    
    if (x>0 and y>0):
        z=1
        print('z: ',z)
    else:
        z=0
        print('z: ',z)
        
# q2(3,4)
# q2(-3,4)
# q2(3,-4)
# q2(0,0)
# q2(-3,-4)

def q3(x,y,u,v):
    a = x+y
    b = u+v
    if (a>b):
        c=a
        print('a is bigger')
    else:
        c=b
        print('b is bigger than or equal to')

    print('c: ',c)

# q3(1,2,3,4)
# q3(5,3,2,1)
# q3(1,1,1,1)

def q4(x,y,u,v):
    a = x+y
    b = u-v
    if ((a/b)>=2):
        c=x-y
        print('result is bigger than or equal to 2')
    else:
        c=b
        print('result is smaller than 2: ', c)

    print('result: ',c)

# q4(1,2,3,4)
# q4(5,3,2,1)
# q4(1,1,1,0)

def q5(x,y):
    if (x>=y):
        result=x*x
    else:
        result=y*y
    print('result: ',result)

# q5(3,4)
# q5(40,30)
# q5(0,0)
# q5(-3,-4)
# q5(-4,-3)

def q6(income):
    if income > 4090000:
        rate = int(0.4*100)
        difference = 721100
    elif income > 2180000:
        rate = int(0.3*100)
        difference = 312100
    elif income > 1090000:
        rate = int(0.21*100)
        difference = 115900
    elif income > 410000:
        rate = int(0.13*100)
        difference = 28700
    elif income > 0:
        rate = int(0.06*100)
        difference = 0
    temp = (income*rate/100)
    print('temp: ', temp)
    tax = round(income*rate/100 - difference,2)
    print("------------")
    print('tax: ', tax)
    print('rate: ', rate)
    print('diff: ', difference)

q6(4090001)
q6(2180001)
q6(1090001)
q6(410001)
q6(409)

print(1/10)
print(1/100)