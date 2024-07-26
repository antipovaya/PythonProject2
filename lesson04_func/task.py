# функция map
text = ['ПРИВЕТ', 'ЗДорово', 'ПриВетСВУЮ']
res = map(lambda x: x.lower(), text)
print(*res)  # звездочка тут значит распаковка


# функция filter берет на вход функцию и возвращает true или false
num = [-2, 22, -4, 88]
res = tuple(filter(lambda x: x > 0, num)) # чтобы не использовать звездочку мы используем tuple, так как на выходе
# xотим кортеж
print(res)


# функция zip позволит итерироваться сразу по нескольким массивам:
# Итератор останавливается, когда исчерпана кратчайшая из последовательностей.

names = ['Иван', 'Николай', 'Семен']
salaries = [125_000, 96_000, 109_000]
awards = [0.1, 0.25, 0.13, 0.99]
for name, salary, award, in zip(names, salaries, awards):
    print(f'{name} заработал {salary:.2f} денег и премию {salary * award:.2f}')


# Функция max()
# max(iterable, *[, key, default]) или max(arg1, arg2, *args[, key])
# Функция принимает на вход итерируемую последовательность или несколько
# позиционных элементов и ищет максимальное из них. Ключевой параметр key
# указывает на то, какие элементы необходимо сравнить, если объект является
# сложной структурой. Отдельно параметр default используется для возврата
# значения, если на вход передана пустой итератор

lst_1 = []
lst_2 = [42, 256, 73]
lst_3 = [("Иван", 125_000), ("Николай", 96_000), ("Пётр",
109_000)]
print(max(lst_1, default='empty'))
print(max(*lst_2))
print(max(lst_3, key=lambda x: x[1]))


# ● Функция min()
# min(iterable, *[, key, default]) или min(arg1, arg2, *args[, key])
# Функция работает аналогично max, но ищет минимальный элемент.

lst_1 = []
lst_2 = [42, 256, 73]
lst_3 = [("Иван", 125_000), ("Николай", 96_000), ("Пётр",
109_000)]
print(min(lst_1, default='empty'))
print(min(*lst_2))
print(min(lst_3, key=lambda x: x[1]))


# Функция sum()
# sum(iterable, /, start=0)
# Функция принимает объект итератор и подсчитывает сумму всех элементов.
# Ключевой аргумент start задаёт начальное значение для суммирования

my_list = [42, 256, 73]
print(sum(my_list))
print(sum(my_list, start=1024))  # старт означает, что к этому значению прибавится сумма чисел в списке



# Функция all()
# all(iterable)
# Функция возвращает истину, если все элементы последовательности являются
# истиной. На Python создание функции all выглядело бы так:
# def all(iterable):
#     for element in iterable:
#         if not element:
#             return False
#         return True

# Функция all обычно применяется с результатами каких-то вычислений, которые
# должны быть истинными или ложными.
numbers = [42, -73, 1024]
if all(map(lambda x: x > 0, numbers)):
    print('Все элементы положительные')
else:
    print('В последовательности есть отрицательные и/или нулевые элементы')

# Функция map заменила числа на True и False, далее all проверила все ли элементы
# больше нуля или есть как минимум один не более нуля.


# Функция any()
# any(iterable)
# Функция возвращает истину, если хотя бы один элемент последовательности
# являются истиной. На Python создание функции any выглядело бы так:

# def any(iterable):
#     for element in iterable:
#         if element:
#             return True
#     return False
# Функция any работает аналогично all. Но если all можно представить как if c
# цепочкой and, то any — это if с цепочкой or.
# Функция map заменила числа на True и False, далее all проверила все ли элементы
# больше нуля или есть как минимум один не более нуля.


numbers = [42, -73, 1024]
if any(map(lambda x: x > 0, numbers)):
    print('Хотя бы один элемент положительный')
else:
    print('Все элементы не больше нуля')


# Функция chr()
# chr(integer)
# Функция возвращает строковой символ из таблицы Юникод по его номеру. Номер -
# целое число от 0 до 1_114_111.
print(chr(97))
print(chr(1105))
print(chr(128510))
# ● Функция ord()
# ord(char)
# Функция принимает один символ и возвращает его код в таблице Юникод.
print(ord('a'))
print(ord('а'))
print(ord('😉'))
# Функции ord и chr выполняют противоположные действия.



# Функция locals()
# Функция возвращает словарь переменных из локальной области видимости на
# момент вызова функции.
# SIZE = 10
# def func(a, b, c):
#     x = a + b
#     print(locals())
#     z = x + c
#     return z
#
# func(1, 2, 3)
# Функция вернула словарь с переменными a, b, c, x и их значениями. Константа SIZE
# не попала в вывод, т.к. не входит в локальную область функции. Так же в словаре
# отсутствует переменная z. Она была впервые создана после вызова функции locals.


# Функция globals()
# Функция возвращает словарь переменных из глобальной области видимости, т.е. из
# пространства модуля.
SIZE = 10
def func(a, b, c):
    x = a + b
    print(globals())
    z = x + c
    return z
print(globals())
print(func(1, 2, 3))
# Функция не сохраняет в словаре локальные переменные функций, даже если будет
# вызвана из тела функции.
# В словаре от globals содержаться и дандер переменные модуля. Они нужны Python
# для правильной работы кода.


# Функция vars()
# Функция без аргументов работает аналогично функции locals(). Если передать в vars
# объект, функция возвращает его атрибут __dict__. А если такого атрибута нет у
# объекта, вызывает ошибку TypeError.
print(vars(int))
# Получили все дандер методы класса int

def my_func(a, b):
    return a ** b


def my_func2(*args):
    return args[0] ** args[1]


def my_func3(a, b):
    return a ** b


def my_func4(**kwargs):
    return kwargs['a'] ** kwargs['b']


func = lambda a, b: a ** b

print(my_func(3, 3))
print(my_func2(3, 3))
print(my_func3(b=5, a=3))
print(my_func4(b=4, a=7))
print(func(2, 2))
print((lambda a, b: a ** b)(3, 3)) # Вызов лямбда функции без переменной