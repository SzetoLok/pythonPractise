def readfile(file):
    A = []
    f = open(file, 'r')
    # f1 = f.readlines()
    # print(f1)
    for line in f:
        line = line.strip('\n')
        line = line.strip('[]')
        print(line)
        print(type(line))
        element = line.split(',')
        # print(element)
        # print(type(element))
        array = [eval(elem.strip()) for elem in element]
        print(array)
        print(type(array))
        A.append(array)
        # for i in range(len(array)):
        print('array: ', A)
        print(len(A))
        B = [[0 for i in range(len(A))]for j in range(len(A[0]))]
        print(B)
        B = transpose(A,B)

def transpose(A,B):
    for i in range(len(A)):
        for j in range(len(A[0])):
            B[j][i] = A[i][j]

    print("this is the answer: ", B)

readfile("q3test.txt")
# A =[]
# print(type(A))