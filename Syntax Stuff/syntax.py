# this is a comment
# end of line terminates statement
x = 5

x = 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10
# can be written as:
x = 1 + 2 + 3 + 4 + 5\
  + 6 + 7 + 8 + 9 + 10
# or:
x = (1 + 2 + 3 + 4 + 5 
  + 6 + 7 + 8 + 9 + 10)
  
# two staements can be joined like this:
a = []; b = []

# every variable in python is a pointer
# and an object!

# operators:
a + b # addition
a - b # substraction
a * b # multiplication
a / b # true division (gives a decimal)
a // b # floor division (gives only integral part)
a % b # modulus/ remainder. even floats can undergoe this operation
# 3.5 % 3 is valid
a ** b # exponentiation a ^ b
a & b # bitwise AND
a | b # bitwise OR
a ^ b # bitwise XOR
a << b # left shift
a >> b # right shift
~a # bit negation
a > b # greater than
a >= b # greater than or equal to
a < b # lesser than
a <= b # lesser than or equal to
a = 25
15 < a < 30 # is valid
a and b # logical AND
a or b # logical OR
not a # logical NOT
a != b # not equal to
a is b
a is not b # checks identity
a in b
a not in b # checks membership

## FLOATS
# can be represented as:
y = 1.4e6 # 1.4 * 10^6

# a function that doesnt return anything,
# returns None

# TUPLES ARE IMMUTABLE

## FLOW OF CONTROL:
if <statement>:
    # do this
elif <another statement>:
    # do this:
else:
    # do this
  
for <data> in <iterable>:
    # do this

while <statement>:
    # do this

# if your loop has a break,
# you can check if there has been no break like this:
for <data> in <iterable>:
    if <statement>:
        break
else: # if the loop never broke even once
    # do this

# *args and **kwargs
def catch_everything(*args, **kwargs):
    print(args) # arguments
    print(kwargs) # keyword arguments
 
catch_everything(1, 2, 3, 4, a=1, b=2, c=3)
#OUTPUT
# (1, 2, 3, 4)
# {'a': 1, 'b': 2, 'c': 3}

# sorting by two values:
a = [(1,3), (2,2), (2,1), (1,0)]
a.sort() # works :(
# sort by only one value:
a.sort(key=lambda x:x[0])

# ERRORS:
# common runtime errors:
NameError # something doesnt exist
TypeError # you messed up the data types
ZeroDivisionError # division by zero duh
IndexError # list index out of bounds

# error handling:
try:
    # do this
except Error as e:
    # do this if error e happens
else:
    # do this if try clause succeeds
finally:
    # do this regardless

a = [1,2,3,4,5,6]
# *a will unpack a from a list to separate values
# so,  
c, *d = a
# c => 1
# d => [2,3,4,5,6]
