
'''
seq = 'ACGTACGTGGGGGACGTACGTCCCCC'
w = 10
for i in range(len(seq) -w +1):
	s = seq[i:i+w]
	print(i, sequence.gc_comp(s), sequence.gc_skew(s))
	
#initial number: 4641652
'''

import sys
import mcb185

w = int(sys.argv[2])
for defline, seq in mcb185.read_fasta(sys.argv[1]):
    num_g = 0
    num_c = 0
    #for i in range(len(seq) - w + 1):
    for i in range(20):
        s = seq[i:i+w]
        print(s)
        if i == 0:
            num_g = s.count('G')
            num_c = s.count('C')
            gc_comp = (num_g + num_c) / len(s)
            gc_skew = (num_g - num_c) / (num_g + num_c)
        else:
            left_nt = seq[i-1]
            right_nt = seq[i+w-1]
            if left_nt == 'G':
                num_g -= 1
            elif left_nt == 'C':
                num_c -= 1
            if right_nt == 'G':
                num_g += 1
            elif right_nt == 'C':
                num_c += 1
            gc_comp = (num_g + num_c) / len(s)
            if num_c + num_g == 0:
                gc_skew = 0
            else:
                gc_skew = (num_g - num_c) / (num_g + num_c)
            print(i, gc_comp, gc_skew)
