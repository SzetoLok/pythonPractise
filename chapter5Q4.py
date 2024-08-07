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
    sum=0
    for k in range(h):
        sum=sum+A[k][i]
    print('sum of column ',i,' is ',sum)


i=0
for i in range(h):
    sum=0
    for k in range(w):
        sum=sum+A[i][k]
    print('sum of row ',i,' is ',sum)

print (len(A), len(A[0]))