# data = list([1, 2, 3])
# print(f'{data = }, {type(data) = }, {type(list) = }')
#
#
# class Person:
#     max_up = 3
#
#
# p1 = Person()
# print(p1.max_up)
# print(Person.max_up)
#
# class Person:
#     max_up = 3
#
#
# p1 = Person()
# p2 = Person()
# print(f'{Person.max_up = }, {p1.max_up = }, {p2.max_up = }')
# p1.max_up = 12
# print(f'{Person.max_up = }, {p1.max_up = }, {p2.max_up = }')
# Person.max_up = 42
# print(f'{Person.max_up = }, {p1.max_up = }, {p2.max_up = }')


# class Person:
#     max_up = 3
#
#
# p1 = Person()
# p2 = Person()
# Person.level = 1
# print(f'{Person.level = }, {p1.level = }, {p2.level = }')
# p1.health = 100
# print(f'{Person.health = }, {p1.health = }, {p2.health = }') #AttributeError: type object 'Person' has no attribute 'health'
# print(f'{p1.health = }, {p2.health = }') # AttributeError:'Person' object has no attribute 'health'
# print(f'{p1.health = }')



# Конструктор экземпляра
# При создании класса обычно используют функцию конструктор __init__.
class Person:
    max_up = 3
    def __init__(self):
        self.level = 1
        self.health = 100


p1 = Person()
p2 = Person()
print(f'{p1.max_up = }, {p1.level = }, {p1.health = }')
print(f'{p2.max_up = }, {p2.level = }, {p2.health = }')
print(f'{Person.max_up = }, {Person.level = }, {Person.health =}') # AttributeError: type object 'Person' has no attribute'level'
Person.level = 100
print(f'{Person.level = }, {p1.level = }, {p2.level = }')

