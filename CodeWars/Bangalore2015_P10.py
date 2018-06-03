r,c = list(map(int, input().split()))

mat = []

for i in range(r):
    mat.append(input().split())

rtm = []
ctm = []

for i in range(r):
    for j in range(c):
        if (mat[i][j] == '$'):
            rtm.append(i)
            ctm.append(j)

k = '$ ' * c
k = k[0:len(k) - 1]
for i in range(r):
    if (i in rtm):
        print(k)
    else:
        tp = ''
        for j in range(c):
            if (j in ctm):
                tp += '$ '
            else:
                tp += mat[i][j]
                tp += ' '
        tp = tp[0:len(tp) - 1]
        print(tp)
