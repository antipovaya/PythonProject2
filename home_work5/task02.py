# Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины: имена str, ставка int, премия str с указанием процентов вида 10.25%.
# В результате result получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
#
# Сумма рассчитывается как ставка умноженная на процент премии.
#
# Не забудьте распечатать в конце результат.
#
# Пример использования.
# На входе:
#
#
names = ["Alice", "Bob", "Charlie"]
salary = [5000, 6000, 7000]
bonus = ["10%", "5%", "15%"]
# На выходе:
#
#
# {'Alice': 500.0, 'Bob': 300.0, 'Charlie': 1050.0}

result = {name: sal * float(bon.rstrip('%'))/100 for name, sal, bon in zip(names, salary, bonus)}

# return {name: salary * float(award.rstrip('%'))/100 for name, salary, award in zip(names, salaries, awards)}
print(result)