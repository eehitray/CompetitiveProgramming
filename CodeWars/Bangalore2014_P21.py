from queue import PriorityQueue

k = input().split()
rooms = int(k[0])
paths = int(k[1])

neibs = {}

for i in range(paths):
	t = input().split(',')
	neibs.setdefault(t[0], [])
	neibs[t[0]].append(t[1])
	neibs.setdefault(t[1], [])
	neibs[t[1]].append(t[0])

cases = int(input())
caseDests = []

for i in range(cases):
	p = input().split(',')
	start = p[0]
	end = p[1]
	frontier = PriorityQueue()
	frontier.put(start, 0)
	cameFrom = {}
	costSoFar = {}

	cameFrom[start] = None
	costSoFar[start] = 0

	while (not frontier.empty()):
		current = frontier.get()

		for n in neibs[current]:
			cost = costSoFar[current] + 1
			if (n not in costSoFar or costSoFar[n] > cost):
				costSoFar[n] = cost
				frontier.put(n, cost)
				cameFrom[n] = current
	print(costSoFar[end])


