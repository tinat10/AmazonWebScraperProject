# importing libraries
from bs4 import BeautifulSoup
import requests
import smtplib
import time
import datetime

# connect to website

URL = 'https://www.amazon.com/Apple-iPhone-256GB-Black-Titanium/dp/B0CLMGHDBV/ref=sr_1_6?crid=23JCP3U1GK52M&dib=eyJ2IjoiMSJ9.entQOTS1zH8TwbF3D_QEApTa1Rx6HHoIDe3oi2dEtPOkluJPUf6-JRDS3OQieTGOgYS7X5hRv_kBh7ELB8DYETCiocl1iYpYdHzyKsmlQvOJIFN-1ghS7-KJbRbQ4ZCtIjdOefREFn2h4AMY2DiSCWenOXIu-cj8QE9yZv9LyU5wJ3iFFewVuAylyPU6KKTQ-hTqxPtO7HQ8ukaIhN59lmcpHXExVBye9wfBg-6E0To.2mIDibGPm0Mo06Af-dOMtsaYwwmORfieXirzJytaxxk&dib_tag=se&keywords=iphone+15&qid=1717724714&sprefix=iphone+15%2Caps%2C127&sr=8-6'

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

page = requests.get(URL, headers = headers)

# pulls in page content
soup1 = BeautifulSoup(page.content, "html.parser") 
soup2 = BeautifulSoup(soup1.prettify(), 'html.parser')
# print(soup2) -> shows html 

title = (soup2.find(id = 'productTitle').get_text()).strip()
print(title)
price = (soup2.find(class_="a-price-whole").get_text(strip=True) + soup2.find(class_='a-price-fraction').get_text(strip=True)).replace('\n', '').replace(' ', '')
print(price) 


today = datetime.date.today()
print(today)


import csv

header = ['Product', 'Price', 'Date']
data = [title, price, today]
# Product -> title  | price -> price | Date = today

with open('AmazonWebScraperDataset.csv', 'w', newline='', encoding = "UTF8") as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(data)

'''
to check if it's working
'''
import pandas as pd

df = pd.read_csv(r'C:\Users\tinat\AmazonWebScraperDataset.csv')
df.head()

# append data to previously made csv file

with open('AmazonWebScraperDataset.csv', 'a+', newline='', encoding = "UTF8") as f:
    writer = csv.writer(f)
    writer.writerow(data)


def check_price():
    URL = 'https://www.amazon.com/Apple-iPhone-256GB-Black-Titanium/dp/B0CLMGHDBV/ref=sr_1_6?crid=23JCP3U1GK52M&dib=eyJ2IjoiMSJ9.entQOTS1zH8TwbF3D_QEApTa1Rx6HHoIDe3oi2dEtPOkluJPUf6-JRDS3OQieTGOgYS7X5hRv_kBh7ELB8DYETCiocl1iYpYdHzyKsmlQvOJIFN-1ghS7-KJbRbQ4ZCtIjdOefREFn2h4AMY2DiSCWenOXIu-cj8QE9yZv9LyU5wJ3iFFewVuAylyPU6KKTQ-hTqxPtO7HQ8ukaIhN59lmcpHXExVBye9wfBg-6E0To.2mIDibGPm0Mo06Af-dOMtsaYwwmORfieXirzJytaxxk&dib_tag=se&keywords=iphone+15&qid=1717724714&sprefix=iphone+15%2Caps%2C127&sr=8-6'
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
    page = requests.get(URL, headers = headers)
    
    soup1 = BeautifulSoup(page.content, "html.parser") 
    soup2 = BeautifulSoup(soup1.prettify(), 'html.parser')
    
    title = (soup2.find(id = 'productTitle').get_text()).strip()
    price = (soup2.find(class_="a-price-whole").get_text(strip=True) + soup2.find(class_='a-price-fraction').get_text(strip=True)).replace('\n', '').replace(' ', '')

    import datetime
    today = datetime.date.today()
    print(today)

    import csv
    header = ['Product', 'Price', 'Date']
    data = [title, price, today]

    with open('AmazonWebScraperDataset.csv', 'a+', newline='', encoding = "UTF8") as f:
        writer = csv.writer(f)
        writer.writerow(data)
    if (float(price) < 1200):
        send_mail()


# method for sending mail
def send_mail():
    server = sntplib.SMTP_SSL('tkt@njit.edu', 465)
    server.ehlo()
    server.login('tkt@njit.edu', 'xxxxxxxxxxx')

    subject = 'The Apple iPhone 15 is on sale NOW! Go grab it before it sells out!'
    body = 'Tina, go purchase a NEW iPhone 15! It is less than $1200 right now. This is a STEAL!'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail('tkt@njit.edu', msg)


while(True):
    check_price()
    # time.sleep(3600) # runs once every hour -> for busy days like black friday
    time.sleep(86400) # runs once every day (86400 seconds = 1 day)
# tracking price by day

