from math import sqrt
ar = []
i = int(input())

while(i != 0):
	ar.append(i)
	i = int(input())

for t in ar:
	print(t, round((100*sqrt(t) + 201/(t+1) + 1)))