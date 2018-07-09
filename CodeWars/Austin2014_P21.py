from itertools import permutations

states = []

for _ in range(6):
	states.append(input())
names = []
for state in states:
	k = state.split()
	if (k[0] not in names):
		names.append(k[0])
	if ("HIGHER" in k or "ADJACENT" in k):
		nsub = k[-1]
		if nsub not in names:
			names.append(nsub)

p = permutations(names, 5)

for trial in p:
	flag = 1
	for s in states:
		t = s.split()
		if ("NOT ON FLOOR " in s):
			if (trial[int(t[-1]) - 1] == t[0]):
				flag = 0
				break
		elif ("NOT ON FLOORS " in s):
			if (trial[int(t[-1]) - 1] == t[0] or trial[int(t[-3]) - 1] == t[0]):
				flag = 0
				break
		elif ("ON HIGHER FLOOR THAN" in s):
			p1 = trial.index(t[0])
			p2 = trial.index(t[-1])
			if not (p1 > p2):
				flag = 0
				break
		elif ("NOT ON ADJACENT FLOOR TO" in s):
			p1 = trial.index(t[0])
			p2 = trial.index(t[-1])
			if (p2 - 1 == p1 or p2 + 1 == p1):
				flag = 0
				break
		else:
			p1 = trial.index(t[0])
			p2 = trial.index(t[-1])
			if not (p2 - 1 == p1 or p2 + 1 == p1):
				flag = 0
				break
	if (flag == 1):
		for i, j in enumerate(list(reversed(trial))):
			print(5 - i, j)

