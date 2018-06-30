import math

"""
math.ceil(x)
returns smallest integer greater than x
"""

print(math.ceil(1.5)) # => 2

"""
math.copysign(x, y)
returns absolute value of x but with the dign of y
"""

print(math.copysign(1.5, -1)) # => -1.5

"""
math.factorial(x)
returns factorial of x
"""

print(math.factorial(5)) # => 120

"""
math.floor(x)
returns greatest intgere small than x
"""

print(math.floor(1.2)) # => 1

"""
math.fabs(x)
returns absolute value of x
"""

print(math.fabs(x))

"""
math.fmod(x, y)
returns x % y. Best suited for floats.
"""

print(math.fmod(5, 10)) # => 5

"""
math.frexp(x)
returns (m, e) where x == m * 2**e
"""

print(math.frexp(10)) # => (0.625, 4)

"""
math.fsum(iterable)
returns an accurate floating point sum of values in the iterables.
avoids loss of precision
"""

print(sum([.1, .1, .1, .1, .1, .1, .1, .1, .1, .1])) # => 0.9999999999999999
print(math.fsum([.1, .1, .1, .1, .1, .1, .1, .1, .1, .1]))
# => 1.0

"""
math.gcd(x, y)
returns greatest common divisor of x and y
"""

math.gcd(4, 8) # => 4

"""
math.isclose(a, b, *, rel_tol=1e-09, abs_tol=0.0)
returns True if the values a and b are close to each other and
False otherwise.
whether or not two values are considered close is determined
according to given absolute and relative tolerances.

math.isfinite(x)
returns True if x is neither infinity or NaN

math.isinf(x)
returns True if x is +ve or -ve infinity

math.isnan(x)
returns True if a is NaN
"""

"""
math.ldexp(x, i)
returns x * 2**i
inverse of math.frexp()
"""

math.ldexp(0.625, 4) # => 10

"""
math.modf(x)
returns integral and fractional part of x
"""

math.modf(1.25) # => (1.0, 0.25)

"""
math.trunc(x)
returns x truncated to an integer
"""













































































































