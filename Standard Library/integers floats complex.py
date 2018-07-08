"""
operations supported by integers floats complex numbers:

x + y	sum of x and y	 	 
x - y	difference of x and y	 	 
x * y	product of x and y	 	 
x / y	quotient of x and y	 	 
x // y	floored quotient of x and y	
x % y	remainder of x / y
-x	x negated	 	 	 
abs(x)	absolute value or magnitude of x	
int(x)	x converted to integer
float(x)	x converted to floating point	
complex(re, im)	a complex number with real part re, imaginary part im. im defaults to zero.	
c.conjugate()	conjugate of the complex number c	 	 
divmod(x, y)	the pair (x // y, x % y)	
pow(x, y)	x to the power y	
x ** y	x to the power y

Python defines pow(0, 0) and 0 ** 0 to be 1, as is common for programming languages.

Bitwise operations only make sense for integers.
x | y	bitwise or of x and y	 
x ^ y	bitwise exclusive or of x and y	 
x & y	bitwise and of x and y	 
x << n	x shifted left by n bits
x >> n	x shifted right by n bits	
~x	the bits of x inverted	 

int.bit_length()
Return the number of bits necessary to represent an integer in binary, excluding the sign and leading zeros

float.as_integer_ratio()
Return a pair of integers whose ratio is exactly equal to the original float and with a positive denominator. 

float.is_integer()
Return True if the float instance is finite with integral value, and False otherwise:
"""
