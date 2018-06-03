from copy import deepcopy

rows = int(input())
cols = int(input())

grid = []

for i in range(rows):
	grid.append(list(input()))

initSea = int(input())
finalSea = int(input())

def getNeighbours(i, j):
	n = []
	notUp = i != 0
	notDown = i != (rows - 1)
	notLeft = j != 0
	notRight = j != (cols - 1)

	if (notUp):
		n.append([i - 1, j])
	if (notDown):
		n.append([i + 1, j])
	if (notLeft):
		n.append([i, j - 1])
	if (notRight):
		n.append([i, j + 1])
	if (notUp and notLeft):
		n.append([i - 1, j - 1])
	if (notUp and notRight):
		n.append([i - 1, j + 1])
	if (notDown and notLeft):
		n.append([i + 1, j - 1])
	if (notDown and notRight):
		n.append([i + 1, j + 1])

	return n, [grid[t[0]][t[1]] for t in n]

for sea in range(initSea, finalSea + 1):
	while True:
		x = deepcopy(grid)

		for i in range(rows):
			for j in range(cols):
				if (grid[i][j].isnumeric() and int(grid[i][j]) <= sea):
					ind, neigh = getNeighbours(i, j)
					if ('.' in neigh):
						grid[i][j] = '.'
		if (x == grid):
			break
	print("Sea level:", sea)
	for p in range(rows):
		for q in range(cols):
			if (grid[p][q] == '.'):
				print('W', sep='', end='')
			else:
				print(' ', sep='', end='')
		print()
