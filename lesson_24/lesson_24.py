"""Задание 24 Решите систему линейных уравнений. Матрицу коэффициентов и столбец свободных членов прочитайте из текстовых файлов,
созданных ранее. Запишите в новый текстовый файл полученные корни."""

# import numpy as np

# def solve_linear_system(coefficient_file, constant_file):

#     # Загружаем матрицу коэффициентов из файла
#     with open(coefficient_file, 'r') as f:
#         coefficients = []
#         for line in f:
#             row = [float(x) for x in line.strip().split()]
#             coefficients.append(row)

#     # Загружаем столбец свободных членов из файла
#     with open(constant_file, 'r') as f:
#         constants = [float(line.strip()) for line in f]

#     # Преобразуем списки в матрицы NumPy
#     coefficients = np.array(coefficients)
#     constants = np.array(constants)

#     # Решаем систему уравнений
#     solution = np.linalg.solve(coefficients, constants)

#     return solution

# if __name__ == '__main__':
#     coefficient_file = input('Введите имя файла с матрицей коэффициентов: ')
#     constant_file = input('Введите имя файла со столбцом свободных членов: ')
#     solution = solve_linear_system(coefficient_file, constant_file)

#     # Сохраняем корни в файл
#     with open('solution.txt', 'w') as f:
#         for root in solution:
#             f.write(str(root) + '\n')

#     print('Корни системы сохранены в файл solution.txt')