from queue import PriorityQueue

gridCosts = []

for i in range(4):
	gridCosts.append(list(map(int, input().split(' '))))

def getCostTo(i, j):
	return gridCosts[i][j]

def getNeighbours(i, j):
	indices = []
	notRight = j != 3
	notDown = i != 3

	if (notRight):
		indices.append((i, j+1))
	if(notDown):
		indices.append((i + 1, j))
	if (notRight and notDown):
		indices.append((i + 1, j +1))

	return indices

frontier = PriorityQueue()
frontier.put((0, 0), 0)
cameFrom = {}
costSoFar = {}
cameFrom[(0, 0)] = None
costSoFar[(0, 0)] = 0

while not frontier.empty():
	current = frontier.get()

	if current == (3,3):
		break

	for nextLoc in getNeighbours(current[0], current[1]):
		#print(nextLoc[0], nextLoc[1])
		newCost = costSoFar[current] + getCostTo(nextLoc[0], nextLoc[1])
		if nextLoc not in costSoFar or newCost < costSoFar[nextLoc]:
			costSoFar[nextLoc] = newCost
			frontier.put(nextLoc, newCost)
			cameFrom[nextLoc] = current

locs = [(3,3)]

while (0,0) not in locs:
	locs.append(cameFrom[locs[-1]])

locs.reverse()

steps = ''
for p in range(1, len(locs)):
	a = locs[p]
	b = locs[p - 1]

	bo = a[0] != b[0] and a[1] == b[1]
	r = a[1] != b[1] and a[0] == b[0]
	d = a[0] != b[0] and a[1] != b[1]

	if (bo):
		steps += 'B'
	elif (r):
		steps += 'R'
	elif (d):
		steps += 'D'

print("The shortest path is", steps)

costs = [getCostTo(t[0], t[1]) for t in locs]
print("Time taken is 0", sep='', end='')
for t in range(1, len(costs)):
	print('+', costs[t],sep='',end='')

print('=',str(sum(costs)) + ' hrs', sep = '', end='')
