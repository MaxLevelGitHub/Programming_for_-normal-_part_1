"""Задание 25 Выполнять одно задание с номером (𝑛 − 1)%𝑚 + 1, где 𝑛 —
номер в списке группы, а 𝑚 — число задач в задании."""

# n = 19 # по прежнему Михайлов
# m = 8 # кол-во. заданий
# print((n - 1) % m + 1) # =3

"""Сгенерируйте набор значений заданной функции с шумом. Аппроксимируйте его полиномом второй степени. Оцените ошибку аппроксимации. Постройте
график. Функции:
3. парабола 𝑦 = 𝑥^2 − 𝑥 − 6 на отрезке [−4; 4] с белым шумом, распределённым по закону 𝜒^2 (random.chisquare) с параметрами (6; 𝑛), где 6 — количество
степеней свободы шума, а 𝑛 — длина ряда 𝑦;"""

# import numpy as np
# import matplotlib.pyplot as plt
# from numpy.polynomial import Polynomial

# def generate_data(func, interval, noise_func, noise_params):
#   """
#   Генерирует набор значений функции с шумом.

#   Args:
#     func: Функция, которую нужно сгенерировать.
#     interval: Интервал, на котором нужно сгенерировать данные.
#     noise_func: Функция, генерирующая шум.
#     noise_params: Параметры для функции шума.

#   Returns:
#     numpy.ndarray: Массив значений функции с шумом.
#   """

#   x = np.linspace(interval[0], interval[1], 100)
#   y = func(x)
#   noise = noise_func(*noise_params)
#   y_noisy = y + noise
#   return x, y_noisy

# def polynomial_approximation(x, y, degree):
#   """
#   Аппроксимирует данные полиномом заданной степени.

#   Args:
#     x: Массив значений x.
#     y: Массив значений y.
#     degree: Степень полинома.

#   Returns:
#     numpy.polynomial.Polynomial: Полином, аппроксимирующий данные.
#   """

#   poly = Polynomial.fit(x, y, degree)
#   return poly

# def calculate_error(y_true, y_pred):
#   """
#   Вычисляет среднеквадратическую ошибку.

#   Args:
#     y_true: Истинные значения.
#     y_pred: Предсказанные значения.

#   Returns:
#     float: Среднеквадратичная ошибка.
#   """

#   error = np.sqrt(np.mean((y_true - y_pred) ** 2))
#   return error

# def plot_results(x, y_true, y_pred, poly):
#   """
#   Строит график с истинными данными, аппроксимированными данными и полиномом.

#   Args:
#     x: Массив значений x.
#     y_true: Истинные значения.
#     y_pred: Предсказанные значения.
#     poly: Полином, аппроксимирующий данные.
#   """

#   plt.plot(x, y_true, label='Истинные данные')
#   plt.plot(x, y_pred, label='Аппроксимированные данные')
#   plt.plot(x, poly(x), label='Полином 2-й степени')
#   plt.legend()
#   plt.title('Аппроксимация параболы полиномом 2-й степени')
#   plt.xlabel('x')
#   plt.ylabel('y')
#   plt.show()

# if __name__ == '__main__':
#   # Задаем функцию, интервал и параметры шума
#   func = lambda x: x ** 2 - x - 6
#   interval = [-4, 4]
#   noise_func = np.random.chisquare
#   noise_params = (6, 100)  # 6 степеней свободы, 100 значений

#   # Генерируем данные с шумом
#   x, y_noisy = generate_data(func, interval, noise_func, noise_params)

#   # Аппроксимируем данные полиномом 2-й степени
#   poly = polynomial_approximation(x, y_noisy, 2)

#   # Вычисляем предсказанные значения
#   y_pred = poly(x)

#   # Оцениваем ошибку
#   error = calculate_error(func(x), y_pred)

#   # Строим график
#   plot_results(x, func(x), y_pred, poly)

#   print(f'Среднеквадратичная ошибка: {error}')