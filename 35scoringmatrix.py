import sys

# Read command-line arguments
alphabet = sys.argv[1]  # Alphabet (e.g., "ACGT")
match_score = int(sys.argv[2])  # Score for a match (e.g., +1)
mismatch_score = int(sys.argv[3])  # Score for a mismatch (e.g., -1)

# Print the header row
print("  " + "  ".join(alphabet))  # Formatting for column labels

# Generate and print the scoring matrix
for i in range(len(alphabet)):
    row = alphabet[i]  # Row label (A, C, G, T)
    
    for j in range(len(alphabet)):
        if alphabet[i] == alphabet[j]:  # If characters match
            row += f" {match_score:2}"  # Align values for formatting
        else:  # If characters mismatch
            row += f" {mismatch_score:2}"
    
    print(row)  # Print the row
