from functools import reduce

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

'''MAP'''
# iterative
arr1 = [] 
for i in arr:
    arr1.append(i**2)

# map function
arr1 = list(map(lambda x: x**2, arr))

# list comprehension
arr1 = [x**2 for x in arr]
# ^ this is smooth af. You will pick up a l l the ladies

'''FILTER'''
# iterative
arr2 = []
for i in arr:
    if i % 2 == 0:
        arr2.append(i)

# filter function
arr2 = list(filter(lambda x: x % 2 == 0, arr))

# list comprehension
arr2 = [x for x in arr if x % 2 == 0]
# ^ this is smooth af. You will pick up a l l the guys

'''REDUCE'''
# iterative
prod = 1
for i in arr:
    prod *= i

# reduce function
prod = reduce(lambda a, b: a*b, arr)

# list comprehension
'''extremly janky, doesnt guarantee any ladies or guys'''