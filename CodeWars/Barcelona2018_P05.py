name = input()
age = input()
gender = input()
city = input()
sport = input()
team = input()
job = input()

pronoun = {'boy': 'he', 'girl': 'she'}
cPronoun = {'boy': 'He', 'girl': 'She'}

pPronoun = {'boy': 'his', 'girl': 'her'}

print(name, ' is a ', age, ' year-old ', gender, '. ', cPronoun[gender], ' is living with ', pPronoun[gender], ' parents in an apartment in the centre of ', city, ', where ', pronoun[gender], ' hangs out with ', pPronoun[gender], ' friends. Moreover, in ', pPronoun[gender], ' free time ', pronoun[gender], ' plays ', sport, ' in a team called ', team, '. ', name, ' would like to pursue a career in ', job, ' when ', pronoun[gender], ' is older, that\'s why ', pronoun[gender], ' is studying hard.', sep='')