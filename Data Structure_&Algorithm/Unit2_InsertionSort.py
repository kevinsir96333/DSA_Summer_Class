def insertion_sort(array, n):
    for i in range(1, n):
        key = array[i]
        j = i-1
        while j > -1 and key < array[j]:
            array[j+1] = array[j]
            j = j-1
        array[j+1] = key
    return array
