"""Задание 19 Выполнять одно задание с номером (𝑛 − 1)%𝑚 + 1, где 𝑛 —
номер в списке группы, а 𝑚 — число задач в задании."""

# n = 19 # по прежнему Михайлов
# m = 15 # кол-во. заданий
# print((n - 1) % m + 1) # =4

"""Постройте закрашенную контурную диаграмму и трёхмерный график для
следующих функций двух переменных, определённых в прямоугольной области
𝑥 ∈ [−3; 3], 𝑦 ∈ [−3; 3]:
4. z = x^3 - y^3"""

# import matplotlib.pyplot as plt
# import numpy as np
# from mpl_toolkits.mplot3d import Axes3D

# # Определяем функцию
# def func(x, y):
#   return x**3 - y**3

# # Создаем сетку координат
# x = np.linspace(-3, 3, 100)
# y = np.linspace(-3, 3, 100)
# X, Y = np.meshgrid(x, y)

# # Вычисляем значения функции
# Z = func(X, Y)

# # Строим контурную диаграмму
# fig, ax = plt.subplots()
# contour = ax.contourf(X, Y, Z, 20, cmap='viridis')  # 20 уровней контура, цветовая схема 'viridis'
# ax.clabel(contour, inline=True, fontsize=8)  # Подписи уровней контура
# ax.set_xlabel('x')
# ax.set_ylabel('y')
# ax.set_title('Контурная диаграмма функции z = x^3 - y^3')
# plt.show()

# # Строим 3D-график
# fig = plt.figure()
# ax = fig.add_subplot(projection='3d')
# ax.plot_surface(X, Y, Z, cmap='viridis')  # Цветовая схема 'viridis'
# ax.set_xlabel('x')
# ax.set_ylabel('y')
# ax.set_zlabel('z')
# ax.set_title('3D-график функции z = x^3 - y^3')
# plt.show()