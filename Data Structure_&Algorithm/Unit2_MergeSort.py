def insertion_sort(array, n):
    for i in range(1, n):
        key = array[i]
        j = i-1
        while j > -1 and key < array[j]:
            array[j+1] = array[j]
            j = j-1
        array[j+1] = key
    return array

def merge_sort(array, n):
    left = list()
    right = list()
    if n <= 1:
        return array
    else:
        middle = n//2
    for i in range(0, middle):
      left.append(array[i])
    for i in range(middle, n):
      right.append(array[i])
    left = merge_sort(left, len(left))
    right = merge_sort(right, len(right))
    return merge(left, right)

def merge(left, right):
    result = list()
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left[0])
            left.pop(0)
        else:
            result.append(right[0])
        right.pop(0)
    if len(left) > 0:
        result.extend(left)
    if len(right) > 0:
        result.extend(right)
    return result




import random
import time

n = 10000

array = list()
for i in range(0, n):
  element = random.randint(1, n)
  array.append(element)
print('Problem:', array, end='\n\n')


start = time.time()
print('Result of insertion:', insertion_sort(array.copy(), len(array)))
end = time.time()
print('Consumed time by insertion:', end-start, end='\n\n')

start = time.time()
print('Result of merge:', merge_sort(array.copy(), len(array)))
end = time.time()
print('Consumed time by merge:', end-start)