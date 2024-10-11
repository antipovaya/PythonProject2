# На вход автоматически подаются две строки frac1 и frac2 вида a/b - дробь с числителем и знаменателем.
#
# Напишите программу, которая должна возвращать сумму и произведение дробей. Дроби упрощать не нужно.
#
# Для проверки своего кода используйте модуль fractions.
#
# Пример
# На входе:

import fractions

frac1 = "1/2"
frac2 = "1/3"
# На выходе:
# Сумма дробей: 5/6
# Произведение дробей: 1/6
# Сумма дробей: 5/6
# Произведение дробей: 1/6


numerator1 = int(frac1[0])
denominator1 = int(frac1[2])

numerator2 = int(frac2[0])
denominator2 = int(frac2[2])

n1 = fractions.Fraction(numerator1, denominator1)
n2 = fractions.Fraction(numerator2, denominator2)

print(f'Сумма дробей: {(numerator1 * denominator2 + numerator2 * denominator1)}/{denominator1 * denominator2}')
print(f'Произведение дробей: {(numerator1 * numerator2)}/{denominator1 * denominator2}')
# проверка:
print(f'Сумма дробей: {n1 + n2}')
print(f'Произведение дробей: {n1 * n2}')

