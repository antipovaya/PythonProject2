import requests

category = input("Введите название интересующей Вас категории на английском языке (например: Park, Zoos, Museums и т.п.) : ")
url = "https://api.foursquare.com/v3/places/search"
params = {
    'limit': 50,
    'query': category,
    'fields': 'name,location,rating'
}
headers = {
    "Accept": "application/json",
    "Authorization": "fsq3P6zWw5hrHAp69JoTu+0TFeYEBCEXDIo7+Ivypcz/4Uo="
}
response = requests.request("GET", url, params=params, headers=headers)
if response.status_code == 200:
    print("Успешный запрос API по URL: ", response.url)
else:
    print("Запрос API отклонен с кодом состояния:", response.status_code)

data = response.json()

establishments = []
for place in data['results']:
    place_name = place.get('name')
    place_address = place.get('location')['formatted_address']
    place_rating = place.get('rating') if 'rating' in place else "Рейтинг не определялся"
    establishments.append({'name': place_name, 'address': place_address, 'rating': place_rating})
for establishment in establishments:
        print(f"Название: {establishment['name']}")
        print(f"Адрес: {establishment['address']}")
        print(f"Рейтинг: {establishment['rating']}")
        print()

# response = requests.get(url, headers=headers)

# print(response.text)
