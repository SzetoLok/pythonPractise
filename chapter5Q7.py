A = [[-1, 2, -3, 4, -5], [60, 70, 80, 90, 100], [-11, 12, -13, 14, -150], [9,-8], [-11, 12], [-4,-5]]
B = [0 for i in range(len(A))]
for i in range(len(A)):
    max = A[i][0]
    for j in range(1,len(A[i])):
        if A[i][j] > max:
            max = A[i][j]
    B[i] = max

print(B)
min = B[0]
for i in range(1, len(B)):
    if B[i]<min:
        min = B[i]

print('min is :', min)
