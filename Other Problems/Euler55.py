count = 0

def checkLychrel(n):
	for i in range(50):
		n += int(str(n)[::-1])
		if (str(n) == str(n)[::-1]):
			return False
	return True

for i in range(1, 10001):
	if (checkLychrel(i)):
		print("Found Lychrel:", i)
		count += 1

print("Lychrels under 10000:", count)