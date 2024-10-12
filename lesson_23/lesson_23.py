"""7.5 Задания на использование встроенных библиотек numpy
Задание 23 Найдите определитель матрицы. Матрицу возьмите из
текстового файла, созданного ранее, либо у преподавателя."""

# import numpy as np

# def calculate_determinant(filename):

#     # Загружаем матрицу из файла
#     with open(filename, 'r') as f:
#         matrix = []
#         for line in f:
#             row = [float(x) for x in line.strip().split()]
#             matrix.append(row)

#     # Преобразуем список списков в матрицу NumPy
#     matrix = np.array(matrix)

#     # Вычисляем определитель
#     determinant = np.linalg.det(matrix)

#     return determinant

# if __name__ == '__main__':
#     filename = input('Введите имя файла с матрицей: ')
#     determinant = calculate_determinant(filename)
#     print(f'Определитель матрицы: {determinant}')