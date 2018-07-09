n  = int(input())

ar = []

for _ in range(n):
	ar.append(list(map(int, input().split())))

for c in ar:
	r = 0
	for i in range(0, len(c), 2):
		r += c[i]
	r*=3
	for i in range(1, len(c), 2):
		r += c[i]
	r %= 10
	if (r != 0):
		r = 10 - r
	for i in c:
		print(i, sep = '', end=' ')
	print(r, sep='')