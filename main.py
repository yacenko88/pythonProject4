import datetime
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import csv

def collect_data(city_code = '1445'):
    cur_time = datetime.datetime.now().strftime('%d_%m_%Y_%H_%M')
    ua = UserAgent()

    headers = {
        'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'User-Agent' : ua.random
    }
    cookies = {
        'mg_geo_id' : f'{city_code}'
    }
    response = requests.get(url = 'https://magnit.ru/promo/', headers = headers, cookies = cookies)
    # with open(f'index.html', 'w', encoding='utf-8') as file:
    #     file.write(response.text)
    with open('index.html') as file:
        src = file.read()
    soup = BeautifulSoup(response.text, 'lxml')

    city = soup.find('a', class_='header__contacts-link_city').text.strip()
    cards = soup.find_all('a', class_='card-sale_catalogue')
    print(city, len(cards))

def main():
    collect_data(cyti_code = '1445')


if __name__=='__main__':
    main()