# Задание №8
# Нарисовать в консоли ёлку спросив
# у пользователя количество рядов.
# Пример результата:
# Сколько рядов у ёлки? 5
# ----*----
# ---***---
# --*****--
# -*******-
# *********

space = ' '
elem = '*'
rows = 5
spaces = rows - 1
elems = 1
for _ in range(rows):
    print(space * spaces + elem * elems + space * spaces)
    elems += 2
    spaces -= 1

