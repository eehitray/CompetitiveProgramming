n = int(input())

rooms = {}

for i in range(n):
	a = list(map(int, input().split()))
	rooms[a[0]] = a[1]

keys = list(rooms.keys())
values = list(rooms.values())

c = 0

def depSearch(visited, i):
	global c
	if (i == 0):
		c += 1
	elif (i not in visited):
		visited.append(i)
		depSearch(visited, rooms[i])

for i in keys:
	if i == 0:
		c += 1
	else:
		visited = []
		depSearch(visited, i)


print(c, end='')