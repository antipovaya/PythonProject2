import requests  # pip install requests
from bs4 import BeautifulSoup  # pip install bs4
from fake_useragent import UserAgent  # pip install fake_useragent
from pprint import pprint
import json
import datetime
import time

ua = UserAgent()

url = "https://www.calend.ru"

headers = {"User-Agent": ua.chrome}
session = requests.session()  # аналогия с открытой вкладкой

page = datetime.date(2000, 1, 1)
all_persons = []

while page.year == 2000:

    param = str(page.month) + "-" + str(page.day) + "/"
    response = session.get(url + "/persons/" + param, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    persons = soup.find_all('li', {'class': 'one-four'})

    for person in persons:
        person_info = {}

        year_info = person.find('span', {'class': 'year_on_img'}).getText()
        person_info['date'] = year_info + "-" + str(page.month) + "-" + str(page.day)

        person_info['name'] = person.find('div', {'class': 'caption'}).find('span', {'class': 'title'}).find(
            'a').getText()
        person_info['profession'] = (
            person.find('div', {'class': 'caption'}).find('span', {'class': 'title'}).find('span').getText())

        all_persons.append(person_info)
    print(f'Обработана {page.month} - {page.day} дата')
    time.sleep(3)
    page += datetime.timedelta(days=1)
pprint(all_persons)

with open('persons.json', 'w', encoding='utf-8') as f:
    json.dump(all_persons, f, ensure_ascii=False)  # без ensure_ascii=False не будет русских букв
