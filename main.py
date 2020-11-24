# You should first install BeautifulSoup4 , Request and Pandas module
from bs4 import BeautifulSoup
import requests
import pandas as pd


def return_results(address):
    page = requests.get(address)
    page_text = page.content

    bs = BeautifulSoup(page_text, features='html.parser')
    ls = bs.find_all('div', 'tombstone-container')

    period_names = [i.get_text() for i in [item.find(class_='period-name') for item in ls]]
    short_descriptions = [i.get_text() for i in [item.find(class_='short-desc') for item in ls]]
    temperature = [i.get_text() for i in [item.find(class_='temp') for item in ls]]
    results = zip(period_names, short_descriptions, temperature)

    weather_stuff = pd.DataFrame(
        {
            'period': period_names,
            'short_description': short_descriptions,
            'temperature': temperature
        }
    )

    weather_stuff.to_csv('weather.csv')
