from bs4 import BeautifulSoup
import requests
import csv

URL = "https://www.screener.in/screens/234/bluest-of-the-blue-chips/"
headers= {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}


page = requests.get(URL, headers=headers)

soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

table = soup2.find('table',class_ = 'data-table text-nowrap striped mark-visited').find_all('tr')

print(table[1])

# Create a Timestamp for your output to track when data was collected

import datetime

today = datetime.date.today()

print(today)

name="Spaj Industries"
price=1000
marketcap=15000
header= ['Date','Company Name', 'Price', 'Market Cap']
data=[today, name, price, marketcap]

with open('BlueChipDataset.csv', 'w', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(data)
import pandas as pd

df = pd.read_csv(r'D:\User Data\Desktop\PycharmProjects\MEDUSA\BlueChipDataset.csv')
for t in table[1:15]:
    name = t.find('a').get_text().strip()
    xyz = t.find_all('td')
    price = xyz[2].get_text().strip()
    marketcap = xyz[4].get_text().strip()
    data = [today, name, price, marketcap]
    with open('BlueChipDataset.csv', 'a+', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data)

print(df)