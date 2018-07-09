s = input()
ar=[]
while (s!='0 $'):
	p = s.split()
	ar.append(p[0:len(p) - 1])
	s = input()

for x in ar:
	t = x[1:len(x)]
	print(t[-1*int(x[0])])