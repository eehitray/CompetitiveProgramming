from copy import deepcopy
turns = int(input())
size = int(input())

k = []
for i in range(size):
	k.append(input().split(' '))

q = deepcopy(k)

'''
def getNeighbours(board, i, j):
	n = []
	notUp = i != 0
	notDown = i != (size - 1)
	notLeft = j != 0
	notRight = j != (size - 1)

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

	return n, [board[t[0]][t[1]] for t in n]	
'''

def traversableCellExists(i, j):
	if (i >= 0 and i <= size -1 and j >= 0 and j <= size - 1):
		return True
	return False

def getNeighbours(board, i, j):
	n = []
	for p in range(i - 1, i + 2):
		for q in range(j - 1, j + 2):
			if ((p != i or q != j) and traversableCellExists(p, q)):
				n.append((p, q))
	return n, [board[t[0]][t[1]] for t in n]

def gol(board):
	global q
	for r in range(size):
		for c in range(size):
			ind, neigh = getNeighbours(board, r, c)
			#print(board,sep='!!')
			hashes = neigh.count('#')
			if (board[r][c] is '.'):
				if (hashes == 3):
					q[r][c] = '#'
			else:
				if (hashes > 3 or hashes < 2):
					q[r][c] = '.'

for it in range(turns):
	p = deepcopy(k)
	gol(p)
	k = deepcopy(q)

for i in range(size):
	for j in range(size):
		print(k[i][j], sep='', end='')
		if (j != size - 1):
			print(' ', sep='', end='')
	if (i != size - 1):
		print('')
