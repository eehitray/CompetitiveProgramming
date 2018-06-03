i = int(input())
li = list(map(int, input().split()))

curChange = li[1] - li[0]

for j in range(i):
    for k in range(j + 1, i):
        if ((li[k] - li[j]) > curChange):
            curChange = li[k] - li[j]

if (curChange >= 0):
    print("Profit: ", abs(curChange), sep= '')
else:
    print("Loss: ", abs(curChange), sep= '')

