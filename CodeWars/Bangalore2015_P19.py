def subInLine(line, pts):
    rel1 = pts[1] + line[0]*pts[0] + line[1]
    rel2 = pts[3] + line[0]*pts[2] + line[1]
    return rel1*rel2
number = int(input())
allCoords = input()
allCoords = [float(i) for i in allCoords.split()]
ar = []
for i in range(0, 4*number, 4):
    ar.append(tuple(allCoords[i:i+4]))
dic = {}
for s in ar:
    m = (s[3] - s[1])/(s[2] - s[0])
    c = s[1] - m*s[0]
    dic[s] = [-m, -c]
count = 0
res = []
for coord in list(dic.keys()):
    x = dic.pop(coord)
    for othercoord in list(dic.keys()):
        if (subInLine(dic[othercoord], coord) < 0 and subInLine(x, othercoord) < 0):
            count += 1
            p = (x[1] - dic[othercoord][1])/(dic[othercoord][0] - x[0])
            q = -x[1] - x[0]*p
            res.append([p, q])
print(count)
for j in res:
    k = ['%.2f' % i for i in j]
    print(*k, sep = ' ')

