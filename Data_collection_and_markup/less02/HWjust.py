import requests  # pip install requests
from bs4 import BeautifulSoup  # pip install bs4
from fake_useragent import UserAgent  # pip install fake_useragent
from pprint import pprint

ua = UserAgent()

url = "https://just-make-up.ru"

# headers = {"User-Agent": ua.random}
headers = {"User-Agent": ua.chrome}

session = requests.session()  # аналогия с открытой вкладкой

response = session.get(url + "/catalog/", headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
products = soup.find_all('div', {'class': 'inner card-body d-flex flex-column'})
all_products = []

for product in products:
    product_info = {}
    name_info = product.find('a')
    product_info['name'] = name_info.getText()
    product_info['url'] = url + name_info.get('href')
    count_info = product.find('div', {"class": 'skuc color-7'})
    try:
        product_info['count_in_collection'] = int(count_info.getText()[:2])
    except:
        product_info['count_in_collection'] = int(count_info.getText()[:1])
    all_products.append(product_info)
pprint(all_products)