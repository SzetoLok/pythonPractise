def q1(b,n):
    if n == 0:
        print(1)
        return 1
    else:
        sum = pow(b,n) + q1(b,n-1)
        print(pow(b,n))
        # print(sum)
        return sum
    
# x = q1(3,8)
# print(x)


def q2(n):
    if n == 0:
        return 0
    else:
        sum = n*(n+1)+q2(n-1)
        print(n*(n+1))
        return sum

# x = q2(10)
# print(x)

def q3(a,b,n):
    if n == 1:
        return a 
    else:
        sum = a + ((n-1)*(b)) + q3(a,b,n-1)
        print(a + ((n-1)*(b)))
        return sum

x = q3(1,2,3)
print(x)