ar = []

k = input().split(' ', 1)
n = int(k[0])
dec = k[1]

curInd = 0
ar.append(dec[0])
iCov = [0]
unCov = [i for i in range(1, n)]
x = -1
while(len(ar) != n):
	#Get current alphabet
	c = dec[curInd]

	#Calculate how much to move
	moveBy = 0
	if not c.isalnum():
		moveBy = 1
	else:
		if c.isupper():
			moveBy = ord(c) -65 + 1
		else:
			moveBy = ord(c) - 97 + 1
	
	#Move in the array of unfilled letters
	while(moveBy != 0):
		if (x == (len(unCov) - 1)):
			x = 0
		else:
			x += 1
		moveBy -= 1

	#t stores the index after the pop
	t =0 

	#Store the current unfilled (about to be filled) letter
	curInd = unCov[x]

	#Store the letter for the next iteration in t
	if (x == len(unCov) - 1):
		t = unCov[0]
	else:
		t = unCov[x + 1]

	#Remove the current unfilled index from the list of unfilled letters
	unCov.pop(x)

	#Edge case wizardry I don't understand
	if (len(ar) == n - 1):
		ar.append(dec[t])

	#In most cases, fill the unfilled letter and set up x for the next iteration
	else:
		ar.append(dec[curInd])
		x = unCov.index(t) - 1

print(''.join(ar))
