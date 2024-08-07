import math


n =0 
while n <= 0:
    n = int(input('enter the size of the array: '))
A = []
while n>0:
    val = int(input('enter a value: '))
    if val <=0 :
        A.append(0)
        # continue
    else:
        A.append(val)
    n -= 1

B = []
for i in range(len(A)):
    B.append(A[i] * A[i])

print(A)
print(B)

final = open('q1.txt', 'w')
for i in range(len(B)):
    final.write(str(B[i]) + '\n')
final.close()

final = open('q1.txt', 'r')
print('----final----')
for line in final:
    print(line, end="")
