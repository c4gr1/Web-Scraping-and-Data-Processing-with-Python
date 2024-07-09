#   Scraping Data from a Real Website + Pandas

import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue"

page = requests.get(url)

soup = BeautifulSoup(page.text,"html.parser")

#print(soup)

table = soup.find_all('table')[1]
#print(table)

#   th = table header cell
world_titles = table.find_all("th")

#print(world_titles)

#   strip() deletes characters like \n in the text
world_table_titles = [title.text.strip() for title in world_titles]

#print(world_table_titles)

#pd.set_option("display.max_columns",None)
#pd.set_option("display.max_rows",None)

df = pd.DataFrame(columns= world_table_titles)

#print(df)

#   tr = table row
#   td = table data cell
column_data = table.find_all("tr")
for row in column_data[1:]:
    row_data = row.find_all("td")
    indivudual_row_data = [data.text.strip() for data in row_data]
    #print(indivudual_row_data)
    lenght = len(df) 
    df.loc[lenght] = indivudual_row_data

print(df)

df.to_csv(r'companies.csv',index = False)