"""
Lists are mutable sequences
see mutable sequences.py for common operations on mutable sequences

sort is a new method for lists

sort(*, key=None, reverse=False)

The value of the key parameter should be a function that takes a single argument and returns a key to use for sorting purposes. 

for example, a case insensitive string sort:
 >> "This is a test string from Andrew".split().sort(key=str.lower)
 ['a', 'Andrew', 'from', 'is', 'string', 'test', 'This']
 
A common pattern is to sort complex objects using some of the object's indices as a key. For example:

 >> class Student:
        def __init__(self, name, grade, age):
                self.name = name
                self.grade = grade
                self.age = age
        def __repr__(self):
                return repr((self.name, self.grade, self.age))
        def weighted_grade(self):
                return 'CBA'.index(self.grade) / float(self.age)

  >> student_objects = [
        Student('john', 'A', 15),
        Student('jane', 'B', 12),
        Student('dave', 'B', 10),
     ]
  
  >> sorted(student_objects, key=lambda student: student.age)   # sort by age
  [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
  
  >> student_tuples = [
        ('john', 'A', 15),
        ('jane', 'B', 12),
        ('dave', 'B', 10),
     ]
  >> sorted(student_tuples, key=lambda student: student[2])   # sort by age
  [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
  
-----Operator Module Functions-----
The key-function patterns shown above are very common, 
so Python provides convenience functions to make accessor functions easier and faster. 
The operator module has itemgetter, attrgetter, and methodcaller function.

Using those functions, the above examples become simpler and faster.

  >> from operator import itemgetter, attrgetter, methodcaller

  >> sorted(student_tuples, key=itemgetter(2))
  [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]

  >> sorted(student_objects, key=attrgetter('age'))
  [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
  
The operator module functions allow multiple levels of sorting. For example, to sort by grade then by age:
  
  >> sorted(student_tuples, key=itemgetter(1,2))
  [('john', 'A', 15), ('dave', 'B', 10), ('jane', 'B', 12)]

  >> sorted(student_objects, key=attrgetter('grade', 'age'))
  [('john', 'A', 15), ('dave', 'B', 10), ('jane', 'B', 12)]

The third function from the operator module, methodcaller is used in the following example in which the weighted grade of each student is shown before sorting on it:

  >> [(student.name, student.weighted_grade()) for student in student_objects]
  [('john', 0.13333333333333333), ('jane', 0.08333333333333333), ('dave', 0.1)]
  >> sorted(student_objects, key=methodcaller('weighted_grade'))
  [('jane', 'B', 12), ('dave', 'B', 10), ('john', 'A', 15)]
  
 the third argument specifies wether the list must be sorted in ascending or descending.
 """
