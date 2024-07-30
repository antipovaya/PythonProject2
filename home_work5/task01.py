# Напишите функцию get_file_info, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
#
# Пример использования.
# На входе:
#
#
# file_path = "C:/Users/User/Documents/example.txt"
#
# На выходе:
#
#
# ('C:/Users/User/Documents/', 'example', '.txt')

# def get_file_info(file_path):
#     way, expansion = file_path.split('.')
#     n = len(way.split('/'))
#     name = way.split('/')[n-1]
#     way = way.split('/')
#     way.pop()
#     way = '/'.join(way)
#
#     return (way, name, '.' + expansion)
#
#
#


#
# import os
#
# def get_file_info(path):
#     filepath, file_extension = os.path.splitext(path)
#     dirname, filename = os.path.split(filepath)
#     return (dirname, filename, file_extension)

# Два этих варианта не проходят тест, теряется скобка.

import os



def get_file_info(file_path):

    path, filename = os.path.split(file_path)
    # print(path, filename)
    if path:

        path += '/'

    base, ext = os.path.splitext(filename)
    # print(base, ext)
    return path, base, ext



file_path = "C:/Users/User/Documents/example.txt"

print(get_file_info(file_path))