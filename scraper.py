import requests  
r = requests.get('http://worldpopulationreview.com/countries/india-population/cities/')
from bs4 import BeautifulSoup  
soup = BeautifulSoup(r.text, 'html.parser')  
table = soup.find('table', attrs={'class': 'table table-striped'})
list_of_rows = []
for row in table.findAll('tr')[1:]:
    list_of_cells = []
    for cell in row.findAll('td'):
        a = cell.find('a')
        if (a != None):    # if 'td' contains maps link, then extract latitude and longitude from it
            link_text = a['href']
            textnew = link_text.replace('https://www.google.com/maps/?q=', '')
            latlng_list = textnew.split(',')
            lat = latlng_list[0]
            lng = latlng_list[1]
            list_of_cells.append(lat)
            list_of_cells.append(lng)
            
        else:             # else 'td' contains city and its population
            city_or_population_text = cell.text
            list_of_cells.append(city_or_population_text)
    list_of_rows.append(list_of_cells)
print(list_of_rows)
import pandas as pd  
df = pd.DataFrame(list_of_rows, columns=['city name', 'population count', 'latitude', 'longitude'])   
df.to_csv('city_data.csv', index=False, encoding='utf-8')