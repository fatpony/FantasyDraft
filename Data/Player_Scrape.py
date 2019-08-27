import pandas as pd
from bs4 import BeautifulSoup
from requests import get

url = "https://fantasy.espn.com/football/players/projections"

response = get(url)

nfl = BeautifulSoup(response.content, 'html.parser')
print(nfl.prettify())