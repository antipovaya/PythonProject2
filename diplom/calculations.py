from astropy.time import Time
from astropy.coordinates import solar_system_ephemeris, EarthLocation
from astropy.coordinates import get_body_barycentric, get_body

t = Time("1934-1-4 12:00")
loc = EarthLocation.of_site('greenwich')

with solar_system_ephemeris.set('builtin'):
    sun_user = get_body('saturn', t, loc)

print(sun_user)

# <SkyCoord (GCRS: obstime=2024-12-10 16:30:00.000, obsgeoloc=(3353159.10641094, -2163608.49484903, 4958838.61798787)
# m, obsgeovel=(157.78511936, 243.64017167, -0.39054804) m / s): (ra, dec, distance) in (deg, deg, AU)
#     (257.78413159, -22.96298649, 0.98471784)>



def sun_user(user):
    """Функция рассчитывает координаты Солнца по дате рождения пользователя, определяет знак зодиака"""
    if user['date'][:1] in 'р.':
        user['date'] = user['date'].replace('р. ', '')
    date_user = Time(user['date'] + ' 12:00')
    loc = EarthLocation.of_site('greenwich')
    with solar_system_ephemeris.set('builtin'):
        coordinates_sun = get_body('sun', date_user, loc)
        # print(str(coordinates_sun)[219:-28])
        coordinates_sun = float(str(coordinates_sun)[219:-28])
        user['coordinates_sun'] = coordinates_sun
    if 0 <= coordinates_sun < 30:
        user['zodiac_sign_of_sun'] = 'aries'
    if 30 <= coordinates_sun < 60:
        user['zodiac_sign_of_sun'] = 'taurus'
    if 60 <= coordinates_sun < 90:
        user['zodiac_sign_of_sun'] = 'gemini'
    if 90 <= coordinates_sun < 120:
        user['zodiac_sign_of_sun'] = 'cancer'
    if 120 <= coordinates_sun < 150:
        user['zodiac_sign_of_sun'] = 'leo'
    if 150 <= coordinates_sun < 180:
        user['zodiac_sign_of_sun'] = 'virgo'
    if 180 <= coordinates_sun < 210:
        user['zodiac_sign_of_sun'] = 'libra'
    if 210 <= coordinates_sun < 240:
        user['zodiac_sign_of_sun'] = 'scorpio'
    if 240 <= coordinates_sun < 270:
        user['zodiac_sign_of_sun'] = 'sagittarius'
    if 270 <= coordinates_sun < 300:
        user['zodiac_sign_of_sun'] = 'capricorn'
    if 300 <= coordinates_sun < 330:
        user['zodiac_sign_of_sun'] = 'aquarius'
    if 330 <= coordinates_sun < 360:
        user['zodiac_sign_of_sun'] = 'pisces'


def mercury_user(user):
    """Функция рассчитывает координаты Меркурия по дате рождения пользователя, определяет знак зодиака планеты"""
    if user['date'][:1] in 'р.':
        user['date'] = user['date'].replace('р. ', '')
    date_user = Time(user['date'] + ' 12:00')
    loc = EarthLocation.of_site('greenwich')
    with solar_system_ephemeris.set('builtin'):
        coordinates_mercury = get_body('mercury', date_user, loc)
        # print(str(coordinates_sun)[219:-28])
        coordinates_mercury = float(str(coordinates_mercury)[219:-28])
        user['coordinates_mercury'] = coordinates_mercury
    if 0 <= coordinates_mercury < 30:
        user['zodiac_sign_of_mercury'] = 'aries'
    if 30 <= coordinates_mercury < 60:
        user['zodiac_sign_of_mercury'] = 'taurus'
    if 60 <= coordinates_mercury < 90:
        user['zodiac_sign_of_mercury'] = 'gemini'
    if 90 <= coordinates_mercury < 120:
        user['zodiac_sign_of_mercury'] = 'cancer'
    if 120 <= coordinates_mercury < 150:
        user['zodiac_sign_of_mercury'] = 'leo'
    if 150 <= coordinates_mercury < 180:
        user['zodiac_sign_of_mercury'] = 'virgo'
    if 180 <= coordinates_mercury < 210:
        user['zodiac_sign_of_mercury'] = 'libra'
    if 210 <= coordinates_mercury < 240:
        user['zodiac_sign_of_mercury'] = 'scorpio'
    if 240 <= coordinates_mercury < 270:
        user['zodiac_sign_of_mercury'] = 'sagittarius'
    if 270 <= coordinates_mercury < 300:
        user['zodiac_sign_of_mercury'] = 'capricorn'
    if 300 <= coordinates_mercury < 330:
        user['zodiac_sign_of_mercury'] = 'aquarius'
    if 330 <= coordinates_mercury < 360:
        user['zodiac_sign_of_mercury'] = 'pisces'


def mars_user(user):
    """Функция рассчитывает координаты Марса по дате рождения пользователя, определяет знак зодиака планеты"""
    if user['date'][:1] in 'р.':
        user['date'] = user['date'].replace('р. ', '')
    date_user = Time(user['date'] + ' 12:00')
    loc = EarthLocation.of_site('greenwich')
    with solar_system_ephemeris.set('builtin'):
        coordinates_mars = get_body('mars', date_user, loc)
        # print(str(coordinates_sun)[219:-28])
        coordinates_mars = float(str(coordinates_mars)[219:-28])
        user['coordinates_mars'] = coordinates_mars
    if 0 <= coordinates_mars < 30:
        user['zodiac_sign_of_mars'] = 'aries'
    if 30 <= coordinates_mars < 60:
        user['zodiac_sign_of_mars'] = 'taurus'
    if 60 <= coordinates_mars < 90:
        user['zodiac_sign_of_mars'] = 'gemini'
    if 90 <= coordinates_mars < 120:
        user['zodiac_sign_of_mars'] = 'cancer'
    if 120 <= coordinates_mars < 150:
        user['zodiac_sign_of_mars'] = 'leo'
    if 150 <= coordinates_mars < 180:
        user['zodiac_sign_of_mars'] = 'virgo'
    if 180 <= coordinates_mars < 210:
        user['zodiac_sign_of_mars'] = 'libra'
    if 210 <= coordinates_mars < 240:
        user['zodiac_sign_of_mars'] = 'scorpio'
    if 240 <= coordinates_mars < 270:
        user['zodiac_sign_of_mars'] = 'sagittarius'
    if 270 <= coordinates_mars < 300:
        user['zodiac_sign_of_mars'] = 'capricorn'
    if 300 <= coordinates_mars < 330:
        user['zodiac_sign_of_mars'] = 'aquarius'
    if 330 <= coordinates_mars < 360:
        user['zodiac_sign_of_mars'] = 'pisces'


def jupiter_user(user):
    """Функция рассчитывает координаты Юпитера по дате рождения пользователя, определяет знак зодиака планеты"""
    if user['date'][:1] in 'р.':
        user['date'] = user['date'].replace('р. ', '')
    date_user = Time(user['date'] + ' 12:00')
    loc = EarthLocation.of_site('greenwich')
    with solar_system_ephemeris.set('builtin'):
        coordinates_jupiter = get_body('jupiter', date_user, loc)
        coordinates_jupiter = float(str(coordinates_jupiter)[219:-28])
        user['coordinates_jupiter'] = coordinates_jupiter
    if 0 <= coordinates_jupiter < 30:
        user['zodiac_sign_of_jupiter'] = 'aries'
    if 30 <= coordinates_jupiter < 60:
        user['zodiac_sign_of_jupiter'] = 'taurus'
    if 60 <= coordinates_jupiter < 90:
        user['zodiac_sign_of_jupiter'] = 'gemini'
    if 90 <= coordinates_jupiter < 120:
        user['zodiac_sign_of_jupiter'] = 'cancer'
    if 120 <= coordinates_jupiter < 150:
        user['zodiac_sign_of_jupiter'] = 'leo'
    if 150 <= coordinates_jupiter < 180:
        user['zodiac_sign_of_jupiter'] = 'virgo'
    if 180 <= coordinates_jupiter < 210:
        user['zodiac_sign_of_jupiter'] = 'libra'
    if 210 <= coordinates_jupiter < 240:
        user['zodiac_sign_of_jupiter'] = 'scorpio'
    if 240 <= coordinates_jupiter < 270:
        user['zodiac_sign_of_jupiter'] = 'sagittarius'
    if 270 <= coordinates_jupiter < 300:
        user['zodiac_sign_of_jupiter'] = 'capricorn'
    if 300 <= coordinates_jupiter < 330:
        user['zodiac_sign_of_jupiter'] = 'aquarius'
    if 330 <= coordinates_jupiter < 360:
        user['zodiac_sign_of_jupiter'] = 'pisces'


def saturn_user(user):
    """Функция рассчитывает координаты Сатурна по дате рождения пользователя, определяет знак зодиака планеты"""
    if user['date'][:1] in 'р.':
        user['date'] = user['date'].replace('р. ', '')
    date_user = Time(user['date'] + ' 12:00')
    loc = EarthLocation.of_site('greenwich')
    with solar_system_ephemeris.set('builtin'):
        coordinates_saturn = get_body('saturn', date_user, loc)
        coordinates_saturn = float(str(coordinates_saturn)[219:-29])
        user['coordinates_saturn'] = coordinates_saturn
    if 0 <= coordinates_saturn < 30:
        user['zodiac_sign_of_saturn'] = 'aries'
    if 30 <= coordinates_saturn < 60:
        user['zodiac_sign_of_saturn'] = 'taurus'
    if 60 <= coordinates_saturn < 90:
        user['zodiac_sign_of_saturn'] = 'gemini'
    if 90 <= coordinates_saturn < 120:
        user['zodiac_sign_of_saturn'] = 'cancer'
    if 120 <= coordinates_saturn < 150:
        user['zodiac_sign_of_saturn'] = 'leo'
    if 150 <= coordinates_saturn < 180:
        user['zodiac_sign_of_saturn'] = 'virgo'
    if 180 <= coordinates_saturn < 210:
        user['zodiac_sign_of_saturn'] = 'libra'
    if 210 <= coordinates_saturn < 240:
        user['zodiac_sign_of_saturn'] = 'scorpio'
    if 240 <= coordinates_saturn < 270:
        user['zodiac_sign_of_saturn'] = 'sagittarius'
    if 270 <= coordinates_saturn < 300:
        user['zodiac_sign_of_saturn'] = 'capricorn'
    if 300 <= coordinates_saturn < 330:
        user['zodiac_sign_of_saturn'] = 'aquarius'
    if 330 <= coordinates_saturn < 360:
        user['zodiac_sign_of_saturn'] = 'pisces'


user = {"date": "р. 1934-1-4", "name": "Зураб Церетели",
        "profession": "советский и российский художник, скульптор, педагог, Народный художник России"}

sun_user(user)
mercury_user(user)
mars_user(user)
jupiter_user(user)
saturn_user(user)


# {'date': '1934-1-4', 'name': 'Зураб Церетели',
#  'profession': 'советский и российский художник, скульптор, педагог, Народный художник России',
#  'coordinates_sun': 285.61208171,
#  'zodiac_sign_of_sun': 'capricorn',
#  'coordinates_mercury': 275.6333463,
#  'zodiac_sign_of_mercury': 'capricorn',
#  'coordinates_mars': 309.3849143,
#  'zodiac_sign_of_mars': 'aquarius',
#  'coordinates_jupiter': 201.175321,
#  'zodiac_sign_of_jupiter': 'libra',
#  'coordinates_saturn': 318.44305432,
#  'zodiac_sign_of_saturn': 'aquarius'}







professions = {'aries': ['спортсмен', 'теннисист', 'боксер', 'стрелок', 'автогонщик', 'гонщик', 'лыжник',
                         'биатлонист', 'шахматист', 'гимнаст', 'гимнастка', 'чемпионка', 'хоккеист', 'чемпион',
                         'тренер', 'физик', 'инженер', 'механик', 'военачальник', 'каскадер', 'дрессировщик',
                         'офицер', 'майор', 'спасатель', 'пожарный', 'генерал', 'полководец', 'солдат', 'военный',
                         'электротехник', 'изобретатель', 'артист', 'актер', 'актриса', 'артистка', 'киноактер',
                         'киноактриса', 'политик', 'агитатор', 'революционер', 'государственный деятель',
                         'политический', 'космонавт', 'конструктор оружия', 'разведчик', 'бизнес', 'предприниматель',
                         'криминалист', 'детектив', 'ученый', 'хирург', 'врач', 'психиатр', 'психолог', 'астроном',
                         'испытатель', 'стоматолог', 'травматолог', 'пилот', 'летчик', 'летчица', 'водитель',
                         'пилот', 'конструктор', 'разработчик', 'вооружения', 'телеведущий', 'альпинист', 'электроник',
                         'математик', 'военачальник', 'лидер', 'первый'],

               'taurus': ['юрист', 'адвокат', 'строитель', 'архитектор', 'земледелец', 'фермер', 'повар',
                          'землевладелец', 'банкир', 'бухгалтер', 'экономист', 'певец', 'певица', 'артист', 'артистка',
                          'актер', 'актриса', 'балерина', 'фигурист', 'фигуристка', 'поэт', 'поэтесса', 'режиссер',
                          'ученый', 'дизайнер', 'декоратор', 'портной', 'стилист', 'биолог', 'эколог', 'химик',
                          'фармацевт', 'математик', 'терапевт', 'отоларинголог', 'скульптор', 'художник', 'врач',
                          'правозащитник', 'писатель', 'писательница', 'композитор', 'дирижер', 'пианист', 'пианистка',
                          'музыковед', 'критик', 'искусствовед', 'публицист', 'телеведущий', 'дипломат', 'политический',
                          'общественный деятель', 'сценарист', 'философ', 'музыкант', 'хореограф'],

               'gemini': ['пистаель', 'ученый', 'писательница', 'журналист', 'журналистка', 'химик', 'врач',
                          'фармацевт',
                          'связист', 'связистка', 'разведчик', 'разведчица', 'лингвист', 'педагог', 'учитель',
                          'переводчик',
                          'переводчица', 'предприниматель', 'бизнес', 'поэт', 'поэтесса', 'ведущий', 'ведущая',
                          'телеведущий', 'телеведущая', 'радиоведущий', 'радиоведущая', 'математик', 'информатик',
                          'разработчик', 'техник', 'биолог', 'эколог', 'историк', 'бактериолог', 'физик',
                          'переговорщик',
                          'дипломат', 'правозащитник', 'адвокат', 'изобретатель', 'государственный деятель', 'политик',
                          'политический', 'психиатр', 'психолог', 'психотерапевт', 'критик', 'публицист',
                          'общественный',
                          'автор', 'режиссер', 'сценарист', 'актер', 'актриса', 'фольклор', 'композитор',
                          'изобретатель',
                          'криптограф', 'географ', 'секретарь', 'лектор', 'агент', 'посыльный', 'диктор', 'маклер',
                          'телефонист', 'телефонистка', 'посол', 'консул', 'шпион', 'детектив', 'легкоатлет', 'бегун',
                          'теннисист', 'лыжник', 'альпинист', 'гимнаст', 'мотогонщик', 'водитель', 'пилот', 'инженер',
                          'социолог', 'юморист', 'сатирик', 'актер', 'актриса', 'художник', 'географ', 'автор',
                          'философ',
                          'редактор'],

               'cancer': ['певец', 'певица', 'музыкант', 'поэт', 'поэтесса', 'композитор', 'пианист', 'пианистка',
                          'скрипач', 'писатель', 'писательница', 'композитор', 'врач', 'хирург', 'акушер', 'гениколог',
                          'педиатр', 'терапевт', 'историк', 'биолог', 'картограф', 'эколог', 'бактериолог', 'лингвист',
                          'ученый', 'педагог', 'учитель', 'псхолог', 'артист', 'артистка', 'актер', 'актриса', 'фермер',
                          'географ', 'повар', 'художник', 'скульптор', 'балерина', 'хореограф', 'скпипачка', 'танцор',
                          'танцовщица', 'драматург', 'фотограф', 'сценарист', 'кинорежессер', 'режессер', 'археолог',
                          'общественный', 'фермер', 'социолог', 'издатель', 'критик', 'киноактер', 'киноактриса',
                          'деятель',
                          'ботаник', 'автор', 'химик', 'психиатр', 'психотерапевт', 'антрополог', 'социолог', 'дирижер',
                          'культуролог', 'искусствовед', 'геолог', 'геммолог'],

               'leo': ['генерал', 'политик', 'военачальник', 'артист', 'актер', 'актриса', 'артистка', 'киноактер',
                       'киноактриса', 'политик', 'агитатор', 'революционер', 'государственный деятель',
                       'политический', 'певец', 'певица', 'музыкант', 'поэт', 'поэтесса', 'композитор', 'пианист',
                       'пианистка', 'скрипач', 'писатель', 'писательница', 'композитор', 'врач', 'сатирик', 'ведущий',
                       'телеведущий', 'телеведущая', 'ведущая', 'ювелир', 'художник', 'скульптор', 'ресторатор',
                       'бизнес', 'предприниматль', 'кардиолог', 'терапевт', 'педиатр', 'режиссер', 'дизайнер',
                       'продюсер', 'дирижер', 'педагог', 'преподаватель', 'ректор', 'тренер', 'атлет', 'ресторан',
                       'казино', 'ресторан', 'галерея', 'искусствовед', 'военный', 'разведчик', 'криминалист',
                       'начальник', 'критик', 'деятель', 'агитатор', 'публицист', 'автор', 'композитор', 'пианист',
                       'пианистка', 'кино', 'театр', 'профессор', 'лидер'],

               'virgo': ['ученый', 'математик', 'физик', 'химик', 'разработчик', 'изобретатель', 'диктор', 'профессор',
                         'биолог', 'автор', 'писатель', 'писательница', 'переводчик', 'переводчица', 'разведчик',
                         'разведчица', 'экономист', 'бухгалтер', 'аналитик', 'критик', 'издатель', 'литератор',
                         'публицист', 'писатель', 'писательница', 'композитор', 'врач', 'инфекциолог', 'бактериолог',
                         'фармацевт', 'поэт', 'поэтесса', 'дизайнер', 'архитектор', 'декоратор', 'ювелир', 'техник',
                         'программист', 'криминалист', 'детектив', 'инспектор', 'ревизор', 'философ', 'филолог',
                         'геолог',
                         'исследователь', 'преподаватель', 'статистик', 'ветеринар', 'медсестра', 'владелец', 'травник',
                         'предприниматель', 'модель', 'актриса', 'певец', 'певица', 'композитор', 'хореограф',
                         'журналист', 'журналистка', 'педагог', 'теоретик', 'артист', 'артистка', 'политик',
                         'политический', 'государственный', 'деятель', 'эколог', 'микробиолог', 'биолог', 'редактор'],

               'libra': ['юрист', 'адвокат', 'архитектор', 'дипломат', 'переговорщик', 'модель', 'актриса',
                         'певец', 'певица', 'композитор', 'хореограф', 'педагог', 'артист', 'артистка', 'политик',
                         'политический', 'государственный', 'критик', 'деятель', 'агитатор', 'публицист', 'консул',
                         'правозащитник', 'певец', 'певица', 'музыкант', 'поэт', 'поэтесса', 'композитор', 'пианист',
                         'пианистка', 'скрипач', 'писатель', 'писательница', 'композитор', 'критик', 'искусствовед',
                         'публицист', 'телеведущий', 'дипломат', 'политический', 'общественный деятель', 'сценарист',
                         'философ', 'музыкант', 'драматург', 'стилист', 'ювелир', 'декоратор', 'дизайнер',
                         'предпринимаель',
                         'педагог', 'кинорежиссер', 'литературовед', 'публицист', 'автор', 'деятель', 'автор',
                         'живописец',
                         'художник', 'скульптор', 'социолог', 'полководец', 'маршал', 'майор', 'генерал', 'военный',
                         'агитатор', 'судья', 'танцор', 'тансовщица', 'фотограф', 'режиссер', 'парфюмер', 'психолог',
                         'социолог', 'архитектор', 'модельер'],

               'scorpio': ['спортсмен', 'теннисист', 'боксер', 'стрелок', 'автогонщик', 'гонщик', 'лыжник',
                           'биатлонист', 'шахматист', 'гимнаст', 'гимнастка', 'чемпионка', 'хоккеист', 'чемпион',
                           'тренер', 'физик', 'инженер', 'механик', 'военачальник', 'каскадер', 'дрессировщик',
                           'офицер', 'майор', 'спасатель', 'пожарный', 'генерал', 'полководец', 'солдат', 'военный',
                           'электротехник', 'изобретатель', 'артист', 'актер', 'актриса', 'артистка', 'киноактер',
                           'киноактриса', 'политик', 'агитатор', 'революционер', 'государственный деятель',
                           'политический', 'космонавт', 'конструктор оружия', 'разведчик', 'бизнес', 'предприниматель',
                           'криминалист', 'детектив', 'ученый', 'хирург', 'врач', 'психиатр', 'психолог',
                           'психотерапевт',
                           'испытатель', 'стоматолог', 'травматолог', 'пилот', 'летчик', 'летчица', 'водитель',
                           'пилот', 'конструктор', 'разработчик', 'вооружения', 'телеведущий', 'альпинист',
                           'электроник',
                           'математик', 'военачальник', 'онколог', 'прокурор', 'нотариус', 'политик', 'депутат',
                           'тренер',
                           'альпинист', 'следователь', 'штурман', 'гинеколог', 'инфекциолог', 'венеролог',
                           'патлогоанатом',
                           'рентгенолог', 'физиотерапевт', 'целитель', 'химик', 'математик', 'фармацевт', 'астрофизик',
                           'генетик', 'оккультист', 'чемпион', 'чемпионка'],

               'sagittarius': ['священник', 'папа', 'посол', 'агитатор', 'пропагандист', 'политолог', 'лингвист',
                               'политик', 'агитатор', 'революционер', 'государственный деятель', 'политический',
                               'этнограф',
                               'исследователь', 'изобретатель', 'публицист', 'профессор', 'ученый', 'путешественник',
                               'переводчик', 'переводчица', 'преподаватель', 'педагог', 'учитель', 'меценат',
                               'дипломат', 'консул', 'депутат', 'нотриус', 'юрист', 'адвокат', 'модель', 'актриса',
                               'певец', 'певица', 'композитор', 'хореограф', 'артист', 'артистка', 'публицист',
                               'политический', 'ученый', 'следователь', 'прокурор', 'судья', 'правозащитник', 'врач',
                               'психиатр', 'психолог', 'психотерапевт', 'ветеренар', 'стрелок', 'наездник', 'конный',
                               'скачки', 'кардинал', 'епископ', 'жокей', 'журналист', 'журналистка', 'предприниматель',
                               'бизнес', 'экспедитор', 'деятель', 'автор', 'издатель', 'писатель', 'кинорежиссер',
                               'литературовед', 'публицист', 'певец', 'певица', 'актер', 'актриса', 'балерина',
                               'фигурист',
                               'фигуристка', 'поэт', 'поэтесса', 'режиссер', 'биолог', 'эколог', 'химик', 'скульптор',
                               'художник', 'врач', 'писатель', 'писательница', 'композитор', 'дирижер', 'пианист',
                               'пианистка', 'музыковед', 'критик', 'искусствовед', 'публицист', 'телеведущий',
                               'телеведущая',
                               'сценарист', 'философ', 'музыкант', 'хореограф', 'чемпион', 'чемпионка', 'академик',
                               'разведчик', 'модель', 'спортсмен', 'тренер', 'философ', 'историк', 'археолог',
                               'географ',
                               'картограф', 'лидер', 'художник', 'продюсер', 'доктор'],

               'capricorn': ['чемпионка', 'чемпион', 'политик', 'государственный деятель', 'политический', 'артист',
                             'артистка', 'предприниматель', 'бизнес', 'телеведущий', 'телеведущая', 'хореограф',
                             'сценарист', 'модель', 'спортсмен', 'тренер', 'публицист', 'певец', 'певица', 'актер',
                             'актриса', 'балерина', 'фигурист', 'фигуристка', 'боксер', 'ученый', 'математик', 'физик',
                             'химик', 'разработчик', 'изобретатель', 'диктор', 'профессор', 'биолог', 'автор',
                             'писатель',
                             'писательница', 'переводчик', 'переводчица', 'разведчик', 'разведчица', 'экономист',
                             'бухгалтер', 'аналитик', 'критик', 'математик', 'физик', 'публицист', 'писатель',
                             'писательница', 'ученый', 'врач', 'часы', 'часовщик', 'изобретатель', 'поэт',
                             'поэтесса', 'архитектор', 'философ', 'ювелир', 'техник', 'программист', 'криминалист',
                             'детектив', 'инспектор', 'ревизор', 'археолог', 'филолог', 'геолог', 'исследователь',
                             'преподаватель', 'статистик', 'военачальник', 'офицер', 'майор', 'генерал', 'полководец',
                             'солдат', 'военный', 'социолог', 'инженер', 'техник', 'технолог', 'географ', 'картограф',
                             'пилот', 'инженер', 'микробиолог', 'художник', 'скульптор', 'оружейник', 'промышленник',
                             'теоретик', 'историк', 'академик', 'создатель'],

               'aquarius': ['пилот', 'инженер', 'космонавт', 'астроном', 'астролог', 'летчик', 'летчица', 'водитель',
                            'математик', 'физик', 'публицист', 'писатель', 'писательница', 'ученый', 'техник',
                            'программист',
                            'публицист', 'профессор', 'агитатор', 'общественный', 'политический', 'деятель',
                            'революционер',
                            'психиатр', 'психолог', 'психотерапевт', 'астроном', 'испытатель', 'исследователь',
                            'правозащитник', 'химик', 'гуру', 'радиотехник', 'радиофизик', 'сюрреалист', 'художник',
                            'художница', 'хореограф', 'танцор', 'танцовщица', 'балерина', 'гипнолог', 'психиатр',
                            'психолог', 'психотерапевт', 'изобретатель', 'философ', 'модель', 'актриса', 'певец',
                            'певица', 'композитор', 'хореограф', 'педагог', 'артист', 'артистка', 'политик',
                            'государственный', 'критик', 'сценарист', 'музыкант', 'драматург', 'стилист', 'ювелир',
                            'декоратор', 'дизайнер', 'предпринимаель', 'кинорежиссер', 'литературовед', 'публицист',
                            'автор', 'автор', 'живописец', 'скульптор', 'социолог', 'правозащитник', 'певец', 'певица',
                            'музыкант', 'поэт', 'поэтесса', 'композитор', 'пианист', 'пианистка', 'скрипач',
                            'орнитолог',
                            'авиаинженер', 'астрофизик', 'авиации', 'авиация', 'создатель'],

               'pisces': ['моряк', 'пилот', 'капитан', 'химик', 'космонавт', 'мореплаватель', 'физик', 'сюрреалист',
                          'художница', 'хореограф', 'танцор', 'танцовщица', 'балерина', 'гипнолог', 'психиатр',
                          'психолог', 'психотерапевт', 'философ', 'модель', 'актриса', 'певец', 'художник', 'дирижер'
                                                                                                            'певица',
                          'композитор', 'хореограф', 'педагог', 'артист', 'артистка', 'критик', 'сценарист',
                          'музыкант', 'драматург', 'стилист', 'ювелир', 'декоратор', 'дизайнер', 'кинорежиссер',
                          'литературовед', 'публицист', 'автор', 'писатель', 'живописец', 'скульптор', 'писательница',
                          'певец', 'певица', 'поэт', 'поэтесса', 'фотограф', 'пианист', 'пианистка', 'скрипач',
                          'скрипачка', 'целитель', 'экстрасенс', 'травник', 'математик', 'детектив', 'криминалист',
                          'разведчик', 'разведчица', 'сказочник', 'фвнтаст', 'невропатолог', 'океанолог', 'ихтиолог',
                          'биолог', 'теолог', 'священник', 'папа', 'проповедник', 'богослужитель', 'фармацевт',
                          'парфюмер', 'кораблестроение', 'конструктор', 'авиаинженер', 'комик', 'сатирик', 'юмарист',
                          'публицист', 'военный', 'летчик', 'летчица', 'астрофизик', 'врач', 'шахматист', 'ученый',
                          'астроном', 'морской', 'военный', 'доктор', 'профессор', 'авиации', 'авиация', 'педагог']}

def checking_planet(user, professions_of_zodiac_signs):
    """
    Функция проверяет совпадает ли реальная профессия личности с той, которая характерна ее гороскопу.
    Также выдется подсчет количества вхождений в список профессий.
    :param user: Словарь с именем, датой рождения и видами деятельности личности.
    :param professions_of_zodiac_signs: Словарь профессий, классифицированных по знакам зодиака
    """
    user_profession = user['profession'].split()
    new_user_profession = []
    for el in user_profession:
        new_user_profession.append(el.replace(',', ''))
    print(new_user_profession)
    user['connection_sun_proffesion'] = 0
    user['count_sun_proffesion'] = 0

    user['connection_mercury_proffesion'] = 0
    user['count_mercury_proffesion'] = 0

    user['connection_mars_proffesion'] = 0
    user['count_mars_proffesion'] = 0

    user['connection_jupiter_proffesion'] = 0
    user['count_jupiter_proffesion'] = 0

    user['connection_saturn_proffesion'] = 0
    user['count_saturn_proffesion'] = 0

    for prof in new_user_profession:
        if prof in professions_of_zodiac_signs[user['zodiac_sign_of_sun']]:
            user['connection_sun_proffesion'] = 1
            user['count_sun_proffesion'] += 1
    for prof in new_user_profession:
        if prof in professions_of_zodiac_signs[user['zodiac_sign_of_mercury']]:
            user['connection_mercury_proffesion'] = 1
            user['count_mercury_proffesion'] += 1
    for prof in new_user_profession:
        if prof in professions_of_zodiac_signs[user['zodiac_sign_of_mars']]:
            user['connection_mars_proffesion'] = 1
            user['count_mars_proffesion'] += 1
    for prof in new_user_profession:
        if prof in professions_of_zodiac_signs[user['zodiac_sign_of_jupiter']]:
            user['connection_jupiter_proffesion'] = 1
            user['count_jupiter_proffesion'] += 1
    for prof in new_user_profession:
        if prof in professions_of_zodiac_signs[user['zodiac_sign_of_saturn']]:
            user['connection_saturn_proffesion'] = 1
            user['count_saturn_proffesion'] += 1

checking_planet(user, professions)
print(user)

# {'date': '1934-1-4', 'name': 'Зураб Церетели',
#  'profession': 'советский и российский художник, скульптор, педагог, Народный художник России',
#  'coordinates_sun': 285.61208171,
#  'zodiac_sign_of_sun': 'capricorn',
#  'coordinates_mercury': 275.6333463,
#  'zodiac_sign_of_mercury': 'capricorn',
#  'coordinates_mars': 309.3849143,
#  'zodiac_sign_of_mars': 'aquarius',
#  'coordinates_jupiter': 201.175321,
#  'zodiac_sign_of_jupiter': 'libra',
#  'coordinates_saturn': 318.44305432,
#  'zodiac_sign_of_saturn': 'aquarius',
#  'connection_sun_proffesion': 1,
#  'count_sun_proffesion': 3,
#  'connection_mercury_proffesion': 1,
#  'count_mercury_proffesion': 3,
#  'connection_mars_proffesion': 1,
#  'count_mars_proffesion': 4,
#  'connection_jupiter_proffesion': 1,
#  'count_jupiter_proffesion': 4,
#  'connection_saturn_proffesion': 1,
#  'count_saturn_proffesion': 4}


# {'date': '1934-1-4', 'name': 'Зураб Церетели',
#  'profession': 'советский и российский художник, скульптор, педагог, Народный художник России',
#  'coordinates_sun': 285.61208171,
#  'zodiac_sign_of_sun': 'capricorn',
#  'coordinates_mercury': 275.6333463,
#  'zodiac_sign_of_mercury': 'capricorn',
#  'coordinates_mars': 309.3849143,
#  'zodiac_sign_of_mars': 'aquarius',
#  'coordinates_jupiter': 201.175321,
#  'zodiac_sign_of_jupiter': 'libra',
#  'coordinates_saturn': 318.44305432,
#  'zodiac_sign_of_saturn': 'aquarius'}

#
# for i in test['profession'].split():
#     if i in professions['capricorn']:
#         print(i)
#
# k = test['profession'].split()
# new_k = []
# for i in k:
#     new_k.append(i.replace(',', ''))
# print(new_k)
#
# for prof in new_k:
#     if prof in professions['capricorn']:
#         test['planets'] = 1
#         print(prof)
# print(test)
