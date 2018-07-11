'''FILE I/O'''

# opening a file for writing
file = open('test.txt', 'w')

'''MODES:
'w' => write
'r' => read
'r+' => read and write
'b' => binary
'a' => append
'''

#ALWAYS CLOSE YOUR FILES!!
file.close() 

# better way to open files:
with open('test.txt', 'w') as file:
    file.write('HELLO WORLD!')
#file is closed automagically

#writing into a file
with open('test.txt', 'a') as file:
    file.write('CYKA BLYAT!\n')

#reading into a file
with open('test.txt', 'r') as file:
    print(file.read()) # reads entire file

#reading line by line
with open('test.txt', 'r') as file:
    print(file.readline())

# better way to read lines
with open('test.txt', 'r') as file:
    for line in file:
        print(line)

# all lines in a lis
with open('test.txt', 'r') as file:
    print(file.readlines())

# seekg/p() tellg/p() equivalents
with open('test.txt', 'rb+') as file: 
    file.read(3)
    print(file.tell()) #=> 3
    file.seek(5) # goes to 5th byte from beginning
    print(file.tell())
    file.seek(5, 1) # goes to the fifth byte from current position
    print(file.tell())
    file.seek(5, 2) # seeks the fifth byte before the end
    print(file.tell())