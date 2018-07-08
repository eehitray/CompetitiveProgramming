"""
Textual data in Python is handled with str objects, or strings.

String literals are written in a variety of ways:

Single quotes: 'allows embedded "double" quotes'
Double quotes: "allows embedded 'single' quotes".
Triple quoted: '''Three single quotes''', """Three double quotes"""

String literals that are part of a single expression and have only 
whitespace between them will be implicitly converted to a single string literal. 
That is, ("spam " "eggs") == "spam eggs".

It is an immutable sequence.
"""

# -----METHODS-----
"""
capitalize() => Converts first character to Capital Letter
"""
"""
center(width, fillchar=' ') =>
Pads the string into another string of specified width with specified fill character
 >> "bhargav".center(13, '*')
 ***bhargav***
"""

"""
endswith(char) => checks if string ends with the specified suffix
"""

"""
find(substr,i ,j, k) => returns the lowest index of substring
works just like:
 >> substr in string[i:j:k]
"""

"""
index(substr, i, j, k) => returns index of substring
  just like find
"""

"""
isalnum()	Checks Alphanumeric Character
isalpha()	Checks if All Characters are Alphabets
isdecimal()	Checks Decimal Characters
isdigit()	Checks Digit Characters
isidentifier()	Checks for Valid Identifier
islower()	Checks if all Alphabets in a String are Lowercase
isnumeric()	Checks Numeric Characters
isprintable()	Checks Printable Character
isspace()	Checks Whitespace Characters
istitle()	Checks for Titlecased String
isupper()	returns if all characters are uppercase characters
lower()	returns lowercased string
upper()	returns uppercased string
swapcase()	swap uppercase characters to lowercase; vice versa
join(string)	Returns a Concatenated String
startswith(string)	Checks if String Starts with the Specified String
title()	Returns a Title Cased String
lstrip()	Removes Leading Characters
rstrip()	Removes Trailing Characters
strip()	Removes Both Leading and Trailing Characters
"""

"""
ljust(width)	returns left-justified string of given width
rjust(width)	returns right-justified string of given width
"""

"""
partition(sep)	Returns a Tuple at the first occurence of sep. sep is included in the 3 part tuple
replace(substr)	Replaces Substring Inside
"""
