import math
def char_to_prob(char):
	asc1 = ord(char)-33
	prob = 10**(-asc1/10)
	return prob
	
def prob_to_char(prob):
	q = -10*math.log10(prob)
	asc2 = chr(int(q + 33))
	return asc2
	
print(char_to_prob('A'))
print(prob_to_char(0.001))