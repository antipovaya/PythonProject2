# Наследование
# В Python все объекты являются наследниками класса object. В начале лекции мы
# рассмотрели пример создания класса:
# class Person:
# pass
# Представленная запись создания класса является упрощённой. На самом деле
# класс Person наследуется от класса object. Т.е. object — родительский класс для
# Person, а Person — дочерний класс для object.
# class Person(object):
# pass
# 🔥 Важно! Наследование от object принято опускать при создании класса.
# Создадим класс героя на основе класса персонажа.


class Person:
    __max_up = 3
    _max_level = 80
    def __init__(self, name, race='unknown', speed=100):
        self.name = name
        self.race = race
        self.level = 1
        self.health = 100
        self._speed = speed
        self.up = 3
    def _check_level(self):
        return self.level < self._max_level
    def level_up(self):
        if self._check_level():
            self.level += 1
    def change_health(self, other, quantity):
        self.health += quantity
        other.health -= quantity

    def add_up(self):
        self.up += 1
        self.up = min(self.up, self.__max_up)

class Hero(Person):
    def __init__(self, power, *args, **kwargs):
        self.power = power
        super().__init__(*args, **kwargs)


p1 = Hero('archery', 'Сильвана', 'Эльф', 120)
print(f'{p1.name = }, {p1.up = }, {p1.power = }')

