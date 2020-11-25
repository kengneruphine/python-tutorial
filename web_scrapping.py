import pandas as pd
import requests
from bs4 import BeautifulSoup

page = requests.get('https://forecast.weather.gov/MapClick.php?lat=41.8843&lon=-87.6324#.X75Q3Z1Kjjs')
soup = BeautifulSoup(page.content, 'html.parser')
week = soup.find(id='seven-day-forecast-body') 
#print(week)

items = week.find_all(class_ ='tombstone-container')

period_names = [item.find(class_='period-name').get_text() for item in items] 
short_descriptions =[item.find(class_='short-desc').get_text() for item in items]
temperatures =[item.find(class_='temp').get_text() for item in items]

#converting data into table format
weather_stuff = pd.DataFrame({
    'period':period_names,
    'short_descriptions':short_descriptions,
    'temperatures':temperatures
})

print(weather_stuff)

#converting data into csv format
weather_stuff.to_csv('weather.csv', sep='\t',encoding='utf-8')