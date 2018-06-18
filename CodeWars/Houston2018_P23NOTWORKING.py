from queue import PriorityQueue

k = input().split()
rows = int(k[0])
cols = int(k[1])

grid = []

for _ in range(rows):
	temp = list(input())
	grid.append(temp)

def getNeighbours(r, c):
	neigbours = []
	if (r > 0):
		neigbours.append((r - 1, c))
	if (c > 0):
		neigbours.append((r, c - 1))
	if (r < rows - 1):
		neigbours.append((r + 1, c))
	if (c < cols - 1):
		neigbours.append((r, c + 1))
	return neigbours

def dijkstra(startR, startC, endR, endC):
	frontier = PriorityQueue()
	start = (startR, startC)
	end = (endR, endC)
	cameFrom = {}
	costSoFar = {}
	frontier.put(start, 0)
	cameFrom[start] = None
	costSoFar[start] = 0

	while not frontier.empty():
		current = frontier.get()
		neigbours = getNeighbours(current[0], current[1])
		for n in neigbours:
			newCost = costSoFar[current]
			if n == '.':
				newCost += 1
		
			if n not in costSoFar or costSoFar[n] >= newCost or n != '.':
				print(n)
				costSoFar[n] = newCost
				frontier.put(n, newCost)
				cameFrom[n] = current

	return grid[startR][startC], grid[endR][endC], costSoFar[end]

nI = int(input())

for _ in range(nI):
	coords = list(map(int, input().split()))
	start, end, cost = dijkstra(coords[0], coords[1], coords[2], coords[3])
	print(start, "to", end, "takes", str(cost))