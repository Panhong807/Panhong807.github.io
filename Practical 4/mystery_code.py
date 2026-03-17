# What does this piece of code do?
# Answer: This code simulates a process where it draws random numbers between 1 and 10, adds them up, and keeps track of the progress until it reaches 10. Finally, it prints the total of the drawn random numbers.

# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

total_rand = 0    # Initialize total_rand to 0
progress=0        # Initialize progress to 0
while progress<=10:    # Loop until progress is greater than 10
	progress+=1        # Increment progress by 1
	n = randint(1,10)  # Draw a random number between 1 and 10
	total_rand+=n  # Add the drawn number to total_rand

print(total_rand)   # Print the total of the drawn random numbers

