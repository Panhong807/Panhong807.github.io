# This code analyzes heart rate data for a group of patients, prints the
# number of patients and the mean heart rate, classifies heart rates as low,
# normal, or high, reports the most common category, and shows a labelled pie chart.
import matplotlib.pyplot as plt

heart_rate = [72, 60, 126, 85, 90, 59, 76, 131, 88, 121, 64]
num_patients = len(heart_rate)
mean_heart_rate = sum(heart_rate) / num_patients

print(f"Number of patients: {num_patients}")
print(f"Mean heart rate: {mean_heart_rate:.2f} bpm")

low = []
normal = []
high = []

for hr in heart_rate:
    if hr < 60:
        low.append(hr)
    elif hr <= 120:
        normal.append(hr)
    else:
        high.append(hr)

count_low = len(low)
count_normal = len(normal)
count_high = len(high)

if count_low >= count_normal and count_low >= count_high:
    max_category = 'Low (<60 bpm)'
elif count_normal >= count_low and count_normal >= count_high:
    max_category = 'Normal (60-120 bpm)'
else:
    max_category = 'High (>120 bpm)'

print(f"Low heart rate patients: {count_low}")
print(f"Normal heart rate patients: {count_normal}")
print(f"High heart rate patients: {count_high}")
print(f"Category with the highest number of patients: {max_category}")

labels = ['Low (<60 bpm)', 'Normal (60-120 bpm)', 'High (>120 bpm)']
sizes = [count_low, count_normal, count_high]
colors = ['lightcoral', 'lightgreen', 'lightblue']
explode = (0.1, 0, 0)

plt.figure(figsize=(8, 5))
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.title('Heart Rate Distribution')
plt.axis('equal')
plt.show()
