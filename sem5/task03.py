# Задание №3
# ✔ Продолжаем развивать задачу 2.
# ✔ Возьмите словарь, который вы получили.
# Сохраните его итераторатор.
# ✔ Далее выведите первые 5 пар ключ-значение,
# обращаясь к итератору, а не к словарю.


text = 'Это строка текста'

dct1 = {char: ord(char) for char in text}

print(dct1)

iteratorV = iter(dct1.values())
iteratorK = iter(dct1.keys())
print(next(iteratorK), next(iteratorV))
print(next(iteratorK), next(iteratorV))
print(next(iteratorK), next(iteratorV))
print(next(iteratorK), next(iteratorV))
print(next(iteratorK), next(iteratorV))

# либо:

count = 5
my_iter = iter(dct1.items())
for _ in range(count):
    print(next(my_iter))















