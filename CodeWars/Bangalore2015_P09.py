def getNum(st):
    no = ''
    st += 'x'
    for i in range(len(st)):
        if st[i].isdigit():
            for j in range(i, len(st)):
                if st[j].isdigit():
                    no += st[j]
                else:
                    return int(no)

n = int(input())

li = []

for i in range(n):
    li.append(input())

li.sort(key=getNum)

for s in li:
    print(s)
