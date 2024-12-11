from clickhouse_driver import Client
import json

client = Client('localhost')

import pandas as pd

# Создание базы данных (если она не существует)
client.command('CREATE DATABASE IF NOT EXISTS books_toscrape_com')

# Создание таблицы
client.command('''
CREATE TABLE IF NOT EXISTS books_toscrape_com.books (
    id UInt32,
    category String,
    name String,
    url String,
    price Float32,
    available Int16,
    description String,
    PRIMARY KEY(id)
) ENGINE = MergeTree
ORDER BY id
''')

# заполнение таблицы
column_names = ["id", "category", "name", "url", "price", "available", "description"]
data = [[i]+list(book.values()) for i,book in enumerate(books_data,1)]
client.insert('books_toscrape_com.books', data, column_names=column_names)

# первая запись
result = client.query("SELECT * FROM books_toscrape_com.books")
print(result.result_set[0])

# книги в категории
result = client.query("SELECT * FROM books_toscrape_com.books WHERE category = 'Travel'")
df = pd.DataFrame(result.result_set, columns=column_names)
print(df)

# наличие книг
MIN = 18
MAX = 20
result = client.query(f"SELECT * FROM books_toscrape_com.books WHERE available BETWEEN {MIN} and {MAX}")
df = pd.DataFrame(result.result_set, columns=column_names)
print(df)

# наличие книг по убыванию (первые 10)
result = client.query(f"SELECT TOP 10 category, name, available FROM books_toscrape_com.books ORDER BY available DESC")
df = pd.DataFrame(result.result_set, columns=["category", "name", "available"])
print(df)

# количество книг по китегориям
result = client.query("SELECT category, COUNT(id) as cnt FROM books_toscrape_com.books GROUP BY category ORDER BY cnt DESC")
df = pd.DataFrame(result.result_set, columns=["category", "count"])
print(df)

# средняя цена
result = client.query("SELECT AVG(price) FROM books_toscrape_com.books")
print(f"Средняя цена: {round(result.result_set[0][0], 2)}")

# средняя цена по категориям
result = client.query("SELECT category, AVG(price) as avg_price FROM books_toscrape_com.books GROUP BY category ORDER BY avg_price DESC")
df = pd.DataFrame(result.result_set, columns=["category", "avg_price"])
print(df)