"""Задание 8 (Задания на цикл с условием) Выполнять три задания в зависимости от номера в списке группы в алфавитном порядке. Необходимо сделать задания №m, №m+5, №m+10, m=(n-1)%5+1, где 𝑛 — номер в списке группы."""

# n = 19 # по прежнему Михайлов
# m = (n - 1) % 5 + 1 # =4
# print(m, m+5, m+10) # =4, 9, 14

"""4. Напишите программу, которая будет суммировать вводимые с клавиатуры
числа до тех пор, пока они чётные."""

# sum = 0
# while True:
#     n = int(input())
#     if n % 2 == 0:
#         sum += n
#     else:
#         break
# print(sum)

"""9. Напишите программу, которая запрашивает у пользователя числа до тех пор, пока каждое следующее число больше предыдущего. В конце программа сообщает, сколько чисел было введено."""

# count, max = 0, 0
# while True:
#     n = int(input())
#     if n > max:
#         max = n
#         count += 1
#     else:
#         break
# print(count)

"""14. Дано натуральное число, в котором все цифры различны. Определить порядковый номер его минимальной цифры, считая номера: от конца числа; от начала числа."""

# n = list(input())
# min_n = 9

# for i in range(len(n)-1, 0, -1): # от конца числа
#     if int(n[i]) < min_n:
#         min_n = int(n[i])

# for i in range(len(n)): # от начала числа
#     if int(n[i]) < min_n:
#         min_n = int(n[i])

# print(min_n)