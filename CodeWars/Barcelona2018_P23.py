st = list(input())

stl = len(st)

cols = 4
rows = 3

while (cols * rows < stl):
	cols += 4
	rows += 3

for i in range(rows):
	for j in range(cols):
		if (i * cols + j) <= (len(st) - 1):
			letter = st[i*cols + j]
			if(letter.isalpha()):
				if (letter == 'z'):
					letter = chr(ord('A') -1)
				if (letter == 'Z'):
					letter = chr(ord('a') -1)
				print(chr(ord(letter)+1),sep='',end='')
			else:
				print(letter,sep='',end='')
		else:
			if (i == j):
				print('#', sep='', end='')
			else:
				print('\"', sep='', end='')
		if (j != cols - 1):
			print(' ', sep='',end='')
	print('')