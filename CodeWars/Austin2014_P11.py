st = input()
ar = []
#print(st)
while(st != "-1 -1 -1 -1 -1 -1"):
	ar.append(list(map(int, st.split())))
	st = input()
#print(ar)
for c in ar:
	
	n = 1
	while (True):
		#print(n)
		if (n % c[0] == c[3] and n % c[1] == c[4] and n % c[2] == c[5]):
			print(n)
			break
		n += 1