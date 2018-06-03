i = int(input())

fact = 1

for j in range(2, i + 1):
    fact *= j

print(fact)

stF = list(str(fact))
zeroes = 0
for k in range(len(stF) - 1, -1, -1):
    if (stF[k] == '0'):
        zeroes += 1
    else:
        break

print(zeroes)
