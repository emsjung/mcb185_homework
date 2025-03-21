import sys
import mcb185
import itertools

# Read sequence from FASTA file
for defline, seq in mcb185.read_fasta(sys.argv[1]):
    k = 1  # Start from k=1
    while True:
        observed_kmers = set()
        all_possible = {''.join(p) for p in itertools.product('ACGT', repeat=k)}
        
        revcomp = seq.translate(str.maketrans('ACGT', 'TGCA'))[::-1]
        
        # Scan both strands
        for s in [seq, revcomp]:
            for i in range(len(s) - k + 1):
                observed_kmers.add(s[i:i+k])
        
        # Find missing k-mers
        missing_kmers = all_possible - observed_kmers
        if missing_kmers:
            print(f'Missing {len(missing_kmers)} k-mers at k={k}')
            print(missing_kmers)
            break  # Stop after finding missing k-mers
        
        k += 1  # Increase k if all k-mers are present
