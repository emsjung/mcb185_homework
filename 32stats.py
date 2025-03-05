import math
numbers = [5, 2, 8, 1, 3]
def length(vals):
	return len(numbers)
print(length(numbers))

def minmax(vals): 
	mini = vals[0]
	maxi = vals[0]
	for val in vals: 
		if val < mini: 
			mini = val
		if val > maxi: 
			maxi = val
	return mini, maxi	
print(minmax(numbers))

def mean(vals):
	total = 0 
	for val in vals: 
		total += val 
	return total / len(vals)
def std(vals):
	m = mean(vals)
	var_total = 0
	for x in vals: 
		var_total += (x - m) ** 2 
	var = var_total / len(vals)
	return math.sqrt(var)
print(mean(numbers), std(numbers))

def median(vals):
	sorted_vals = sorted(vals)
	n = len(sorted_vals)
	mid = n // 2 
	if n % 2 == 1:
		return sorted_vals[mid]
	else:
		return (sorted_vals[mid - 1] + sorted_vals[mid]) / 2
print(median(numbers))