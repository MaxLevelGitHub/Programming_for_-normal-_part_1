"""Задание 9 (Задания на цикл со счётчиком) Выполнять три задания в
зависимости от номера в списке группы в алфавитном порядке. Необходимо сделать задания №m, №m+5, №m+10, m=(n-1)%5+1, где 𝑛 — номер в
списке группы."""

# n = 19 # по прежнему Михайлов
# m = (n - 1) % 5 + 1 # =4
# print(m, m+5, m+10) # =4, 9, 14

"""4. Напишите программу, вычисляющую сумму всех нечётных чисел в диапазоне от 𝑎 до 𝑏 включительно (вводятся с клавиатуры)."""

# sum = 0
# for i in range(int(input()), int(input())+1):
#     if i % 2 != 0:
#         sum += i
# print(sum)

"""9. Напечатать таблицу стоимости 100, 200, 300, . . . , 2000 г конфет (стоимость 1 кг конфет вводится с клавиатуры)."""

# cost = int(input())
# for i in range(100, 2001, 100):
#     print(f'{i} г конфет = {int((cost / 1000) * i)}')

"""14. Найти произведение всех целых чисел от 10 до 100 включительно. Обратите внимание, что Python может работать с целыми числами неограниченного размера!"""

# p = 1
# for i in range(10, 101): p *= i
# print(p)