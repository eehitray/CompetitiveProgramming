s = ''

l = []
while (s != '0'):
	s = input()
	l.append(int(s))

l.pop()

gpu = l[0]
c = 0
for i in range(1, len(l)):
	if (l[i] <= gpu):
		c += 1
print(c)