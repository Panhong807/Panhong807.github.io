# This code calculates percentage population change from 2020 to 2024,
# prints the values in descending order, reports the countries with the
# largest increase and decrease, and shows a labelled bar chart.
import matplotlib.pyplot as plt

pop_data = {
    'UK': (66.7, 69.2),
    'China': (1426, 1410),
    'Italy': (59.4, 58.9),
    'Brazil': (208.6, 212.0),
    'USA': (331.6, 340.1),
}

percent_changes = {}
for country, (pop2020, pop2024) in pop_data.items():
    percent_change = ((pop2024 - pop2020) / pop2020) * 100
    percent_changes[country] = percent_change

print("Percentage changes in population from 2020 to 2024:")
for country, change in percent_changes.items():
    print(f"{country}: {change:.2f}%")

countries = list(percent_changes.keys())
max_increase_country = countries[0]
max_decrease_country = countries[0]

for country in countries:
    if percent_changes[country] > percent_changes[max_increase_country]:
        max_increase_country = country
    if percent_changes[country] < percent_changes[max_decrease_country]:
        max_decrease_country = country

print(f"Country with the highest population increase: {max_increase_country} ({percent_changes[max_increase_country]:.2f}%)")
print(f"Country with the highest population decrease: {max_decrease_country} ({percent_changes[max_decrease_country]:.2f}%)")

items = []
for country in countries:
    items.append((country, percent_changes[country]))

n = len(items)
for i in range(n):
    max_index = i
    for j in range(i + 1, n):
        if items[j][1] > items[max_index][1]:
            max_index = j
    items[i], items[max_index] = items[max_index], items[i]

print("Percentage changes in descending order:")
for country, change in items:
    print(f"{country}: {change:.2f}%")

countries_sorted = []
changes_sorted = []
colors = []

for country, change in items:
    countries_sorted.append(country)
    changes_sorted.append(change)
    if change > 0:
        colors.append('lightgreen')
    else:
        colors.append('lightcoral')

plt.figure(figsize=(10, 6))
plt.bar(countries_sorted, changes_sorted, color=colors)
plt.xlabel('Countries')
plt.ylabel('Percentage Change in Population')
plt.title('Percentage Change in Population from 2020 to 2024')
plt.axhline(0, color='black', linewidth=0.8)
plt.show()
