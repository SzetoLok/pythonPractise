def push(array, val):
    array += [val] 
    print(array)

def pop(array):
    n = len(array)-1
    array[n:n+1] = []
    print('pop:' ,array)

def peek(array):
    n = len(array)-1
    print('peek:' ,array[n])
    array[n:n+1] = []
    print('after peek:' ,array)
A = []
# A += [10]
# print(A)
push(A, 10)
push(A, 20)
push(A, 30)
push(A, 40)
push(A, 10)
push(A, 20)
push(A, 30)
push(A, 40)
pop(A)
pop(A)
pop(A)
pop(A)
peek(A)
