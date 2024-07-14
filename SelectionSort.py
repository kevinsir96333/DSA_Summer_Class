### 이전 다른 언어 수업에서 VS Code를 이용하여 코드를 작성하여 
### 아직 Jupyter Notebook 및 Google Colab이 아직 손에 익지 않아 & 코드 작성이 보다 편하여
### VS Code를 이용하여 코드를 작성하였습니다. ###


def selectionSort(arr, n):
    minIndex = 0
    tmp = 0
    for i in range(0, n-1, 1):
        minIndex = i
        for j in range(i+1, n, 1):
            if arr[j] < arr[minIndex]:
                minIndex = j    
        if (minIndex != i):
            tmp = arr[i]
            arr[i] = arr[minIndex]
            arr[minIndex] = tmp
            
    return arr


array = [64, 34, 25, 12, 22, 11, 90]
print('Original array:', array)
n = len(array)
selectionSort(array, n)
print('Sorted array:', array)