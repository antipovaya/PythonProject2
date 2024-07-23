'''
✔ Создайте вручную список с повторяющимися целыми числами.
✔ Сформируйте список с порядковыми номерами
нечётных элементов исходного списка.
✔ Нумерация начинается с единицы.
'''

my_list = [1, 4, 2, 4, 5, 3, 5, 6, 23, 45, 23]

# Список для хранения порядковых номеров нечётных элементов
new_list = []

# Проходим по элементам исходного списка
for index, value in enumerate(my_list):
# Проверяем, является ли элемент нечётным
    if value % 2 != 0:
# Добавляем порядковый номер (начиная с 1) в новый список
        new_list.append(index + 1)

# Выводим результат
print(new_list)

print([index+1 for index, value in enumerate(my_list) if value % 2 != 0])