num = int(input())

orderQ = []
changeQ = []
changeCopy = []

curBal = []

for i in range(num):
    s = input()
    k = s.split()
    orderQ.append([k[0], int(k[1])])

for j in orderQ:
    if (50 in curBal and len(changeQ) != 0):
        changeQ.pop(0)
        curBal.pop()
    if (j[1] == 100):
        if (50 in curBal):
            curBal.pop()
        else:
            changeQ.append(j[0])
            if (len(changeQ) > len(changeCopy)):
                changeCopy = list(changeQ)
    elif (j[1] == 50):
        curBal.append(50)

if (len(changeCopy) == 0):
    print("None")
else:
    for i in changeCopy:
        print(i, end=' ', flush = True)
