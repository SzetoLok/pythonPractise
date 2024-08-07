def push(array, val):
    array += [val]
    print('push: ', array)

def pop(array):
    if len(array)!=0:
        print('pop: ', array[0])
        array = array[1:]
        print('after pop: ', array)
        return array
    else:
        return []
    #  haven't figured out why the array is not affect A[]
A = []
push(A, 1)
push(A, 2)
push(A, 3)
push(A, 4)
push(A, 1)
push(A, 2)
push(A, 3)
push(A, 4)
A = pop(A)
A = pop(A)
A = pop(A)
A = pop(A)
A = pop(A)
A = pop(A)
A = pop(A)
A = pop(A)
A = pop(A)
A = pop(A)
A = pop(A)
A = pop(A)