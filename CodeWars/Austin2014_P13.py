from itertools import permutations

n = int(input())

ar = input().split()
ar.sort()

cs = []

k = int(input())
while (k != 0):
	cs.append(k)
	k = int(input())
perms = list(permutations(ar, 5))
o = []
for word in perms:
	if word not in o:
		o.append(word)

for p in cs:
	if (p > len(o)):
		print(str(len(o)) + ':', ''.join(o[len(o) - 1]))
	else:
		print(str(p) + ':', ''.join(o[p-1]))