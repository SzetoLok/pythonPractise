w=5
h=3

A = [[-1, 2, -3, 4, -5], [60, 70, 80, 90, 100], [-11, 12, -13, 14, -150]]

# A = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 150]]
# for i in range(h):
#     for j in range(w):
#         print('please enter: ')
#         A[i][j] = int(input())
print(A)


i=0
for i in range(w):
    min=A[0][i]
    for k in range(1,h):
        if A[k][i]<min:
            min=A[k][i]
    print('min of column ',i,' is ',min)


i=0
for i in range(h):
    min=A[i][0]
    for k in range(1,w):
        if A[i][k]<min:
            min=A[i][k]
    print('min of row ',i,' is ',min)
