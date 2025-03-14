import sys

def dtc(P, Q):
	return abs(P - Q)
	
colorfile = sys.argv[1]
R = int(sys.argv[2])
G = int(sys.argv[3])
B = int(sys.argv[4])

total_dist = None
closest_color = None

with open(colorfile) as fp:
	for line in fp:
		column = line.split()
		rgb_num = column[2].split(',')
		dist_r = dtc(rgb_num[0], R)
		dist_g = dtc(rgb_num[1], G)
		dist_b = dtc(rgb_num[2], B)
		sum = dist_b + dist_g + dist_b
		
		if total_dist > sum:
			total_dist = sum 
			color = column[0]
print(color)
		