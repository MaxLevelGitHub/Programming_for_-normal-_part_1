"""Задание 10 (Задания на комбинацию циклов со счётчиком и условием) Выполнять одно задание с номером (n-1)%8+1 в зависимости от номера 𝑛 в списке группы в алфавитном порядке."""

# n = 19 # по прежнему Михайлов
# print((n - 1) % 8 + 1) # =3

"""3. В детском садике n детей играют в следующую игру. Перед ними гора из 𝑚 кубиков, первый ребёнок вынимает из кучи 1 кубик, каждый последующий ребёнок — в два раза больше предыдущего и так по кругу. Если число кубиков, которые нужно вынуть, превышает 25, из него вычитается 25 и отсчёт идёт от уменьшенного числа, например, вместо 32 кубиков будет вынуто 7, затем 14 и т. д. Проигравшим считается тот, кто не смог вытащить нужное число кубиков (в куче осталось недостаточно). Определите проигравшего."""

# n, m = int(input()), int(input())
# cubs, stop = 1, False
# while stop != True:
#     for i in range(1, n+1):
#         if m - cubs >= 0:
#             m -= cubs
#             cubs *= 2
#             if cubs > 25:
#                 cubs -= 25
#         else:
#             print(f'Проиграл {i} ребенок.')
#             stop = True
#             break