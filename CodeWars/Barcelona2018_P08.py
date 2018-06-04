l = list(map(int, input().split()))
s = sum(l)

if (s * 1.6 >= 622):
	print('Yes', end = '')
else:
	print('No', end = '')