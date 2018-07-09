s = input()
ar = []

while (s != '.'):
	ar.append(s)
	s = input()

for x in ar:
	#print(x)
	flag = 0
	for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
		#print(x, c)
		if (c not in x):
			flag = 0
			break
		else:
			flag = 1
	if flag == 0:
		print("NEITHER:", x)
	else:
		alphas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
		crossed = []
		flag2 = 0
		for char in x:
			if (ord(char) >= 65 and ord(char) <= 90):
				if char in crossed:
					print("PANAGRAM:", x)
					flag2 = 0
					break
				else:
					crossed.append(char)
					flag2 = 1
		if (flag2 == 1):
			print("PERFECT", x)
