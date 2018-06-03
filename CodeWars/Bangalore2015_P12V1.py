n = int(input())
li = list(map(int, input().split()))

profit = li[1] - li[0]

for i, o in enumerate(li):
    for j in li[i:]:
        if (j - o >= profit):
            profit = j - o

if (profit >= 0):
    print("Profit: ", profit)
else:
    print("Loss: ", -profit)
