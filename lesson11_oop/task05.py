# Команда del
# Зарезервированное слово del не удаляет объекты в Python. Оно разрывает связь
# между переменной и объектом, на который переменная указывает. После строки с
# del к переменной нельзя обратиться, а у объекта на единицу уменьшается счётчик
# ссылок.
import sys

class User:
    def __init__(self, name: str):
        self.name = name
        print(f'Создал {self.name = }')
    def __del__(self):
        print(f'Удаление экземпляра {self.name}')


u_1 = User('Спенглер')
print(sys.getrefcount(u_1))
u_2 = u_1
print(sys.getrefcount(u_1), sys.getrefcount(u_2))
del u_1
print(sys.getrefcount(u_2))
print('Завершение работы')
# В момент первого вызова метода getrefcount имеем одно значение счётчика ссылок.
# Когда переменная u_2 получает ссылку на тот же объект, счётчик ссылок
# увеличивается на единицу. Команда del уменьшает счётчик на единицу. А удаление
# объекта происходит после завершения кода.
# 🔥 Важно! Счётчик ссылок возвращает значение больше ожидаемого, так
# как сама функция создаёт дополнительную ссылку на объект при вызове.
# Если в коде дописать del u_2 в предпоследней строке, удаление объекта
# произойдёт раньше завершения работы программы. Счётчик ссылок дошёл до нуля
# и сборщик мусора освободил память.