d = {}

for _ in range(int(input())):
	k = input().split()
	d[k[0]] = (k[1], k[2])

children = []
for t in list(d.values()):
	if (t[0] not in children):
		children.append(t[0])
	if (t[1] not in children):
		children.append(t[1])

parents = list(d.keys())
head = ''
for p in parents:
	if p not in children:
		head = p
		break


def traverse(ch):
	if ch in d:
		childs = d[ch]
		#print("Children of", ch, childs)
		if (childs[0] != '.'):
			traverse(childs[0])
		if (childs[1] != '.'):
			traverse(childs[1])
		print(ch)
	else:
		print(ch)

traverse(head)