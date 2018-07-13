'''
Copying lists:

Copying 1D lists:

a = [1,2,3,4]

1) b = a.copy()
2) b = a[::]
3)
from copy import copy
b = copy(a)
4) b = [x for x in a]

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

sorted() is more flexible - it can take basically any iterable and will return a list
As it's returning, it's out-of-place and does not modify the original iterable
Also can take key and reverse

>>> a = '12312'
>>> sorted(a)
['1', '1', '2', '2', '3']

-----------------------------

Reversing
1) Simplest method:
a = [1,2,3]
p = a[::-1]
p is now [3,2,1]

2) list.reverse() and reversed() are similar to list.sort() and sorted()

-----------------------------

Remember, if you forget any syntax, IDLE can help out! Just pass an instance of some class or the class itself to
the help function:

1) help(list)
2) a = []
help(a)
3) help(str)

and so on.

-----------------------------

Be careful with list assignment and multiplicative assignment:

>>> a = [[]]*3
>>> a[0].append(1)
>>> a
[[1], [1], [1]]

All lists were linked there.

-----------------------------

Some super common methods:

str.split(delimeter, number of times to split)
a = '1234 abc def'

k = a.split(' ', 1)
k is ['1234', 'abc def'] - only one split took place

str.strip(optional char)
removes given char from start,end of string. if char not specified it removes whitespace.

map(method to apply, list to apply to): returns an iterable. you're most likely looking for list(map(...))

list.clear
list.append
list.extend
list.index
list.pop(index optional)
list.remove -> removes first occurence

str. :
capitalize -> first letter capitalized
center(n) -> centers str in n characters
count(sub, optional start, optional end) -> counts occurences of sub in [start:end]
startswith and endswith(sub, optional start, optional end)
find(sub, optional start, optional end) -> returns first index of occurence of sub. if not found returns -1
format() -> ultra useful method. go through https://mkaz.blog/code/python-string-format-cookbook/ DON'T FORGET TO GO THROUGH IT
isalnum, isalpha, isdecimal, isdigit, islower, isspace,
isupper, join [concatenates], ljust and rjust (n characters),
lower and upper -> return lowercased and uppercased copies and not inplace modify
istitle -> checks title case (check .title())
rfind -> find() but from the right of the string
partition(sep):
partition(...)
 |      S.partition(sep) -> (head, sep, tail)
 |      
 |      Search for the separator sep in S, and return the part before it,
 |      the separator itself, and the part after it.  If the separator is not
 |      found, return S and two empty strings.
 |  
 |  
 lstrip and rstrip -> strip but only from left or right
 replace(old, new, count = 1) -> out of place method to return a string of all copies of old replaced with new
 rpartition -> partition but from the right of the string
 swapcase -> out of place; returns all upper case -> lower case and vice versa
 title -> out of place, returns title cased string:
 words start with title case characters, all remaining cased characters have lower case
 translate -> seems super useful. to use:

 table = str.maketrans('123', 'abc'): maps 1->a, 2->b and so on
 or
 table = str.maketrans(dictionary): self explanatory
 or
 table = str.maketrans('123', 'abc', 'xyz'): maps 1->a, 2->b and so on. maps x,y,z to None.

 now:

 string.translate(table) returns a copy where characters are translated. 1 becomes a, and so on. chars mapped to None are removed.
