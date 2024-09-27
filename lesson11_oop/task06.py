# Задание
# Перед вами несколько строк кода. Напишите что делает класс, не запуская код. У
# вас 3 минуты.
class Count:
    _count = 0
    _last = None

    def __new__(cls, *args, **kwargs):
        if cls._count < 3:
            cls._last = super().__new__(cls)
            cls._count += 1
        return cls._last

    def __init__(self, name: str):
        self.name = name


c1 = Count('Первый')
c2 = Count('Второй')
c3 = Count('Третий')
c4 = Count('Четвертый')

print(f'{c1.name = }, {c2.name = }, {c3.name = }, {c4.name = }')