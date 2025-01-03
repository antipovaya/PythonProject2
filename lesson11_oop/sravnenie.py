# 5. Сравнение экземпляров класса

# Числа сравниваются по значению, строки посимвольно. Но при желании можно
# сравнивать любые объекты Python реализовав перечисленные ниже дандер
# методы.
# ● __eq__ - равно, ==
# ● __ne__ - не равно, !=
# ● __gt__ - больше, >
# ● __ge__ - не больше, меньше или равно, <=
# ● __lt__ - меньше, <
# ● __le__ - не меньше, больше или равно, >=
# Перечисленные методы попарно противоположны. Обратите внимание на
# приставку не в списке. Реализовав один из пары, второй Python попытается
# получить инвертируя значение. Не истина — это ложь, а не ложь — это истина.
# При реализации метода обычно принято возвращать True или False. Если
# возвращается другое значение в конструкциях вида if x == y:, Python применит
# функцию bool() к результату для получения True или False.
# Сравнение на идентичность, __eq__
# Создадим класс треугольник, который хранит длины трёх сторон. В первом
# варианте не будем прописывать дандер __eq__ и попробуем сравнить экземпляры.

# class Triangle:
#
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def __str__(self):
#         return f'Треугольник со сторонами: {self.a}, {self.b}, {self.c}'
#
#
# one = Triangle(3, 4, 5)
# two = one
# three = Triangle(3, 4, 5)
# print(one == two)
# print(one == three)

# Переменные one и two равны, т.к. ссылаются на один и тот же объект в памяти. А вот
# треугольники one и three считаются разными хоть и имеют одинаковые длины
# сторон. Дело в том, что Python по умолчанию добавляет метод __eq__ следующего
# вида.
# def __eq__(self, other):
# return self is other
# Как вы помните is сравнивает адреса объектов в памяти. Следовательно проверка
# по умолчанию это: True if id(self) == id(other) else False.
# А теперь напишем свою проверку на идентичность. Допустим возможность
# переворачивания треугольника перед сравнением. Например треугольники со
# сторонами 3, 4, 5 и 4, 3, 5 будем считать равными.


# class Triangle:
#
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def __str__(self):
#         return f'Треугольник со сторонами: {self.a}, {self.b}, {self.c}'
#
#     def __eq__(self, other):
#         first = sorted((self.a, self.b, self.c))
#         second = sorted((other.a, other.b, other.c))
#         return first == second
#
#
# one = Triangle(3, 4, 5)
# two = one
# three = Triangle(3, 4, 5)
# four = Triangle(4, 3, 5)
# print(f'{one == two = }')
# print(f'{one == three = }')
# print(f'{one == four = }')
# print(f'{one != one = }')


# Функция sorted получает кортеж из трёх сторон и возвращает их в упорядоченном
# виде. Сравнив оба списка поэлементно определяем равны треугольники или нет.
# Обратите внимание на последнюю строку. Проверка на неравенство не вызвала
# ошибку. Python вызвал дандер __eq__, а к результату применил команду not.
# 24
# Сравнение на больше и меньше
# При необходимости сравнивать объекты не только на равенство, можно
# реализовать дополнительные методы сравнения. Например для работы сортировки
# используется метод __lt__, проверяющий какой из пары элементов меньше.
# Доработаем класс треугольника и будем сравнивать их по площади. Для
# вычисления площади напишем отдельный метод, использующий формулу Герона.


from math import sqrt


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        return f'Треугольник со сторонами: {self.a}, {self.b}, {self.c}'

    def __repr__(self):
        return f'Triangle({self.a}, {self.b}, {self.c})'

    def __eq__(self, other):
        first = sorted((self.a, self.b, self.c))
        second = sorted((other.a, other.b, other.c))
        return first == second

    def area(self):
        p = (self.a + self.b + self.c) / 2
        _area = sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
        return _area

    def __lt__(self, other):
        return self.area() < other.area()


one = Triangle(3, 4, 5)
two = Triangle(5, 5, 5)
print(f'{one} имеет площадь {one.area():.3f} у.е.²')
print(f'{two} имеет площадь {two.area():.3f} у.е.²')
print(f'{one > two = }\n{one < two = }')
data = [Triangle(3, 4, 5), Triangle(6, 2, 5), Triangle(4, 4, 4),
        Triangle(3, 5, 3)]
result = sorted(data)
print(result)
print(', '.join(f'{item.area():.3f}' for item in result))

# Рассмотрим получившийся код:
# ● дандер __init__ и __str__ остались без изменений
# ● дандер __repr__ нужен для вывода читаемого списка экземпляров
# ● дандер __eq__ также не изменился
# ● метод area вычисляет площадь треугольника по формуле Герона:
# ○ находим p как половину суммы длин сторон
# ○ вычисляем площадь как корень из произведения p на разность p с
# каждой из сторон
# ● дандер __lt__ вызывает для каждого из сравниваемых экземпляров метод
# area и возвращает результат сравнения площадей: True или False.
# В основном коде создали пару треугольников, посмотрели на их площадь и
# убедились, что сравнения на больше так же работает и возвращает обратное от
# сравнения на меньше.
# Далее создали список треугольников и отсортировали их. Визуальная проверка
# площадей подтверждает, что треугольники были упорядочены именно на основе их
# сравнения.
