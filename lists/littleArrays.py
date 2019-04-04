import random
 
array1 = [i for i in range(10)]
array2 = list(filter(lambda x: x % 2 == 0, range(10)))
array3 = list(filter(lambda x: x % 2 == 0, range(random.randint(0, 100))))
array4 = [random.randint(0, 100) for i in range(100)]
print(array1)
print(array2)
print(array3)
print(array4)
