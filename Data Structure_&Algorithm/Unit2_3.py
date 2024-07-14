
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