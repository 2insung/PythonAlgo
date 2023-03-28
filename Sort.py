import numpy as np

def SWAP(a, b):
    temp = a
    a = b
    b = temp
    return a, b

def InsertionSort(arr):
    for i in range(1, len(arr)):
        j = i - 1
        while (j >= 0) and (arr[j] >= arr[j + 1]) :
            arr[j] , arr[j+1] = SWAP(arr[j] , arr[j+1])
            j-=1

    return arr

def SelectionSort(arr):
    for i in range(len(arr)-1):
        key = i
        minIndex = i
        for j in range(i+1, len(arr)):
            if arr[key] > arr[j]:
                minIndex = j
        arr[key] , arr[minIndex] = SWAP(arr[key] , arr[minIndex])
    return arr 
        
def BubbleSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j] , arr[j+1] = SWAP(arr[j] , arr[j+1])
    return arr

def InsertionSortGap(start, arr, gap):
    for i in range(start, len(arr), gap):
        j = i - gap
        while (j >= 0) and (arr[j] >= arr[j + gap]) :
            arr[j] , arr[j+gap] = SWAP(arr[j] , arr[j+gap])
            j-=gap

    return arr


def ShellSort(arr):
    n = len(arr)
    Gap = int(n / 2)
    while Gap != 0:
        if Gap % 2 == 0:
            Gap += 1
        for i in range(Gap):
            InsertionSortGap(i, arr, Gap)
        Gap = int(Gap / 2)

    return arr



Arr = [2,5,1,7,8,6,3,10]
Arr2 = np.random.randint(low=0, high=100, size= 20)
print(InsertionSort(Arr))
print(SelectionSort(Arr))
print(BubbleSort(Arr))
print(ShellSort(Arr))
print(InsertionSort(Arr2))
print(SelectionSort(Arr2))
print(BubbleSort(Arr2))
print(ShellSort(Arr2))
