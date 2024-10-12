"""Задание 13 Выполнять три задания в зависимости от номера в списке
группы в алфавитном порядке. Необходимо сделать задания №m, №m+5,
№m+10, m=(n-1)%5+1, где 𝑛 — номер в списке группы."""

# n = 19 # по прежнему Михайлов
# m = (n - 1) % 5 + 1 # =4
# print(m, m+5, m+10) # =4, 9, 14

"""Протабулируйте (вычислите значения функций при изменении аргумента в
некоторых пределах с заданным шагом) функции:
4. cos(2𝜋𝑡) на отрезке 𝑡 ∈ [−10; 10] с шагом 1 и с шагом 0.25;
9. ln(𝑥 + 1) на отрезке 𝑥 ∈ [0; 𝑒 − 1] с шагом 0.01 и с шагом 0.001;
14. √3 𝑥 на отрезке 𝑥 ∈ [1; 125] с шагом 1 и с шагом 5, но так, чтобы значения 1 и 5 присутствовали среди аргументов;"""

# import numpy as np
# import math

# # cos(2πt) на отрезке t ∈ [-10; 10]
# print("cos(2πt) на отрезке t ∈ [-10; 10]:")

# # Шаг 1
# t_values = np.arange(-10, 11, 1)
# cos_values = np.cos(2 * np.pi * t_values)
# print("Шаг 1:")
# for i in range(len(t_values)):
#     print(f"t = {t_values[i]:.0f}, cos(2πt) = {cos_values[i]:.4f}")

# # Шаг 0.25
# t_values = np.arange(-10, 11, 0.25)
# cos_values = np.cos(2 * np.pi * t_values)
# print("\nШаг 0.25:")
# for i in range(len(t_values)):
#     print(f"t = {t_values[i]:.2f}, cos(2πt) = {cos_values[i]:.4f}")

# # ln(x + 1) на отрезке x ∈ [0; e - 1]
# print("\nln(x + 1) на отрезке x ∈ [0; e - 1]:")

# # Шаг 0.01
# x_values = np.arange(0, math.e - 1, 0.01)
# ln_values = np.log(x_values + 1)
# print("Шаг 0.01:")
# for i in range(len(x_values)):
#     print(f"x = {x_values[i]:.2f}, ln(x + 1) = {ln_values[i]:.4f}")

# # Шаг 0.001
# x_values = np.arange(0, math.e - 1, 0.001)
# ln_values = np.log(x_values + 1)
# print("\nШаг 0.001:")
# for i in range(len(x_values)):
#     print(f"x = {x_values[i]:.3f}, ln(x + 1) = {ln_values[i]:.4f}")

# # √3 x на отрезке x ∈ [1; 125]
# print("\n√3 x на отрезке x ∈ [1; 125]:")

# # Шаг 1 (включая 1)
# x_values = np.arange(1, 126, 1)
# sqrt3_values = np.sqrt(3) * x_values
# print("Шаг 1 (включая 1):")
# for i in range(len(x_values)):
#     print(f"x = {x_values[i]:.0f}, √3 x = {sqrt3_values[i]:.4f}")

# # Шаг 5 (включая 1 и 5)
# x_values = np.arange(1, 126, 5)
# sqrt3_values = np.sqrt(3) * x_values
# print("\nШаг 5 (включая 1 и 5):")
# for i in range(len(x_values)):
#     print(f"x = {x_values[i]:.0f}, √3 x = {sqrt3_values[i]:.4f}")