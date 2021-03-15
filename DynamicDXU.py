import os
from datetime import datetime
import requests
import urllib.request as urllib2
from bs4 import BeautifulSoup
import re
import pycountry

import sqlite3

url = "https://funds.dynamic.ca/fundprofiles/en-US/etf/DXU/CAD"

response = requests.get(url)
html = response.content
soup = BeautifulSoup(response.text, 'html.parser')


curtime     = datetime.now()
day         = curtime.date()

  
# Get the 'as of' date. This is when the holdings were posted.  
for i in soup.find_all("span", {"class": "small"}):
  if i.find(text=re.compile("As at")):
    array = []
    array.append(i.text)
    PostingDate= i.text

    if array:
      break;
    else:
      print("")


for i in soup.find_all("h2", {"class": "page-header"}):
  if i.text == "Top 10 Equity Holdings  (%)":
    toptenString= i.text

# While selecting the stock names, the scrape picks up country names from the other tables. We dont want these in the database.
# pycountry contains the world contry names which we can use to compare our results to. If the results are within a world contry, keep it from the final results as this is not a stock name. 
countrynames = []
TheStocks = []
for co in list(pycountry.countries):
  countrynames.append(co.name)


divTag = soup.find_all("table", {"class": "table table-striped table-noborder"})
for i in divTag:
  tdTags = i.find_all("td", {"class": "text-left"})
  for i in tdTags:
    filterOut = ['Equities', 'Other', 'Cash and equivalents', 'Taiwan']
    if i.text in filterOut:
      continue
    
    elif i.text in countrynames:
      continue
    else:
      TheStocks.append(i.text)
      TheStock = i.text

      params =(PostingDate, TheStock, day)
      
      # Insert web scrape results into sqlite database. 
      db = sqlite3.connect('./dynamic.db')
      cursor = db.cursor()
      cursor.execute("INSERT INTO dynamictable (PostingDate, StockName, ScriptRunDate) VALUES (?, ?, ?)", params)
      db.commit()
      
print(PostingDate)
print(TheStocks)

print("test")










