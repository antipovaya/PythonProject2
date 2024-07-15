"""
Задание №5
Работа в консоли в режиме интерпретатора Python.
Посчитайте сумму чётных элементов от 1 до n исключая кратные e.
Используйте while и if.
Попробуйте разные значения e и n.
"""


def even_elements(n, e):
    num = 0
    total = 0
    while num <= n:
        num += 1
        if num % 2 == 0:
            if num % e == 0:
                continue
            total += num

    return total


print(even_elements(20, 3))
