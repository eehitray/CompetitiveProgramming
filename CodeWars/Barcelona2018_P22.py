n = int(input())
baseLen = 4*n - 1
startSpace = baseLen//2
for i in range(n, 0, -1):
	for j in range(i - n + startSpace):
		print(' ', sep='', end='')
	for j in range(n, i - 1, -1):
		print(j, sep='', end='')
	for j in range(i + 1, n + 1):
		print(j, sep='', end='')
	print()

for i in range(1, n + 1):
	for j in range(n - i):
		print(' ', sep='', end='')
	for j in range(n, i, -1):
		print(j, sep='', end='')
	occ = 4*i - 1
	print(str(i) * occ, sep='', end='')
	for j in range(i + 1, n + 1):
		print(j, sep='', end='')
	print()