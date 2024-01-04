import pandas as pd


data = pd.read_csv("countries-population.csv")

most_populat = data[data['Population'] == data['Population'].max()]


print("The most populated  is:")
print(most_populat[['Name', 'Population']])

data["density"]=data["Population"]/data["Size-sqr-km"]


most_crowd=data[data["density"]==data["density"].max()]
print("\nThe most crowd  is:")
print(most_crowd[['Name', "density"]])

most_crowd=data[data["density"]==data["density"].min()]
print("\nThe least crowd  is:\n")
print(most_crowd[['Name', "density"]])


data['Established-Date'] = pd.to_datetime(data['Established-Date'], errors='coerce')



oldest_country = data[data['Established-Date'] == data['Established-Date'].min()]
newest_country = data[data['Established-Date'] == data['Established-Date'].max()]


print("The oldest country is:")
print(oldest_country[['Name', 'Established-Date']])

print("\nThe newest country is:")
print(newest_country[['Name', 'Established-Date']])


continent_counts = data['Continent'].value_counts()


print("Number of countries for each continent:")
print(continent_counts)

