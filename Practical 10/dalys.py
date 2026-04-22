import os                
import pandas as pd    
import matplotlib.pyplot as plt   
import numpy as np     

os.chdir('C:/Users/HP/Desktop/Practical 10')
print(os.getcwd())
print(os.listdir())

dalys_data = pd.read_csv('dalys-rate-from-all-causes.csv')
print(dalys_data.head(5))  #print the first 5 rows of the dataset
dalys_data.info()  #get information about the dataset
dalys_data.describe()  #get summary statistics of the dataset

print(dalys_data.iloc[0,3]) #access the value in the first row and fourth column
subset = dalys_data.iloc[0:10, 2:4] #create a subset of the first 10 rows and first 5 columns
print(subset)

afg=dalys_data[dalys_data['Entity'] == 'Afghanistan'] #filter the dataset for Afghanistan
afg_first10=afg.iloc[0:10]
max_year=afg_first10['Year'].max() #find the maximum year in the subset
print(max_year)

zimbabwe_years=dalys_data[dalys_data['Entity'] == 'Zimbabwe']['Year'] #filter the dataset for Zimbabwe and get the years
print(zimbabwe_years)
print(zimbabwe_years.min()) #find the minimum year in the Zimbabwe dataset
print(zimbabwe_years.max()) #find the maximum year in the Zimbabwe dataset

recent_data=dalys_data.loc[dalys_data['Year']==2019, ['Entity', 'DALYs (rate)']] #filter the dataset for the year 2019 and select the Entity and DALYs (rate) columns
max_country=recent_data.loc[recent_data['DALYs (rate)'].idxmax()]
min_country=recent_data.loc[recent_data['DALYs (rate)'].idxmin()]
print(max_country)
print(min_country)

country_name=max_country['Entity']
country_data=dalys_data[dalys_data['Entity'] == country_name] #filter the dataset for the country with the maximum DALYs (rate) in 2019
plt.plot(country_data['Year'], country_data['DALYs (rate)']) #plot the DALYs (rate) over time for the country with the maximum DALYs (rate) in 2019
plt.xlabel('Year')
plt.ylabel('DALYs (rate)')
plt.title(f'DALYs (rate) over time for {country_name}')
plt.xticks(rotation=-90)
plt.show()

plt.hist(recent_data["DALYs (rate)"])
plt.xlabel("DALYs (rate)")
plt.ylabel("Frequency")
plt.title("Distribution of DALYs (rate) in 2019")
plt.show()