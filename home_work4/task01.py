# Напишите функцию для транспонирования матрицы transposed_matrix, принимает в аргументы matrix, и возвращает транспонированную матрицу.
#
# Пример использования На входе:
#
#
# matrix = [[1, 2, 3],
#          [4, 5, 6],
#          [7, 8, 9]]
# transposed_matrix = transpose(matrix)
# На выходе:
#
#
# [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

matrix = [[1, 2, 3, 5],
          [4, 5, 6, 7],
          [7, 8, 9, 2]]


# print(len(matrix[0]))


def transpose(matrix):
    """Функция для транспонирования матрицы, принимает в аргументы matrix, и возвращает
    транспонированную матрицу."""
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]


if __name__ == '__main__':
    print(transpose(matrix))
