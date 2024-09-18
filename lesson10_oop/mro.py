# MRO
# Аббревиатура MRO — method resolution order переводится как “порядок разрешения
# методов”. Относится этот порядок не только к методам, но и ко всем атрибутам
# класса. Это внутренний механизм, определяющий порядок наследования.
# Забегая вперёд, иногда механизм не справляется с задачей. И чаще всего это
# говорит о сложности кода и неверной логики построения наследования. Т.е.
# нерабочий механизм наследования намекает разработчику на проблемы в его коде.
# Рассмотрим работу MRO на нескольких простых классах.
class A:
    def __init__(self):
        print('Init class A')
        self.data_a = 'A'


class B:
    def __init__(self):
        print('Init class B')
        self.data_b = 'B'


class C:
    def __init__(self):
        print('Init class C')
        self.data_c = 'C'


class D:
    def __init__(self):
        print('Init class D')
        self.data_d = 'D'


class X1(A, C):
    def __init__(self):
        print('Init class X1')
        super().__init__()


class X2(B, D):
    def __init__(self):
        print('Init class X2')
        super().__init__()


class X3(A, D):
    def __init__(self):
        print('Init class X3')
        super().__init__()


class Z(X1, X2, X3):
    def __init__(self):
        print('Init class Z')
        super().__init__()


print(*Z.mro(), sep='\n')

# 1. Четыре класса A, B, C, D не имеют родительского класса. Точнее они
# наследуются от прародителя object. У каждого из классов есть по параметру.
# 2. Далее три класса X имеют по два родительских класса.
# 3. В финале класс Z наследуется от трёх классов X.
# У каждого класса добавили текстовый вывод при вызове методу __init__. Также
# обратите внимание на наличие функции super, которая вызывает инициализацию
# родительского класса.
