import math

def pythagorean_triples(): 
	for a in range(1, 101):
		for b in range(a, 101):
			c = math.sqrt((a ** 2) + (b ** 2))
			if c % 1 == 0 and c < 100:
				print(a, b, int(c))

pythagorean_triples()
