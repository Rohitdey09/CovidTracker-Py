## Current Covid-19 data with python
from covid import Covid
covid = Covid()

print("Total confirmed cases:", covid.get_total_confirmed_cases())
print("Total deaths:", covid.get_total_deaths())
print("Total recovered cases:", covid.get_total_recovered())

country = input("Enter country name: ")
country_data = covid.get_status_by_country_name(country)
print("Data for", country)
print("Confirmed cases:", country_data['confirmed'])
print("Deaths:", country_data['deaths'])
print("Recovered:", country_data['recovered'])