"""Задание 26 Сгенерируйте 5 рядов y, как это описано в предыдущем задании, пусть ряды отличаются реализациями шума. Для каждого x таким
образом будет доступно по 5 значений y. По этим значениям рассчитайте для каждого x соответствующее ему среднее значение 𝑦¯ и среднеквадратичное отклонение от среднего y. С использованием полученных рядов 𝑦¯(x) и y(x) постройте график средних с планками погрешностей (errorbar)."""

# import numpy as np
# import matplotlib.pyplot as plt
# from numpy.polynomial import Polynomial

# def generate_data(func, interval, noise_func, noise_params, n_series=5):
#   """
#   Генерирует набор значений функции с шумом для нескольких рядов.

#   Args:
#     func: Функция, которую нужно сгенерировать.
#     interval: Интервал, на котором нужно сгенерировать данные.
#     noise_func: Функция, генерирующая шум.
#     noise_params: Параметры для функции шума.
#     n_series: Количество рядов.

#   Returns:
#     tuple: Массивы значений x, y_series (массив из n_series массивов y).
#   """

#   x = np.linspace(interval[0], interval[1], 100)
#   y_series = []
#   for _ in range(n_series):
#     y = func(x)
#     noise = noise_func(*noise_params)
#     y_noisy = y + noise
#     y_series.append(y_noisy)
#   return x, np.array(y_series)

# def calculate_mean_and_std(y_series):
#   """
#   Вычисляет среднее значение и среднеквадратичное отклонение для каждого x.

#   Args:
#     y_series: Массив из n_series массивов y.

#   Returns:
#     tuple: Массивы средних значений y_mean, среднеквадратичных отклонений y_std.
#   """

#   y_mean = np.mean(y_series, axis=0)
#   y_std = np.std(y_series, axis=0)
#   return y_mean, y_std

# def plot_errorbar(x, y_mean, y_std):
#   """
#   Строит график средних значений с планками погрешностей.

#   Args:
#     x: Массив значений x.
#     y_mean: Массив средних значений y.
#     y_std: Массив среднеквадратичных отклонений.
#   """

#   plt.errorbar(x, y_mean, yerr=y_std, fmt='o-', label='Средние значения')
#   plt.xlabel('x')
#   plt.ylabel('y')
#   plt.title('Средние значения с планками погрешностей')
#   plt.legend()
#   plt.show()

# if __name__ == '__main__':
#   # Задаем функцию, интервал и параметры шума
#   func = lambda x: x ** 2 - x - 6
#   interval = [-4, 4]
#   noise_func = np.random.chisquare
#   noise_params = (6, 100)  # 6 степеней свободы, 100 значений

#   # Генерируем 5 рядов данных
#   x, y_series = generate_data(func, interval, noise_func, noise_params, n_series=5)

#   # Вычисляем средние значения и среднеквадратичные отклонения
#   y_mean, y_std = calculate_mean_and_std(y_series)

#   # Строим график средних значений с планками погрешностей
#   plot_errorbar(x, y_mean, y_std)