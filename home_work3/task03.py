# Дан список повторяющихся элементов lst. Вернуть список с дублирующимися элементами. В результирующем списке не должно быть дубликатов.
#
# Пример
#
# На входе:
#
#
lst = [1, 1, 2, 2, 3, 3]
# На выходе:
#
#
# [1, 2, 3]

temp_list = []
for item in lst:
    if lst.count(item) > 1:
        temp_list.append(item)

print(list(set(temp_list)))


