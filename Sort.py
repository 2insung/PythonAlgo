def InsertionSort(arr):
    for i in range(1, len(arr)):
        j = i - 1
        while (j >= 0) and (arr[j] >= arr[j + 1]) :
            temp = arr[j]
            arr[j]= arr[j+1]
            arr[j+1] = temp
            j-=1

    return arr

def SelectionSort(arr):
    for i in range(len(arr)-1):
        key = i
        minIndex = i
        for j in range(i+1, len(arr)):
            if arr[key] > arr[j]:
                minIndex = j
        temp = arr[key]
        arr[key]= arr[minIndex]
        arr[minIndex] = temp  
    return arr 
        
def BubbleSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j]= arr[j+1]
                arr[j+1] = temp
    return arr

Arr = [2,5,1,7,8,6,3,10]
print(InsertionSort(Arr))
print(SelectionSort(Arr))
print(BubbleSort(Arr))
