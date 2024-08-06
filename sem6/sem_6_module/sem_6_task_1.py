"""
Задание №1
📌 Вспомните какие модули вы уже проходили на курсе.
📌 Создайте файл, в котором вы импортируете встроенные в
модуль функции под псевдонимами. (3-7 строк импорта).
"""

import math
import random as rnd
from random import choice as ch
from math import exp as e, factorial as fact
import numpy as np
import pandas as pd

arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print([func for func in math.__dir__() if not func.startswith('__')])
[print('\n', func, func.__doc__) for func in rnd.__dir__() if not func.startswith('_')]
print(ch([item for sublist in arr for item in sublist]))
print(e(-3), fact(10))
print(arr.__sizeof__(), np.array(arr).__sizeof__())
print(pd.DataFrame(np.array(arr)))
