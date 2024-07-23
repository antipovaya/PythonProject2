"""
Задание №2
Погружение в Python | Коллекции
Пользователь вводит данные. Сделайте проверку данных
и преобразуйте если возможно в один из вариантов ниже:
✔ Целое положительное число
✔ Вещественное положительное или отрицательное число
✔ Строку в нижнем регистре, если в строке есть
хотя бы одна заглавная буква
✔ Строку в нижнем регистре в остальных случаях
"""

# мое решение:


user_input = input('Введите что-нибудь: ')

if user_input.isdigit():
    user_input = int(user_input)
    print(f'{user_input} тип {type(user_input)}')
elif user_input.split('.')[0].isdigit() and user_input.split('.')[1].isdigit():
    user_input = float(user_input)
    print(f'{user_input} тип {type(user_input)}')
elif user_input.split('.')[0][0] == '-' and user_input.split('.')[0][1:].isdigit() and user_input.split('.')[
    1].isdigit():
    user_input = float(user_input)
    print(f'{user_input} тип {type(user_input)}')
else:
    print(f'{user_input.lower()} тип {type(user_input)}')

# решение на сеинаре:

# user_input = input("Введите что-нибудь: ")
# if user_input.isdigit():
#     user_input = int(user_input)
# else:
#     try:
#         user_input = float(user_input)
#     except ValueError:
#         if not user_input.islower():
#             user_input = user_input.lower()
#         else:
#             user_input = user_input.lower()
#
# print(user_input, type(user_input))
