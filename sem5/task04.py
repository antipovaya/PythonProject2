# Задание №4
# ✔ Создайте генератор чётных чисел от нуля до 100.
# ✔ Из последовательности исключите
# числа, сумма цифр которых равна 8.
# ✔ Решение в одну строку.


# my_gen = (num for num in range(0, 101) if num % 2 == 0 and (num//10 + num % 10 != 8))
# for i in my_gen:
#     print(i)
# Вариант 2

[print(i) for i in range(2, 101, 2) if sum(map(int, str(i))) != 8]


# print(*(map(int, str(66))))