def q4(array):
    val=0
    for i in range(len(array)):
        # temp = int(input('give me a number: '))
        temp = array[i]
        if temp>12:
            val = val + temp
            print(temp, ' is bigger than 12.')
        else:
            print(temp, ' is NOT bigger than 12.')
        i+=1
    print('total: ', val)

# q4([1,2,23,55,66,7,4,3,76,99])

def q6(array):
    val=0
    for i in range(len(array)):
        temp = array[i]
        if temp>0:
            val += temp*temp
            print(temp, ' is +ve. -->', temp*temp)
        else:
            print(temp, ' is -ve.')
        i += 1
    print('total: ', val)

q6([1,2,3,4,5,-6,-7,-8,-9])
q6([12,-2,23,-4,5,-6,7,-8,-9])