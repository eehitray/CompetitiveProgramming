"""
Dicts are mapping object maps hashable values to arbitrary objects. 
Mappings are mutable objects. 
There is currently only one standard mapping type, the dictionary.
"""

"""
len(d)
Return the number of items in the dictionary d.

d[key]
Return the item of d with key key. Raises a KeyError if key is not in the map.

d[key] = value
Set d[key] to value.

del d[key]
Remove d[key] from d. Raises a KeyError if key is not in the map.

key in d
Return True if d has a key key, else False.

key not in d
Equivalent to not key in d.

iter(d)
Return an iterator over the keys of the dictionary. This is a shortcut for iter(d.keys()).

clear()
Remove all items from the dictionary.

copy()
Return a shallow copy of the dictionary.

classmethod fromkeys(seq[, value])
Create a new dictionary with keys from seq and values set to value.

fromkeys() is a class method that returns a new dictionary. value defaults to None.

get(key[, default])
Return the value for key if key is in the dictionary, else default. If default is not given, it defaults to None, so that this method never raises a KeyError.

items()
Return a new view of the dictionary’s items ((key, value) pairs). See the documentation of view objects.

keys()
Return a new view of the dictionary’s keys. See the documentation of view objects.

pop(key[, default])
If key is in the dictionary, remove it and return its value, else return default. If default is not given and key is not in the dictionary, a KeyError is raised.

popitem()
Remove and return an arbitrary (key, value) pair from the dictionary.

popitem() is useful to destructively iterate over a dictionary, as often used in set algorithms. If the dictionary is empty, calling popitem() raises a KeyError.

setdefault(key[, default])
If key is in the dictionary, return its value. If not, insert key with a value of default and return default. default defaults to None.

update([other])
Update the dictionary with the key/value pairs from other, overwriting existing keys. Return None.

update() accepts either another dictionary object or an iterable of key/value pairs (as tuples or other iterables of length two). If keyword arguments are specified, the dictionary is then updated with those key/value pairs: d.update(red=1, blue=2).

values()
Return a new view of the dictionary’s values. See the documentation of view objects.
"""
