def BubbleSort (arr, n):
    for i in range(0, n-1, 1):
        for j in range (0, n-1-i, 1):
            if (arr[j] > arr[j+1]): #별도로 & 조건을 넣어서 만들 수 있나?
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    
    return arr

array = [64, 34, 25, 12, 22, 11, 90]
print('Original array:', array)
n = len(array)
BubbleSort(array, n)
print('Sorted array:', array)  