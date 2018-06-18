import itertools as it
"""
Iterators that return an infinite stream of data.
"""

"""
count(start: int/float, step: int/float) :
returns an iterator that iterates through an
set of infinite set of numbers starting with start
and with a step.
"""

# USES =>

# infinte range:
for i in it.count():
    print(i, end=' ')
    if i == 100:
        break
# out => 1 2 3 4 5 6 ... 100

# arithmetic progressions
for i in it.count(2.5, 0.5):
    print(i, end=' ')
    if i > 5:
        break
# out => 2.5 3 3.5 4 4.5 5 5.5

# generator comprehension
gen1 = (x for x in it.count()) # infinite range
gen2_1 = (x for x in it.count(2, 2)) # AP
gen2_2 = (2 + 2 * i for i in it.count()) # AP style 2

"""
use gen1, gen2 like this:
"""

for i in gen1:
    # code goes here
    break 