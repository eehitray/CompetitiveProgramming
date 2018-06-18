import itertools as it
from operator import mul
"""
Iterators that return an finite stream of data.
"""

"""
chain(*it: iterables) :
takes a variable amount of iterables and
iterates through all of them in order
"""
for i in it.chain('ABCD', 'ZYXW'):
    print(i, end='')
# out => ABCDZYXW

"""
compress(it: iterable, arr: truth table) :
iterates through the values corresponding to true in table
"""
for i in it.compress('EEHIT', [1,0,1,0,1]):
    print(i, end='')
# out => EHT

"""
dropwhile(lambda/func returns boolean, it: iterable) :
starts returning values from an iterator when predicate fails
"""
for i in it.dropwhile(lambda x: x < 5, [1,2,3,4,5,4,3,2,1]):
    print(i, end=' ')
# out => 5 4 3 2 1

"""
takewhile(lambda/func returns boolean, it: iterable) :
stops returning values from an iterator when predicate fails
"""
for i in it.takewhile(lambda x: x < 5, [1,2,3,4,5,4,3,2,1]):
    print(i, end=' ')
# out => 1 2 3 4

"""
accumulate(it: iterable) :
returns [p[0], p[0]+ p[1], p[0] + p[1] + p[2] ... ]
can also take a function
"""
print(list(it.accumulate([1,2,3,4,5]))) # out => [1, 3, 6, 10, 15]
print(list(it.accumulate(range(1,6), mul)))
# out => [1, 2, 6, 24, 120]
# works just like reduce but uses returns all the acummulated values
# as an iterator 

"""
filterfalse(lambda/func returns boolean, it: iterable) :
just like filter but evaluates to false
"""
print(list(it.filterfalse(lambda x: x % 2 == 0, range(0,10))))
# out => [0, 2, 4, 6, 8]

"""
islice(it: iterable, start, stop, step):
works just like a[start:stop:step]
"""
print(list(it.islice([1,2,3,4,5], 0, None, 2)))
# out => [1, 3, 5]

"""
tee(it: iterable, n=2):
returns n itertables
"""
print(list(it.tee([1,2,3,4,5],3)))
# out => [[1,2,3,4,5], [1,2,3,4,5], [1,2,3,4,5]]

"""
starmap(fun: function, it: iterable):
returns values obtained usin the function using
arguments passed in the iterable
"""
print(list(it.starmap(mul, [(2,3), (3,5), (4,5)])))
# out => [6, 15, 20]

"""
ziplongest(*it: iterables) :
zips all iterables passed together as tuples
doesnt stop at shortest iterble like zip()
"""
print(list(it.ziplongest([1,2,3], [6,7,8,9])))
# out => [(1,6), (2,7), (3,8), (None, 9)]
# takes a fill value to replacea all the None

"""
product(*it: iterable) :
returns cartesian product of all elements of all given iterables
product(it, repeat=4) is equivalent to product(it, it, it, it)
------
permutations(it: iterable, length) :
returns all permutations of given elements
of given length
------
combinations(it: iterable, length) :
returns all combinations of given elements
of given length
------
combinations_with_replacements(it: iterable, length) :
returns all combinations with replacements of given elements
of given length
"""
































