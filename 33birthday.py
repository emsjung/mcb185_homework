import random
import sys

# Read command-line arguments
trials = int(sys.argv[1])   # Number of trials (simulations)
days = int(sys.argv[2])     # Number of days in a year (e.g., 365)
people = int(sys.argv[3])   # Number of people in the classroom

def has_duplicate_birthday(people, days):
    """Returns True if at least two people share a birthday."""
    birthdays = []  # Empty list to store birthdays
    for _ in range(people):
        bday = random.randint(0, days - 1)  # Random birthday between 0 and days-1
        if bday in birthdays:  # Check if birthday already exists in the list
            return True  # Found a duplicate
        birthdays.append(bday)  # Add new birthday to the list
    return False  # No duplicate found

# Run the simulation
matches = 0  # Counter for how many times we get at least one shared birthday
for _ in range(trials):
    if has_duplicate_birthday(people, days):
        matches += 1

# Calculate the probability
probability = matches / trials * 100

# Output the result
print(f"Probability of shared birthday with {people} people over {trials} trials: {probability:.2f}%")
