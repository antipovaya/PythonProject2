# Напишите программу, которая получает целое число num и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

num = 255
print(hex(num))

hex_upper = format(num, 'X')
print(f'Шестнадцатеричное представление числа: {hex_upper}')
print(f'Проверка результата: {hex(num)}')

BASE = 16

# не мое решение:
def converts_numbers_by_base(number: int, base: int) -> str:
    """Преобразует число в нужную систему счисления"""
    number_str = '0123456789ABCDEF'
    if number < base:
        return number_str[number]

    return converts_numbers_by_base(number // base, base) + number_str[number % base]


def input_number() -> int:
    try:
        number = int(input('Введите число для перевода в систему счисления:'))
    except ValueError:
        return input_number()
    return number


if __name__ == '__main__':
    number = input_number()
    print(f'Полученый результат в системе счисления {BASE} равен:', converts_numbers_by_base(number, BASE))