from queue import Queue

k = input().split()

parkingSpaces = int(k[0])
cars = int(k[1])

weights = {}
waiting = Queue(maxsize = cars)
spots = []
rates = []
spotTakenBy = {}
revenue = 0

for _ in range(parkingSpaces):
	rates.append(int(input()))
	spots.append(None)

for i in range(cars):
	weights[i] = int(input())

for _ in range(cars*2):
	car = int(input())
	if (not waiting.empty()) and None in spots:
		cur = waiting.get()
		for index, status in enumerate(spots):
			if (status is None):
				spots[index] = cur
				spotTakenBy[cur] = index
				revenue += weights[cur - 1] * rates[index]
				break

	if (car > 0):
		flag = False
		for index, status in enumerate(spots):
			if (status is None):
				
				spots[index] = car
				spotTakenBy[car] = index
				revenue += weights[car - 1] * rates[index]
				flag = True
				break
		if (flag == False):
			waiting.put(car)
	else:

		carVal = -1 * car
		spotOfCar = spotTakenBy[carVal]
		spots[spotOfCar] = None
		del spotTakenBy[carVal]

print(revenue)