def reverse(A,B):
    if len(A)>0:
        for i in range(len(A)-1,-1,-1):
            B.append(A[i])
            print(A[i])
    return B

f1 = open('q2test.txt', 'r')
n = int(f1.readline())
A =[]
B = []
if n <= 0:
    print('the size is not correct.')
else:
    # line = int(f1.readline())
    line = f1.readline()
    while n > 0 and line:
        line = int(line)
        if line<=0:
            print('the value',line,  ' is not positive.')
            # n-=1
        else:
            A.append(line)
            n-=1
        print(A)
        line = f1.readline()
    B = reverse(A,B)
    print(B)