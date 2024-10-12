"""Задание 22 Работа с операционной системой. Задания выполняйте все по порядку.
Напишите две независимые программы. Первую программу, которая создаёт папку Распределения, если она ещё не создана. Далее записывает в неё три
текстовых файла .txt, содержащих последовательность величин, распределённых по равномерному закону, нормальному закону и закону 𝜒^2 с 5 степенями свободы. Необходимые функции ищите в Главе 7, пункт 7.3.
Затем напишите вторую программу, которая переходит в папку Распределения,
находит в ней все текстовые файлы, строит для них гистограммы распределений, сохраняет графики в файлы с таким же названием, как исходный текстовый файл, но другим расширением (.png, .jpg или .pdf)."""

"""Программа 1: Создание файлов с распределениями"""

# import os
# import random
# import numpy as np
# import matplotlib.pyplot as plt

# def generate_uniform(n):
#     """Генерирует n случайных чисел с равномерным распределением"""
#     return [random.uniform(0, 1) for _ in range(n)]

# def generate_normal(n):
#     """Генерирует n случайных чисел с нормальным распределением"""
#     return np.random.normal(loc=0, scale=1, size=n)

# def generate_chi_squared(n, df=5):
#     """Генерирует n случайных чисел с распределением 𝜒^2 с df степенями свободы"""
#     return np.random.chisquare(df=df, size=n)

# def create_distribution_files(directory='Распределения'):
#     """Создаёт папку 'Распределения', если она ещё не создана,
#     затем записывает в неё файлы с распределениями"""
    
#     # Создаём папку, если её нет
#     if not os.path.exists(directory):
#         os.makedirs(directory)

#     # Количество значений в каждом файле
#     n = 1000

#     # Генерируем и сохраняем файлы
#     with open(os.path.join(directory, 'uniform.txt'), 'w') as f:
#         for value in generate_uniform(n):
#             f.write(str(value) + '\n')
    
#     with open(os.path.join(directory, 'normal.txt'), 'w') as f:
#         for value in generate_normal(n):
#             f.write(str(value) + '\n')

#     with open(os.path.join(directory, 'chi_squared.txt'), 'w') as f:
#         for value in generate_chi_squared(n):
#             f.write(str(value) + '\n')

# if __name__ == '__main__':
#     create_distribution_files()

"""Программа 2: Построение гистограмм и сохранение графиков"""

# import os
# import matplotlib.pyplot as plt

# def plot_histograms(directory='Распределения'):
#     """Переходит в папку 'Распределения', находит файлы .txt,
#     строит для них гистограммы и сохраняет графики"""

#     # Переходим в папку
#     os.chdir(directory)

#     # Получаем список файлов .txt
#     txt_files = [f for f in os.listdir() if f.endswith('.txt')]

#     # Строим гистограммы для каждого файла
#     for file in txt_files:
#         # Загружаем данные из файла
#         data = []
#         with open(file, 'r') as f:
#             for line in f:
#                 data.append(float(line.strip()))

#         # Строим гистограмму
#         plt.hist(data, bins=20)

#         # Настраиваем график
#         plt.title(f'Гистограмма распределения {file[:-4]}')
#         plt.xlabel('Значение')
#         plt.ylabel('Частота')

#         # Сохраняем график
#         plt.savefig(file[:-4] + '.png')

#         # Очищаем график
#         plt.clf()

# if __name__ == '__main__':
#     plot_histograms()