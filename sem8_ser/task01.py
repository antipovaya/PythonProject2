# Задание №1
# Вспоминаем задачу 3 из прошлого семинара. Мы сформировали
# текстовый файл с псевдо именами и произведением чисел.
# Напишите функцию, которая создаёт из созданного ранее
# файла новый с данными в формате JSON.
# Имена пишите с большой буквы.
# Каждую пару сохраняйте с новой строки.

import json

fname = r'C:\Users\keoka\Desktop\Яна учеба\Python\Python\sem7\task_3\task7_3.txt'
jname = 'file_1_8.json'
with open(fname, 'r') as f, open(jname, 'w') as j:
    mydict = {}
    for el in f:
        key, value = el.split('-')

        mydict[key.title()] = float(value)
    json.dump(mydict, j, ensure_ascii=False, separators=(',\n', ':')) #для русского языка ставим False



