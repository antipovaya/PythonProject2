"""
Задание №3
Создайте класс-генератор.
Экземпляр класса должен генерировать факториал числа в
диапазоне от start до stop с шагом step.
Если переданы два параметра, считаем step=1.
Если передан один параметр, также считаем start=1.
"""


class FactorialGenerator:
    def __init__(self, stop, start=1, step=1):
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        self.n = self.start
        return self

    def __next__(self):
        if self.n > self.stop:
            raise StopIteration
        factorial = 1
        for i in range(1, self.n + 1):
            factorial *= i
        self.n += self.step
        return factorial


if __name__ == "__main__":
    generator = FactorialGenerator(5) # start=1, step=1 по умолчанию
    for factorial in generator:
        print(factorial)