def evalInclude(n):
	tSum = 0
	for i in range(n + 1):
		tSum += (9 * 10**(i-1) * i)
	return tSum

def findDig(num):
	digitsCrossed = 0
	dig = 1

	while (digitsCrossed < num):
		digitsCrossed = evalInclude(dig)
		dig += 1

	dig -= 1

	allUpTill = evalInclude(dig - 1)
	remain = (int) (num - allUpTill - 1)

	firstDigDigNum = 10**(dig-1)

	iPart = remain // dig
	fPart = remain % dig

	for k in range(iPart):
		firstDigDigNum += 1

	t = str(firstDigDigNum)

	return int(t[fPart])

i = findDig(1) * findDig(10) * findDig(100) * findDig(1000) * findDig(10000) * findDig(100000) * findDig(1000000)
print(i)