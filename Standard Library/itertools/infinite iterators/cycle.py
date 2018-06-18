import itertools as it
"""
Iterators that return an infinite stream of data.
"""

"""
cycle(it: iterable) : 
loops infinitly through a iterable (list, string, tuple)
"""

count = 0

for i in it.cycle("EEHIT"):
    print(i, end=' ')
    count += 1
    if count == 100:
        break
# out => E E H I T E E H I T E E ...

# genexps:
gen = (x for x in it.cycle('EEHIT'))