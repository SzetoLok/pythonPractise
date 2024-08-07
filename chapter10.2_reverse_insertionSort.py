def swap(array,i,j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp

def insert(array, k):
    i = k
    while k < len(array) -1 :
        if array[k] > array[k+1]:
            swap(array, k , k+1)
        else:
            break
        k += 1

n = int(input('Enter the size: '))
A = []
for i in range(n):
    A.append(int(input('Enter the element: ')))
print ("before sorting: ", A)

k = n -2
while k >= 0:
    print(A)
    insert(A, k)
    k -= 1

print('final: ', A)