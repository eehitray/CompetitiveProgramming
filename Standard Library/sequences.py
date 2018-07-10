"""
There are 3 types of sequences in python: lists, tuples, ranges
Tuples and ranges are immutable, lists are mutable
"""

#OPERATIONS COMMON TO BOTH SEQUENCE TYPES:
"""
Taking a sequence s:
x in s => True if an item of s is equal to x, else False
x not in => False if an item of s is equal to x, else True
s + t	=> the concatenation of s and t
s * n or n * s => equivalent to adding s to itself n times
s[i] => ith item of s, origin 0
s[i:j] => slice of s from i to j
s[i:j:k] => slice of s from i to j with step k
len(s) => length of s	 
min(s) => smallest item of s	 
max(s) => largest item of s	 
s.index(x[, i[, j]]) => index of the first occurrence of x in s (at or after index i and before index j)
s.count(x) => total number of occurrences of x in s
"""

"""
NOTES:
1. Creating a multi dimensional list like this:
  >> arr = [[]] * 3
  >> arr[0].append(3)
  >> arr
  [[3], [3], [3]]
can be dangerous.  [[]] is a one-element list containing an empty list, so all three elements of [[]] * 3 are 
references to this single empty list. Modifying any of the elements of lists modifies this single list. 
You can create a list of different lists this way:
  >> lists = [[] for i in range(3)]

2. If i or j is negative, the index is relative to the end of sequence s: len(s) + i or len(s) + j is substituted. 
But note that -0 is still 0.

3. Concatenating immutable sequences always results in a new object.

4. index raises ValueError when x is not found in s.
"""
