"""2.8 Задания на работу с основными типами данных ======================
Задание 2 (Арифметические операции) Выполнять три задания в зависимости от номера в списке. Чтобы узнать номера ваших заданий,
необходимо решить задачку: требуется сделать задания № 𝑚, № 𝑚 + 5,
№ 𝑚 + 10, где 𝑚 = (𝑛 − 1)%5 + 1, 𝑛 — порядковый номер студента в списке группы по алфавиту."""

# n = 19 # Михайлов
# m = (n - 1) % 5 + 1 # =4
# print(m, m+5, m+10) # =4, 9, 14

"""Используя арифметические операторы (+, −, *, /, //, %), напишите программу (необходимая информация запрашивается у пользователя с клавиатуры).
4. Сколько нечётных чисел на отрезке [𝑎; 𝑏], если 𝑎 и 𝑏 — чётные? 𝑎 и 𝑏 — нечётные? 𝑎 — чётное, 𝑏 — нечётное? 𝑎 — нечётное, 𝑏 — чётное?"""

# count = 0 # СОМНИТЕЛЬНОЕ ЗАДАНИЕ
# for i in range(int(input()), int(input())+1):
#     if i % 2 != 0: count += 1
# print(count)

"""9. На территории Российской империи до введения метрической системы мер
для измерения объёма жидкости применялись следующие меры: 1 бочка
= 40 вёдер, 1 ведро = 10 штофов, 1 штоф = 10 чарок, 1 чарка = 2 шкалика. Какое полное количество вёдер, штофов, чарок и шкаликов можно
наполнить из 𝐴 бочек? Разлейте имеющееся количество некой жидкости на
𝑥 полных вёдер + 𝑦 полных штофов + 𝑧 полных чарок + 𝑣 шкаликов."""

# barrels = int(input())
# print(
#     'вёдер: ' +    str(barrels * 40),
#     'штофов: ' +   str(barrels * 40 * 10),
#     'чарок: ' +    str(barrels * 40 * 10 * 10),
#     'шкаликов: ' + str(barrels * 40 * 10 * 10 * 2),
#     sep='\n'
# )

"""14. Бревно длиной 𝐿 распилили в 𝑛 местах. Какова средняя длина получившихся кусков?"""

# print(round(int(input()) / int(input()), 1))