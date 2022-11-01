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
    with open("TwitterMemes.csv", 'a') as file:
        writer = csv.writer(file)
        writer.writerow((data['head'], data['link']))

def get_link(html):
    soup = BeautifulSoup(html, 'lxml')
    head = soup.find_all('div', {"itemtype": 'http://schema.org/Product'})#не понял
    #print(head)
    for i in head:
        link = 'link' #i.find('a', class_='snippet-link')['href']
        heads= i.find('a', class_='css-1dbjc4n r-18u37iz r-1pi2tsx r-13qz1uu')['href']
        data1 = {'head': heads,'link': link}
        csv_read(data1)

def main():
    get_link(get_html('https://twitter.com/memes'))

if __name__ == "__main__":
    main()

#heads= i.find('span', class_='css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0')['title']