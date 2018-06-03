dim = int(input())

ar = []
dic = []

matches = []
coords = []
for i in range(dim):
    ar.append(input().split())

wordCount = int(input())

for i in range(wordCount):
    dic.append(input())

def getNeighbours(i, j):
    neighbours = [(i - 1, j - 1), (i - 1, j), (i - 1, j + 1),
                  (i, j - 1),                 (i, j + 1),
                  (i + 1, j - 1), (i + 1, j), (i + 1, j + 1)]
    if (i == 0):
        if (i - 1, j - 1) in neighbours:
            neighbours.remove((i - 1, j - 1))
        if (i - 1, j) in neighbours:
            neighbours.remove((i - 1, j))
        if (i - 1, j + 1) in neighbours:
            neighbours.remove((i - 1, j + 1))
    if (i == dim - 1):
        if (i + 1, j - 1) in neighbours:
            neighbours.remove((i + 1, j - 1))
        if (i + 1, j) in neighbours:
            neighbours.remove((i + 1, j))
        if (i + 1, j + 1) in neighbours:
            neighbours.remove((i + 1, j + 1))
    if (j == 0):
        if (i - 1, j - 1) in neighbours:
            neighbours.remove((i - 1, j - 1))
        if (i, j - 1) in neighbours:
            neighbours.remove((i, j - 1))
        if (i + 1, j - 1) in neighbours:
            neighbours.remove((i + 1, j - 1))
    if (j == dim - 1):
        if (i - 1, j + 1) in neighbours:
            neighbours.remove((i - 1, j + 1))
        if (i, j + 1) in neighbours:
            neighbours.remove((i, j + 1))
        if (i + 1, j + 1) in neighbours:
            neighbours.remove((i + 1, j + 1))

    return neighbours

def exists(i, j):
    if (i < 0 or i >= dim or j < 0 or j >= dim):
        return False
    else:
        return True

def searchForWord(word):
    global ar
    firstChar = word[0]
    for i in range(dim):
        for j in range(dim):
            if (ar[i][j] == firstChar):
                if (len(word) == 1):
                    matches.append(word)
                    return
                else:
                    neighbours = getNeighbours(i, j)
                    secondChar = word[1]
                    for t in neighbours:
                        if (ar[t[0]][t[1]] == secondChar):
                            if (len(word) == 2):
                                matches.append(word)
                                return
                            else:
                                changeX = t[0] - i
                                changeY = t[1] - j
                                curX = t[0]
                                curY = t[1]
                                for char in range(2, len(word)):
                                    curX += changeX
                                    curY += changeY

                                    if(exists(curX, curY)):
                                        if (word[char] == ar[curX][curY]):
                                            if (char == len(word) - 1):
                                                #The code that follows isn't mandatory for the codewars question, it just looks cool
                                                tI = i
                                                tJ = j

                                                while(tI != curX or tJ != curY):
                                                    coords.append((tI, tJ))
                                                    tI += changeX
                                                    tJ += changeY
                                                coords.append((curX, curY))
                                                #Non mandatory code ends here 
                                                matches.append(word)
                                                return
                                        else:
                                            break
                                    else:
                                        break

for word in dic:
    searchForWord(word)
    
print(len(matches))
for w in matches:
    print(w)


#Non mandatory
print()
for i in range(dim):
    for j in range(dim):
        if ((i, j) in coords):
            print(ar[i][j], '', sep=' ', end='')
        else:
            print('.', '', sep=' ', end='')
    print()
