"""Задание 3 (Строки) Задания выполняйте все по порядку. =================
    Свяжите любую переменную со строкой: «Мы обязательно научимся программировать!». Извлеките из неё следующие срезы:
1. выведите третий символ этой строки;"""

# print(input()[2])

"""2. выведите предпоследний символ этой строки;"""

# print(input()[-2])

"""3. выведите первые пять символов этой строки;"""

# print(input()[:5])

"""4. выведите всю строку, кроме последних двух символов;"""

# print(input()[:-2])

"""5. выведите все символы с чётными индексами (считая, что индексация начинается с 0);"""

# print(input()[::2])

"""6. выведите все символы с нечётными индексами, то есть, начиная с первого символа строки;"""

# print(input()[1::2])

"""7. выведите четыре символа из центра строки;"""

# t = input() # t - text (full)
# count = len(t)
# tt = int((count - 4) / 2) # tt - text2 (part)
# print((t[tt:-tt] if count % 2 == 0 else t[tt:-tt - 1]))

"""8. выведите символы с индексами, кратными трём;"""

# print(input()[2::3])

"""9. выведите все символы в обратном порядке;"""

# print(input()[::-1])

"""10. выведите все символы строки через один в обратном порядке, начиная с последнего;"""

# print(input()[::-2])

"""11. удалите второе слово из строки;"""

# t = input().split()
# print(*t[:1] + t[2:])

"""12. замените второе слово на строку «никогда не»;"""

# t = input().split()
# print(*t[:1], 'никогда не', *t[2:])

"""13. добавьте в конец строки «на Python»;"""

# print(input(), 'на Python')

"""14. поставьте последнее слово первым в строке;"""

# t = input().split()
# print(t[-1], *t[:-1])

"""15. выведите длину данной строки."""

# print(len(input()))
