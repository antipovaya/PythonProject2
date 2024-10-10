# 4. Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа должна подсказывать
# “больше” или “меньше” после каждой попытки. Для генерации случайного числа используйте код:
# from random import randintnum = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint


num = randint(0, 1001)
#print(num)
i = 10
while i != 0:
    try:
        num_user = int(input("Введите свой вариант: "))
        if num_user == num:
            print(f"Ура! Вы угадали, загаданное число: {num}")
            break
        elif num_user > num:
            print(f"Не угадали, загаданное число меньше.")
            i -= 1
            print(f"Осталось {i} попыток")
        else:
            print(f"Не угадали, загаданное число больше.")
            i -= 1
            print(f"Осталось {i} попыток")
    except ValueError:
        print("Неверный формат, пожалуйста введите число")

