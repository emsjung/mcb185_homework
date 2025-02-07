print ('hello, again')
# 10demo.py by Emma Jung

import math

a = 3						# side of triangle 
b = 4						# side of triangle
c = math.sqrt(a**2 + b**2) 	# hypotenuse 
print(c)
print(type(a), type(b), type(c))
print(type(a), type(b), type(c), sep=', ', end='!\n')

def pythagoras(a, b): return math.sqrt(a**2 + b**2)
print(pythagoras(3, 4))

def circle_area(r): return math.pi * r**2
def rectangle_area(w, h): return w * h
def triangle_area(w, h): return rectangle_area(w, h) / 2
print(circle_area(3))
print(rectangle_area(2, 4))
print(triangle_area(2, 4))
def temp_F_to_C(f): return (f - 32) * 5 / 9
print (temp_F_to_C(32))

s = 'hello world'
print(s, type(s))

a = 2 
b = 2
if a == b: 
	print('a equals b')
print(a, b)
def is_even(x): 
		if x % 2 == 0: return True
		return False
print(is_even(2))
print(is_even(3))
c = 3 == 4
print(c)
print(type(c))

a = 0.3 
b = 0.1 * 3
if		a < b: 	print('a < b')
elif 	a > b: 	print('a > b')
else:			print('a == b')

print(abs(a - b)) # 5.551115123125783e-17
if abs(a - b) < 1e-9: print('close enough')
if math.isclose(a, b) : print('close enough')

s1 = 'A'
s2 = 'B'
s3 = 'a'
if s1 < s2: print('A < B')
if s2 < s3: print('B < a')


