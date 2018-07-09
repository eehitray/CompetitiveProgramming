divs = {
	1: 2, 2: 5, 3: 5, 4: 4, 5: 5, 6: 6, 7: 3, 8: 7, 9: 6, 0: 6
}

n = int(input())
ar = []
for _ in range(n):
	ar.append(input())

for x in ar:
	cost = 20
	p = x.split(':')
	hr = p[0]

	for c in hr:
		cost += (15 * divs[int(c)])
	mi = p[1]

	for c in mi:
		cost += (15 * divs[int(c)])
	print(cost, "milliamps")