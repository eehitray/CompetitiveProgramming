from math import sqrt, ceil
ar = []
i = int(input())

while (i != 0):
	ar.append(i)
	i = int(input())

def cPrime(num):
	for i in range(2, ceil(sqrt(num)) + 1):
		if num % i == 0:
			return False
	return True

for k in ar:
	solns = []
	for j in range(2, (k//2) + 1):
		if(cPrime(j) and cPrime(k - j)):
			solns.append((j, k - j))
	if (len(solns) == 1):
		o = list(sorted(sols[0]))
		print(o[0],'+',o[1],'=',k)
	else:
		l = ()
		diff = float('inf')
		for so in solns:
			if (abs(so[0] - so[1]) < diff):
				l = so
				diff = abs(so[0] - so[1])

		print(l[0],'+',l[1],'=',k)