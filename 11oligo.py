def tm(a, t, c, g): 
		if	(a + t + c + g) <= 13:return (a + t) * 2 + (g + c) * 4
		elif(a + t + c + g) > 13: return (64.9 + 41 * (g + c - 16.4) / (a + t + c + g))
print(tm(4, 6, 7, 8))		
print(tm(2, 3, 3, 2))