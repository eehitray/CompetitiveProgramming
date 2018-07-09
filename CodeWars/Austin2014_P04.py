ac = int(input())
n = int(input())

ar = []

for _ in range(n):
	ar.append(input().split())

error = float('inf')
k = []
for c in ar:
	if (abs(ac - int(c[0])) < error):
		p = []
		k.clear()
		k.append(c[1])
		error = abs(ac - int(c[0]))
	elif (abs(ac - int(c[0])) == error):
		k.append(c[1])
		error = abs(ac - int(c[0]))
for name in k:
	print(name, end=' ')