'''
Copying lists:

Copying 1D lists:

a = [1,2,3,4]

1) b = a.copy()
2) b = a[::]
3)
from copy import copy
b = copy(a)

WRONG:
b = a -> modification to either results in modification to other

Copying n-dimensional lists:

from copy import deepcopy
a = [[1,2],[3,4]]
b = deepcopy(a)

-----------------------------

Sorting

list.sort() vs sorted()

list.sort() only works on lists
It's in-place
it has two optional args: key=<a comparator function> and reverse=True or False

Eg: Using the key= arg to sort by second member of tuple
>>> def p(t):
	return t[1]

>>> a = [(1,2), (2,1), (3,0)]
>>> a.sort(key=p)
>>> a
[(3, 0), (2, 1), (1, 2)]

