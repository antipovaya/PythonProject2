# Напишите программу, которая получает целое число num и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.


BASE = 16


def converts_numbers_by_base(number_user: int, base: int) -> str:
    """Преобразует число в нужную систему счисления"""
    number_str = '0123456789ABCDEF'
    if number_user < base:
        return number_str[number_user]

    return converts_numbers_by_base(number_user // base, base) + number_str[number_user % base]


def input_number() -> int:
    try:
        number_user = int(input('Введите число для перевода в систему счисления:'))
    except ValueError:
        return input_number()
    return number_user


if __name__ == '__main__':
    number = input_number()
    print(f'Полученый результат в системе счисления {BASE} равен:', converts_numbers_by_base(number, BASE))


# num = 255
# print(hex(num))
#
# hex_upper = format(num, 'x')
# print(f'Шестнадцатеричное представление числа: {hex_upper}')
# print(f'Проверка результата: {hex(num)}')

