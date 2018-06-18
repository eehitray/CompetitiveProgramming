import itertools as it
"""
Iterators that return an infinite stream of data.
"""

"""
repeat(x: anything, n=inf) :
repeats the element for ever.
optional argument will make the genrator repeat the element n times
"""

for i in it.repeat('NRG'):
    print(i, end=' ')
    # prints forever ...

for i in it.repeat('NRG', 3):
    print(i, end=' ')
    # repeats 3 times

# listcomps
arr = [x for x in it.repeat('NRG', 100)]

# genexps
gen = (x for x in it.repeat('NRG'))