import requests
from bs4 import BeautifulSoup
import csv
#import re
# pip install beautifulsoup4
# pip install lxml

def get_html(url):
    r = requests.get(url)    # Получим метод Response
    r.encoding = 'utf8'
    return r.text   # Вернем данные объекта text


def csv_read(data):
    with open("avito1.csv", 'a') as file:
        writer = csv.writer(file)
        writer.writerow((data['head'], data['link']))

def get_link(html):
    soup = BeautifulSoup(html, 'lxml')
    head = soup.find_all('div', {"itemtype": 'http://schema.org/Product'})
    #print(head)
    for i in head:
        link = 'link'
        heads= i.find('a', class_='snippet-link')['title']
        data1 = {'head': heads,'link': link}
        csv_read(data1)

def main():
    get_link(get_html('http://www.avito.ru/moskva/telefony/iphone-ASgBAgICAUSeAt4J?cd=1'))

if __name__ == "__main__":
    main()