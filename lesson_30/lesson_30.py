"""Задание 30 Выполнять одно задание с номером (𝑛 − 1)%𝑚 + 1, где 𝑛 —
номер в списке группы, а 𝑚 — число задач в задании."""

# n = 19 # по прежнему Михайлов
# m = 15 # кол-во. заданий
# print((n - 1) % m + 1) # =4

"""Сгенерируйте случайный процесс длиною в 10000 значений и постройте гистограмму его распределения для следующих рядов:
4. равномерный шум с параметрами (−𝑎, 𝑎), где 𝑎 — случайное равномерно распределённое число из диапазона [0; 1];"""

# import numpy as np
# import matplotlib.pyplot as plt

# def generate_uniform_noise(n, a):
#   """
#   Генерирует равномерный шум с параметрами (-a, a).

#   Args:
#     n: Количество значений в ряду.
#     a: Верхняя граница для равномерного распределения.

#   Returns:
#     numpy.ndarray: Массив значений равномерного шума.
#   """

#   return np.random.uniform(low=-a, high=a, size=n)

# if __name__ == '__main__':
#   n = 10000  # Длина ряда
#   a = np.random.uniform(low=0, high=1)  # Случайная верхняя граница

#   # Генерируем равномерный шум
#   uniform_noise = generate_uniform_noise(n, a)

#   # Строим гистограмму
#   plt.hist(uniform_noise, bins=50)
#   plt.title('Гистограмма равномерного шума')
#   plt.xlabel('Значение')
#   plt.ylabel('Частота')
#   plt.show()