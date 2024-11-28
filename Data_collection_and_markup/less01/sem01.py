import requests
# https://api.giphy.com/v1/gifs/search?
# api_key=VqnhAeN9EH85ov5JOM5JSMgiy6MWKK4g&
# q=flowers&
# limit=5&
# offset=0&
# rating=pg-13&
# lang=ru&
# bundle=messaging_non_clips

# Далее будет способ создания переменного окружения, чтобы не светить свои личные данные:

import os
from dotenv import load_dotenv
import json
from pprint import pprint

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

url = "https://api.giphy.com/v1/gifs/search"
params = {"api_key": os.getenv("API_KEY"),
          "q": "flowers",
          "limit": 5,
          "offset": 0,
          "rating": "pg-13",
          "lang": "ru",
          "bundle": "messaging_non_clips"}

response = requests.get(url, params=params)
# print()

j_data = response.json()
print()

with open('gifs.json', 'w') as f:
    json.dump(j_data, f)

for gif in j_data.get('data'):
    print(gif.get('images').get('original').get('url'))

# в режиме отладки (нажимаем на паучка)
# response.headers  # выводит словарь заголовков
# response.status_code  # выводит код, то есть есть ли ошиька
# response.ok  # статус коды меньше 400
# response.text # текстовое содержимое ответа (str)
# response.content # то же но в бинарном виде
pprint(j_data)
