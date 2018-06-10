from itertools import chain
from queue import PriorityQueue
n = int(input())

neighbours = {}
costs = {}


speeds = {'green': 20, 'blue': 30, 'red':40, 'black':50}

for _ in range(n):
    s = input().split()
    if (s[0] == 'L'):  
    	cost = float(s[1])
    	begin = int(s[2])
    	end = int(s[3])
    	if ((begin, end) in costs):
            if ((cost) < costs[(begin, end)]):
                neighbours.setdefault(begin, [])
                neighbours[begin].append(end)
				costs[(begin, end)] = cost
		else:
            neighbours.setdefault(begin, [])
            neighbours[begin].append(end)
            costs[(begin, end)] = cost        
    else:
        speed = speeds[s[1]]
        cost = (float(s[2])/speed) * 3600
        begin = int(s[3])
        end = int(s[4])
        if ((begin,end) in costs):
            if (cost < costs[(begin,end)]):     
                neighbours.setdefault(begin, [])
                neighbours[begin].append(end)
                costs[(begin,end)] = cost
        else:
            neighbours.setdefault(begin, [])
            neighbours[begin].append(end)
            costs[(begin,end)] = cost

start = max(list(neighbours.keys()))
destinations = chain.from_iterable(list(neighbours.values()))
end = min(destinations)
        
frontier = PriorityQueue()
frontier.put(start, 0)
came_from = {}
cost_so_far = {}
came_from[start] = None
cost_so_far[start] = 0

while not frontier.empty():
	current = frontier.get()
	for n in neighbours[current]:
		new_cost = cost_so_far[current] + costs[(current, n)]
		if n not in cost_so_far or new_cost < cost_so_far[n]:
			cost_so_far[n] = new_cost
			priority = new_cost
			frontier.put(n, priority)
			came_from[n] = current
      
print("%.2f" % cost_so_far[end])