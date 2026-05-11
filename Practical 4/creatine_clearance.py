# creatine_clearance.py
# Pseudocode:
# 1. Ask the user for age, weight, gender, and serum creatinine.
# 2. Convert the values to the correct data types.
# 3. Check whether the input values are within valid ranges.
# 4. If the inputs are valid, calculate creatinine clearance.
# 5. Adjust the result for female patients.
# 6. Print the final creatinine clearance value.

age = float(input("Enter age (years): "))
weight = float(input("Enter weight (kg): "))
gender = input("Enter gender (male/female): ").strip().lower()
cr = float(input("Enter serum creatinine concentration (umol/l): "))

if age >= 100:
    print("Error: Age must be less than 100 years")
    exit()

if weight <= 20 or weight >= 80:
    print("Error: Weight must be between 20 kg and 80 kg (exclusive)")
    exit()

if cr <= 0 or cr >= 100:
    print("Error: Creatinine concentration must be between 0 and 100 umol/l (exclusive)")
    exit()

if gender not in ["male", "female"]:
    print("Error: Gender must be either 'male' or 'female'")
    exit()

crcl = ((140 - age) * weight) / (72 * cr)

if gender == "female":
    crcl = crcl * 0.85

print("Your creatinine clearance (CrCl) is: {:.2f} ml/min".format(crcl))
