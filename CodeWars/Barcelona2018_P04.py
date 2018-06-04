age = int(input())
planet = input()

x = 0
if (planet == 'Mercury'):
	x = 88
elif (planet == 'Venus'):
	x = 225
elif (planet == 'Earth'):
	x = 365
elif (planet == 'Mars'):
	x = 687
elif (planet == 'Jupiter'):
	x = 4333
elif (planet == 'Saturn'):
	x = 10759
elif (planet == 'Uranus'):
	x = 30689
elif (planet == 'Neptune'):
	x = 60182

print((age * x) // 365, end='')

