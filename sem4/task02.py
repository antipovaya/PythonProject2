"""
Задание №2
✔ Напишите функцию, которая принимает строку текста.
✔ Сформируйте список с уникальными кодами Unicode каждого
символа введённой строки отсортированный по убыванию.
"""

text = 'Шла Саша по шоссе и сосала сушку'

def text_unicode (text):
    print(sorted([ord(item) for item in text], reverse=True))


text_unicode(text)

