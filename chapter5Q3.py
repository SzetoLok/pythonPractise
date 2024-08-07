A = [0 for i in range(10)]
for i in range(10):
    print('enter: ')
    # 1. 获取用户输入
    A[i] = int(input())
print(A)

B = [0 for i in range(10)]
for i in range(10):
    if A[i] >= 0:
        B[i] = 1
    else:
        B[i]=0

print(B)
