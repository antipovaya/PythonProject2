from astropy.time import Time
from astropy.coordinates import solar_system_ephemeris, EarthLocation
from astropy.coordinates import get_body_barycentric, get_body
import json
import calculations
from pprint import pprint
j_old = r'C:\Users\7Ya\PycharmProjects\PythonProject2\Python\diplom\persons.json'
j_new = 'persons_with_calculations.json'


with open(j_old, "r", encoding='utf-8') as f:
    persons = json.load(f)
all_persons = []
for person in persons:
    calculations.sun_user(person)
    calculations.mercury_user(person)
    calculations.mars_user(person)
    calculations.jupiter_user(person)
    calculations.saturn_user(person)
    calculations.checking_planet(person, calculations.professions)
    all_persons.append(person)
print(all_persons[0])


with open(j_new, 'w', encoding='utf-8') as j:
    json.dump(all_persons, j, ensure_ascii=False)