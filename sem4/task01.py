'''
Напишите функцию, которая принимает строку текста.
Вывести функцией каждое слово с новой строки.
✔ Строки нумеруются начиная с единицы.
✔ Слова выводятся отсортированными согласно кодировки Unicode.
✔ Текст выравнивается по правому краю так, чтобы у самого
длинного слова был один пробел между ним и номером строки.
'''
sentence = "Шла саша по шоссе и сосала сушку"


def form_sentence(sentence):
    sentence_split = sorted(sentence.lower().split())
    max_len = len(max(sentence_split, key=len))
    for index, value in enumerate(sentence_split, 1):
        print(f"{index}. {value:>{max_len}} ")


form_sentence(sentence)