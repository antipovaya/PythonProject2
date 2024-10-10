"""
Задание №1
📌 Напишите программу, которая использует модуль logging для
вывода сообщения об ошибке в файл.
📌 Например отлавливаем ошибку деления на ноль.
"""
import logging

logging.basicConfig(filename='example.log.', filemode='w', encoding='utf-8',  # если поставим "w",  то файл будет
                    # перезаписываться каждый раз
                    format='{levelname} - {asctime} в строке {lineno} '
                           'функция "{funcName}()" : {msg}', style='{', level=logging.WARNING)


def func(a, b):
    try:
        res = a / b
    except ZeroDivisionError:
        logging.warning('Нельзя делить на ноль')
        return ''
    else:
        return res


print(func(9, 0))
