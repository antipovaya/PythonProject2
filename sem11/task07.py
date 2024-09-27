from abc import ABC, abstractmethod


class Human(ABC):
    @abstractmethod
    def get_name(self):
        return 'имя'


class Worker(Human):

    def get_name(self):
        return Human.get_name(self)


w1 = Worker()

print(w1.get_name())

# NPV = -450000 + 492000 / (1.19)**1 + 684000 / (1.19)**2 + 756000 / (1.19)**3 + 960000 / (1.19)**4
#
# print(NPV)

# IRR = (- 450000 + 660000) / (1.99*1.99)
#
# print(IRR)