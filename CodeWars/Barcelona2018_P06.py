i = int(input())

x = ''
for j in range(i, -1, -1):
	x += str(j)
	x += ' '

print(x[0:len(x) - 1])