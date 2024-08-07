import math



def squareroot(arr1, arr2):
    if len(arr1)>0:
        for i in range(len(arr1)):
            arr2.append(math.sqrt(arr1[i])*10) 
            print(arr2[i])
    return arr2

def addfile(arr1, arr2):
    f2 = open('q2write.txt', 'w')
    f2.write('A'+'\n')
    for i in range (len(arr1)):
        f2.write(str(arr1[i])+'\n')
    f2.write('B'+'\n')
    for i in range (len(arr2)):
        f2.write(str(arr2[i])+'\n')

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
        # print(type(line))
        # line = int(f1.readline())
        # print(int(line))
    
    B = squareroot(A,B)
    print("B", B)
    addfile(A,B)


