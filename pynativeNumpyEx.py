import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def q1():
    arr = []
    for i in range(8):
        arr.append( int(input('enter a value: ')))
    print(arr)
    np_arr = np.array(arr)
    np2d_arr = np_arr.reshape(4,2)
    np2d_arr = np2d_arr.astype(np.int16)
    print(np2d_arr)
    print('shape: ', np2d_arr.shape)
    print('dimension: ', np2d_arr.ndim)
    print('element size: ', np2d_arr.itemsize)

def q2(start,end):
    a = np.arange(start,end,10).reshape(5,2)
    print(a)

def q3(arr):
    print(type(arr))
    answer = arr[:,2]
    print(answer)

def q4(arr):
    a = []
    for i in range(0, len(arr), 2):
        temp = []
        for j in range (1,len(arr[i]),2):
            temp.append(arr[i][j])
        a.append(temp)
    print(a)
    print(np.array(a))

def q5(arr1, arr2):
    arr3 =[]
    for i in range(len(arr1)):
        temp = []
        for j in range(len(arr1[i])):
            temp.append(arr1[i][j]+arr2[i][j])
        arr3.append(temp)
    print(arr3)
    square = np.array(arr3)
    square = square * square
    print(square) 

def q6():
    arr = np.arange(10,34).reshape(8,3)
    # arr2 = np.array([])
    arr2 = []
    # print(arr)
    # for i in range(0, len(arr),2):
    #     copy = arr[i:i+2].copy()
    #     print(copy)
    #     arr2.append(copy)
    arr2 = np.split(arr,4)
    print(arr2)
        
def q8(arr):
    print(np.min(arr, axis = 1))
    print(np.max(arr, axis = 0))

def q9(arr, col):
    new_arr = np.delete(arr, 1, axis=1)
    print(new_arr)
    print(np.shape(new_arr))
    new_arr = np.insert(new_arr, 1, newColumn, axis=1)
    print(new_arr)
    print(np.shape(new_arr))


# q1()
# q2(100,200)
# sampleArray = np.array([[11 ,22, 33], [44, 55, 66], [77, 88, 99],[1,2,3],[4,5,6]])
# q3(sampleArray)
# sampleArray = np.array([[3 ,6, 9, 120], [15 ,18, 21, 24], 
# [27 ,30, 33, 36], [39 ,42, 45, 48], [51 ,54, 57, 60]])

arr = [[3 ,6, 9, 12], [15 ,18, 21, 24], 
[27 ,30, 33, 36], [39 ,42, 45, 48], [51 ,54, 57, 60],[],[4,3,2,1],[1,2]]
arr1 = [[5, 6, 9,3], [21 ,18, 27, 3]]
arr2 = [[15 ,33, 24,3], [4 ,7, 1,3]]

sampleArray = np.array([[34,43,73],[82,22,12],[53,94,66]])
newColumn = np.array([[10,10,10]])
# q4(arr)

# q5(arr1, arr2)

# q6()
# q8(sampleArray)
q9(sampleArray, newColumn)