# infection.py
# Pseudocode:
# 1. Set the total number of students, starting infected count, growth rate, and day.
# 2. Print the initial infected count.
# 3. While the total infected count is less than the class size:
#    a. Calculate the number of new infections.
#    b. Add the new infections to the current infected count.
#    c. Limit the infected count to the class size if necessary.
#    d. Increase the day counter.
#    e. Print the infected count for that day.
# 4. Print the total number of days required to infect the class.

total_students = 91
infected = 5
growth_rate = 0.4
day = 0

print("Day 0 infected count:", infected)

while infected < total_students:
    new_infected = infected * growth_rate
    infected = infected + new_infected

    if infected > total_students:
        infected = total_students

    day = day + 1
    print("Day {} infected count: {}".format(day, infected))

print("It took {} days to infect all {} students.".format(day, total_students))
