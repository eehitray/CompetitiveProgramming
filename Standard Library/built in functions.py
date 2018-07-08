"""
abs(x)
Return the absolute value of a number. 
The argument may be an integer or a floating point number. 
If the argument is a complex number, its magnitude is returned.

all(iterable)
Return True if all elements of the iterable are true (or if the iterable is empty).

bin(x)
Convert an integer number to a binary string prefixed with “0b”. 

chr(i)
Return the string representing a character whose Unicode code point is the integer i. 
For example, chr(97) returns the string 'a', while chr(8364) returns the string '€'. This is the inverse of ord().

class complex([real[, imag]])
Return a complex number with the value real + imag*1j or 
convert a string or number to a complex number. 
If the first parameter is a string, it will be interpreted as a complex number and 
the function must be called without a second parameter. The second parameter can never be a string.

divmod(a, b)
Take two (non complex) numbers as arguments and return a pair of numbers consisting of their 
quotient and remainder when using integer division. With mixed operand types, the rules for 
binary arithmetic operators apply. For integers, the result is the same as (a // b, a % b). 
For floating point numbers the result is (q, a % b), where q is usually math.floor(a / b) 
but may be 1 less than that. In any case q * b + a % b is very close to a, 
if a % b is non-zero it has the same sign as b, and 0 <= abs(a % b) < abs(b).

filter(function, iterable)
Construct an iterator from those elements of iterable for which function returns true. 
iterable may be either a sequence, a container which supports iteration, or an iterator. 
If function is None, the identity function is assumed, that is, all elements of iterable that are false are removed.
Note that filter(function, iterable) is equivalent to the generator expression 
(item for item in iterable if function(item)) if function is not None and (item for item in iterable if item) if function is None.
See itertools.filterfalse() for the complementary function that returns elements of iterable for which function returns false.

hex(x)
Convert an integer number to a lowercase hexadecimal string prefixed with “0x”.

input([prompt])
If the prompt argument is present, it is written to standard output without a trailing newline.

isinstance(object, classinfo)
Return true if the object argument is an instance of the classinfo argument, or of a (direct, indirect or virtual) subclass thereof.

issubclass(class, classinfo)
Return true if class is a subclass (direct, indirect or virtual) of classinfo.

len(s)
Return the length (the number of items) of an object.

map(function, iterable, ...)
Return an iterator that applies function to every item of iterable, yielding the results.

max(iterable, *[, key, default])
max(arg1, arg2, *args[, key])
Return the largest item in an iterable or the largest of two or more arguments.
key argment in iterables works like in list.sort()

min(iterable, *[, key, default])
min(arg1, arg2, *args[, key])
Return the smallest item in an iterable or the smallest of two or more arguments.
key argment in iterables works like in list.sort()

oct(x)
Convert an integer number to an octal string prefixed with “0o”. 

ord(c)
Given a string representing one Unicode character, return an integer representing the Unicode code point of that character. 
For example, ord('a') returns the integer 97 and ord('€') (Euro sign) returns 8364. This is the inverse of chr().

pow(x, y[, z])
Return x to the power y; if z is present, return x to the power y, modulo z 
(computed more efficiently than pow(x, y) % z). 
The two-argument form pow(x, y) is equivalent to using the power operator: x**y.

print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
Print objects to the text stream file, 
separated by sep and followed by end. sep, end, file and flush, if present, must be given as keyword arguments.

range(stop)
range(start, stop[, step])
Rather than being a function, range is actually an immutable sequence type. returns specified range of integers

reversed(seq)
Return a reverse iterator. seq must be an object which has a __reversed__() method.

round(number[, ndigits])
Return number rounded to ndigits precision after the decimal point. 
If ndigits is omitted or is None, it returns the nearest integer to its input.

sorted(iterable, *, key=None, reverse=False)
Return a new sorted list from the items in iterable.
Has two optional arguments which must be specified as keyword arguments.
key specifies a function of one argument that is used to extract a comparison key from each list element: key=str.lower. 
The default value is None (compare the elements directly).
reverse is a boolean value. If set to True, then the list elements are sorted as if each comparison were reversed.

sum(iterable[, start])
Sums start and the items of an iterable from left to right and returns the total. 
start defaults to 0. The iterable’s items are normally numbers, and the start value is not allowed to be a string.

zip(*iterables)
Make an iterator that aggregates elements from each of the iterables.

Returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the argument sequences or iterables. 
The iterator stops when the shortest input iterable is exhausted. With a single iterable argument, it returns an iterator of 1-tuples.
"""
