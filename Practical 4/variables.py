# variables.py
# Pseudocode:
# 1. Store the population values for three years.
# 2. Calculate the change from 2004 to 2014 and from 2014 to 2024.
# 3. Compare the two changes.
# 4. Print the comparison and add a comment about population growth.
# 5. Create boolean variables X and Y, then compute W.
# 6. Include a truth table in comments.

a = 5.08  # Population in 2004
b = 5.33  # Population in 2014
c = 5.55  # Population in 2024

d = b - a  # Change between 2004 and 2014
e = c - b  # Change between 2014 and 2024

if d > e:
    print("Change between 2004-2014 is larger")
elif d < e:
    print("Change between 2014-2024 is larger")
else:
    print("Changes are equal")

# Because d is greater than e, population growth is decelerating.

X = True
Y = False
W = X or Y

# Truth table for W = X or Y
# X      Y      W
# True   True   True
# True   False  True
# False  True   True
# False  False  False

print("W =", W)
