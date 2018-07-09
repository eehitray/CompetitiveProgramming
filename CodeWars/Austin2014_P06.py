negs = ["DON'T", "CAN'T", "ISN'T", "HAVEN'T", "CANNOT", "WOULDN'T", "COULDN'T", "WON'T", "NO", "NOT", "NEVER", "NOBODY", "NOWHERE", "NEITHER", "AIN'T"]
s = input()
ar = []
while (s != '.'):
	ar.append(s)
	s = input()

for x in ar:
	c = 0
	p = x.split()
	for word in p:
		if not (ord(word[len(word) - 1]) >= 65 and ord(word[len(word) - 1]) <= 90):
			word = word[0:len(word) - 1]
		if not (ord(word[0]) >= 65 and ord(word[0]) <= 90):
			word = word[1:len(word)]
		if word in negs:
			c+=1
	print(str(c) + ':', x)