from dice import Dice
import sys
import pygal
"""wizualizacja rzutów kością, korzysta z biblioteki pygal
pierwszy argument to liczba rzutów, kolejne to ilość ścianek na poszczególnych kostkach, np:
python dice_visual.py 200 6 8 10
oznacza 200 rzutów kostkami o 6, 8 i 10 ściankach i zsumowaniu wyników"""

#lista kości
dices = []
max_value = 0
if len(sys.argv) > 1:
	roll_number = int(sys.argv[1])
	if len(sys.argv) > 2:
		for s in range(2, len(sys.argv)):
			tmp = int(sys.argv[s])
			dices.append(Dice(tmp))
			max_value += tmp
else:
	roll_number = 100
	dices.append(Dice())

#dodanie do listy kości kości typu K6
len_dices = len(dices) 

results = []
for roll_num in range(roll_number):
	result = 0
	for dice in range(len_dices):
		result += dices[dice].roll()
	results.append(result)
	
#analiza wyników
frequencies = []
for value in range(len_dices, max_value+1):
	frequency = results.count(value)
	frequencies.append(frequency)

text_title = "Histogram dla " + str(len_dices) + " kości ("
for q in range(len_dices):
	text_title += "K" + str(dices[q].num_sides) + " "
text_title = text_title.rstrip()
text_title += ") i " + str(roll_number) + " rzutów."


#wizualizacja wyników
histogram = pygal.Bar()
histogram.force_uri_protocol = 'http'

histogram.title = text_title
histogram.x_labels = list(range(len_dices, max_value+1))
histogram.x_title = 'Wynik'
histogram.y_title = 'Częstotliwość wystepowania wartości'
histogram.add('Rzuty', frequencies)
histogram.render_to_file('dice_visual.svg')