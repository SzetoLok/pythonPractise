A = [[-1, 2, -3, 4, -5], [60, 70, 80, 90, 100], [-11, 12, -13, 14, -150]]

for i in range(len(A[0])):
    sum=0
    for j in range(len(A)):
        sum+=A[j][i]
    print('the sum of the column' , j , 'is' , sum)