import queue

size = int(input())

mat = []

for i in range(size):
    mat.append(list(map(int, input().split())))


def getNeighbours(i, j, c):
    global size
    global mat
    ret = []

    if (i != size - 1):
        li = [(i + 1, j)]
        if (j != 0):
            li.append((i + 1, j - 1))
        if (j != size - 1):
            li.append((i + 1, j + 1))

        for t in li:
            if (mat[t[0]][t[1]] == c):
                ret.append(t)
    return ret
            

def searchForX(x):
    global size
    q = queue.Queue()
    for j in range(size):
        if (mat[0][j] == x):
            q.put((0, j))
    while not q.empty():
        t = q.get()
        if (t[0] == size - 1):
            return True
        l = getNeighbours(t[0], t[1], x)
        for h in l:
            q.put(h)
    return False

ones = searchForX(1)
twos = searchForX(2)

if (ones and twos):
    print("AMBIGUOUS")
elif (ones):
    print(1)
elif (twos):
    print(2)
else:
    print(0)
