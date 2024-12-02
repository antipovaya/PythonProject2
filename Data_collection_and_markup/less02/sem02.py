import requests  # pip install requests
from bs4 import BeautifulSoup  # pip install bs4
from fake_useragent import UserAgent  # pip install fake_useragent
from pprint import pprint
ua = UserAgent()
# print(ua.random)


# url = "https://www.boxofficemojo.com/intl/?ref_=bo_nb_hm_tab"
url = "https://www.boxofficemojo.com"

# headers = {"User-Agent": ua.random}
headers = {"User-Agent": ua.chrome}
params = {"ref_": "bo_nb_hm_tab"}
session = requests.session()  # аналогия с открытой вкладкой
response = session.get(url + "/intl", params=params, headers=headers)
# print(response.status_code)
soup = BeautifulSoup(response.text, "html.parser")
# test_link = soup.find("a", {'class': 'a-link-normal'})
# print(test_link)
rows = soup.find_all('tr')

films = []

for row in rows[2:12]:
    film = {}
    # area_info = row.find('a', {'class': 'a-link-normal'})  # создаем переменную, чтобы не дублировать запросы
    # film['area'] = [area_info.getText(), url + area_info.get('href')]  # метод getText дает нам выделить именно
    # # текстовый контент без тегов

    # area_info = row.find('td', {'class': 'a-text-left mojo-header-column mojo-truncate mojo-field-type-area_id'}).find('a')

    # либо ищем через ребенка:
    # try:
    area_info = row.find('td', {'class': 'a-text-left mojo-header-column mojo-truncate mojo-field-type-area_id'}).findChildren()[0]
    film['area'] = [area_info.getText(), url + area_info.get('href')]
    # except:
    #     print('Exception. No information with area')
    #     film['area'] = None

    # try:
    weekend_info = row.find('td', {'class': 'a-text-left mojo-field-type-date_interval'}).findChildren()[0]
    film['weekend'] = [weekend_info.getText(), url + weekend_info.get('href')]
    # except:
    #     print('Exception. No information with weekend')
    #     film['weekend'] = None

    # try:
    film['releases'] = int(row.find('td', {'class': 'a-text-right mojo-field-type-positive_integer'}).getText())
    # except:
    #     print('Exception. No information with releases')
    #     film['releases'] = None

    # try:
    frelease_info = row.find('td', {'class': 'a-text-left mojo-field-type-release mojo-cell-wide'}).findChildren()[0]
    film['frelease'] = [frelease_info.getText(), url + frelease_info.get('href')]
    # except:
    #     print('Exception. No information with first releases')
    #     film['frelease'] = None
    try:
        distributor_info = row.find('td', {'class': 'a-text-left mojo-field-type-studio'}).findChildren()[0]
        film['distributor'] = [distributor_info.getText(), url + distributor_info.get('href')]
    except:
        print('Exception with distributor, object = ', film['frelease'])
        film['distributor'] = None

    # try:
    film['gross'] = row.find('td', {'class': 'a-text-right mojo-field-type-money'}).getText()
    # except:
    #     print('Exception. No information with first releases')
    #     film['gross'] = None

    films.append(film)
    pprint(films)
    # for row in rows[13:-1]:
    #     film = {}
    #     # area_info = row.find('a', {'class': 'a-link-normal'})  # создаем переменную, чтобы не дублировать запросы
    #     # film['area'] = [area_info.getText(), url + area_info.get('href')]  # метод getText дает нам выделить именно
    #     # # текстовый контент без тегов
    #
    #     # area_info = row.find('td', {'class': 'a-text-left mojo-header-column mojo-truncate mojo-field-type-area_id'}).find('a')
    #
    #     # либо ищем через ребенка:
    #     # try:
    #     area_info = row.find('td', {
    #         'class': 'a-text-left mojo-header-column mojo-truncate mojo-field-type-area_id'}).findChildren()[0]
    #     film['area'] = [area_info.getText(), url + area_info.get('href')]
    #     # except:
    #     #     print('Exception. No information with area')
    #     #     film['area'] = None
    #
    #     # try:
    #     weekend_info = row.find('td', {'class': 'a-text-left mojo-field-type-date_interval'}).findChildren()[0]
    #     film['weekend'] = [weekend_info.getText(), url + weekend_info.get('href')]
    #     # except:
    #     #     print('Exception. No information with weekend')
    #     #     film['weekend'] = None
    #
    #     # try:
    #     film['releases'] = int(row.find('td', {'class': 'a-text-right mojo-field-type-positive_integer'}).getText())
    #     # except:
    #     #     print('Exception. No information with releases')
    #     #     film['releases'] = None
    #
    #     # try:
    #     frelease_info = row.find('td', {'class': 'a-text-left mojo-field-type-release mojo-cell-wide'}).findChildren()[
    #         0]
    #     film['frelease'] = [frelease_info.getText(), url + frelease_info.get('href')]
    #     # except:
    #     #     print('Exception. No information with first releases')
    #     #     film['frelease'] = None
    #     try:
    #         distributor_info = row.find('td', {'class': 'a-text-left mojo-field-type-studio'}).findChildren()[0]
    #         film['distributor'] = [distributor_info.getText(), url + distributor_info.get('href')]
    #     except:
    #         print('Exception with distributor, object = ', film['frelease'])
    #         film['distributor'] = None
    #
    #     # try:
    #     film['gross'] = row.find('td', {'class': 'a-text-right mojo-field-type-money'}).getText()
    #     # except:
    #     #     print('Exception. No information with first releases')
    #     #     film['gross'] = None




