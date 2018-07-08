"""
A set object is an unordered collection of distinct hashable objects. 
Common uses include membership testing, removing duplicates from a sequence, 
and computing mathematical operations such as intersection, union, difference, and symmetric difference.
"""

"""
operations

len(s)
Return the number of elements in set s (cardinality of s).

x in s
Test x for membership in s.

x not in s
Test x for non-membership in s.

isdisjoint(other)
Return True if the set has no elements in common with other. Sets are disjoint if and only if their intersection is the empty set.

issubset(other)
set <= other
Test whether every element in the set is in other.

set < other
Test whether the set is a proper subset of other, that is, set <= other and set != other.

issuperset(other)
set >= other
Test whether every element in other is in the set.

set > other
Test whether the set is a proper superset of other, that is, set >= other and set != other.

union(*others)
set | other | ...
Return a new set with elements from the set and all others.

intersection(*others)
set & other & ...
Return a new set with elements common to the set and all others.

difference(*others)
set - other - ...
Return a new set with elements in the set that are not in the others.

symmetric_difference(other)
set ^ other
Return a new set with elements in either the set or other but not both.

copy()
Return a new set with a shallow copy of s.

update(*others)
set |= other | ...
Update the set, adding elements from all others.

intersection_update(*others)
set &= other & ...
Update the set, keeping only elements found in it and all others.

difference_update(*others)
set -= other | ...
Update the set, removing elements found in others.

symmetric_difference_update(other)
set ^= other
Update the set, keeping only elements found in either set, but not in both.

add(elem)
Add element elem to the set.

remove(elem)
Remove element elem from the set. Raises KeyError if elem is not contained in the set.

discard(elem)
Remove element elem from the set if it is present.

pop()
Remove and return an arbitrary element from the set. Raises KeyError if the set is empty.

clear()
Remove all elements from the set.
"""
