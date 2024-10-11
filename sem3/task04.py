'''
✔ Создайте вручную список с повторяющимися элементами.
✔ Удалите из него все элементы, которые встречаются дважды
'''


my_list = [1, 5, 3, 5, 2, 2, 5]

count_dict = {}
for item in my_list:
    count_dict[item] = count_dict.get(item, 0) + 1  # Возвращает значение из словаря по указанному ключу.
# dict.get(key[, default]) -> Значение по ключу, либо default.
# key : Ключ, значение по которому требуется получить.
# default : Значение, которое следует вернуть, если в словаре не окажется указанного ключа. По умолчанию — None.

my_list_copy = my_list[:]

for i in range(len(my_list_copy)):
    if count_dict[my_list_copy[i]] == 2:
        my_list.remove(my_list_copy[i])

print(my_list)
