from queue import PriorityQueue

cols = int(input())
rows = int(input())

nwalls = int(input())

walls = []

for _ in range(nwalls):
	k = list(map(int, input().split(',')))
	walls.append((k[0], rows - 1 - k[1], k[2] - 1, rows - 1 - k[3]))
	
allWallCoords = []

for wallSet in walls:
	x1 = wallSet[0]
	y1 = wallSet[1]
	x2 = wallSet[2]
	y2 = wallSet[3]

	if (x1 == x2 + 1):
		for y in range(min(y1, y2), max(y2, y1) + 1):
			allWallCoords.append((x1, y))

	elif (y1 == y2):
		for x in range(min(x1, x2), max(x2, x1) + 1):
			allWallCoords.append((x, y1))

grid = []

for r in range(rows):
	row = []
	for c in range(cols):
		if ((c, r) in allWallCoords):
			row.append('W')
		else:
			row.append('C')

	grid.append(row)

def isTraversable(i, j):
	if (i < 0 or i >= cols or j < 0 or j >= rows or grid[j][i] == 'W'):
		return False
	return True

def getTraversableNeighbours(i, j):
	n = []
	for x in range(i - 1, i + 2):
		for y in range(j - 1, j + 2):
			if ((x != i or y != j) and (x != i - 1 or y != j -1) and (x != i - 1 or y != j +1) and (x != i + 1 or y != j - 1) and (x != i + 1 or y != j + 1) and isTraversable(x, y)):
				n.append((x, y))
	return n

start = (0, rows - 1)
frontier = PriorityQueue()
frontier.put(start, 0)
came_from = {}
cost_so_far = {}
came_from[start] = None
cost_so_far[start] = 0

while not frontier.empty():
   current = frontier.get()

   for next in getTraversableNeighbours(current[0], current[1]):
      new_cost = cost_so_far[current] + 1
      if next not in cost_so_far or new_cost < cost_so_far[next]:
         cost_so_far[next] = new_cost
         priority = new_cost
         frontier.put(next, priority)
         came_from[next] = current

if ((cols - 1, 0) in cost_so_far and isTraversable(0, rows - 1)):
	print(cost_so_far[(cols - 1, 0)])
else:
	print('-1')