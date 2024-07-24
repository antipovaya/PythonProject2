# На вход подается словарь со списком вещей для похода в качестве ключа и их массой max_weight в качестве значения.
#
# Определите какие вещи влезут в рюкзак backpack передав его максимальную грузоподъёмность.
# Предметы не должны дублироваться.
#
# Результат должен быть в виде словаря {предмет:вес} с вещами в рюкзаке и сохранен в переменную backpack.
#
# Достаточно получить один допустимый вариант и сохранить в переменную backpack. Не выводите backpack на экран.
#
# Пример
#
# На входе:
#
#
items = {
    "ключи": 0.3,
    "кошелек": 0.2,
    "телефон": 0.5,
    "зажигалка": 0.1
}
max_weight = 1.0
# На выходе, например, один из допустимых вариантов может быть таким:
#
#
# {'ключи': 0.3, 'кошелек': 0.2, 'зажигалка': 0.1}


backpack = {}
total = 0

for el in items:
    if total < max_weight:
        backpack[el] = items[el]
        total += items[el]

print(backpack)
