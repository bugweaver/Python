# LESSON 1
# import random

# name = "Elena"  # инициализация переменной
# print("Hello,", name)

# age = 20
# text = "Hello"
# print(text + str(age))
# print(type(age))

# LESSON 2

# number = 6 + 4 * 5 ** 2 + 7
# print(number)

# num = 10
# num += 5
# print(num)
#
# num -= 3
# print(num)

# num = 4325
# print("Исходное число: ", num)
# a = num % 10
# print(a)
# num //= 10
#
# b = num % 10
# print(b)
# num //= 10
#
# c = num % 10
# print(c)
# num //= 10
# print(num)

# num = 4325
# print("Исходное число: ", num)
# res = num % 10 * 1000
# num //= 10
# res += num % 10 * 100
# num //= 10
# res += num % 10 * 10
# num //= 10
# res += num % 10
# print(res)

# num1 = '2.3'
# num2 = 3
# # # res = num1 + str(num2)
# res = float(num1) + num2
# print(res)

# print(int(3.8))
# print(round(3.891, 2))
# print(type(round(3.8424, 2)))

# name = "Виктор"
# age = 28
# print("Меня зовут " + name + ". Мне " + str(age) + " лет.")
# print("Меня зовут ", name, ". Мне ", str(age), " лет.", sep="", end=" ")
# print("Я учу Python")

# name = input("Напиши имя: ")
# print(name)

# num = int(input("Введите число: "))
# power = int(input("Введите степень: "))
# res = num ** power
# print(res)

# b1 = True
# b2 = False
# print(b1 + 5)  # 1 + 5
# print(b2 + 5)  # 0 + 5

# print(bool("python"))
# print(bool(""))
# print(bool(-0.2))
# print(bool(0))

# print(7 == 7)
# print(2 + 5 == 7)
# print(7 != 10 - 7)

# print(2 < 4 < 9)
# print(2 * 5 > 7 >= 4 + 3)
# print(3 * 3 <= 7 >= 2)

# print(5 - 3 == 2 and 1 + 3 == 4)
# print(5 - 3 == 2 and 1 + 3 < 4)

# print(9 - 7)
# print(not 9 - 7)

# cnt = 5
# if cnt < 10:
#     cnt += 2
#     print(cnt)

# a = 15
# b = 25
# if a > b:
#     print("a > b")
# elif a < b:
#     print("a < b")
# else:
#     print("a == b")

# a = input("Введите первую сторону: ")
# b = input("Введите вторую сторону: ")
# c = input("Введите третью сторону: ")
#
# if a == b or a == c or b == c:
#     print("Треугольник равнобедренный")
# elif a == b == c:
#     print("Треугольник равносторонний")
# else:
#     print("Треугольник разносторонний")

# day = int(input("Введите день недели (цифрой): "))
# if (day >= 1) and (day <= 5):
#     print("Рабочий день - ")
# elif day == 6 or day == 7:
#     print("Выходной день - ")
# else:
#     print("Такого дня не существует")

# n = int(input("Введите количество ворон: "))
# if 0 <= n <= 9:
#     print("На ветке", n, end=" ")
#     if n == 1:
#         print("ворона")
#     elif 2 <= n <= 4:
#         print("вороны")
#     else:
#         print("ворон")
#
# else:
#     print("Ошибка ввода данных")


# password = "qwerty"
# match password:
#     case 'admin':
#         print("Администратор")
#     case 'user':
#         print("Пользователь")
#     case _:
#         print("Логин не найден")

# day = 'вторник'
# time = 15
# match day:
#     case 'понедельник' | 'вторник' | 'среда' | 'четверг' | 'пятница' if 9 <= time <= 13 or 15 <= time <= 16:
#         print("Рабочий день")
#     case "суббота" | "воскресенье":
#         print("Выходной день")
#     case _:
#         print("Такого дня недели не существует или не рабочее время")

# a, b = 30, 20
#
# print(a if a < b else b)

# a, b = 20, 30
#
# print("a == b" if a == b else "a > b" if a > b else "b > a")

# a = 5
# b = 1
# print("на ноль делить нельзя" if b == 0 else a / b)
# try:
#     n = int(input("Введите целое число: "))
#     print(n * 2)
# except ValueError:
#     print("Что-то пошло не так")


# try:
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print(n / m)
# except (ValueError, ZeroDivisionError):
#     print("Нельзя вводить строки")
#     print("Нельзя делить на ноль")
# else:  # когда в блоке try не возникло исключения
#     print("Все нормально. Вы ввели числа", n, "и", m)
# finally:  # выполниться в любом случае
#     print("Конец программы")


# n = input("Введите первое число:")
# m = input("Введите второе число:")
#
# try:
#     n = int(n)
#     m = int(m)
# except ValueError:
#     n = str(n)
# finally:
#     print(n + m)

# Циклы
# while

# i = 10
# while i > 0:
#     print("i =", i)
#     i -= 1

# i = 1
# while i <= 20:
#     if i % 2 == 0:
#         print("i =", i)
#     i += 1

# n = int(input("Введите количество символов: "))
# i = 0
# while i < n:
#     print("*", end="")
#     i +=1
# print("*" * n)

# a = int(input("Введите начало диапазона: "))
# b = int(input("Введите конец диапазона: "))
# summ = 0
# while a <= b:
#     if a % 2:
#         summ += a
#     a += 1
# print(summ)

# n = int(input("Введите количество символов: "))
# symbol = input("Тип символа: ")
# orient = int(input("0 - горизонтальная\n1 - вертикальная\n ориентация линии: "))
# i = 0
# while i < n:
#     if orient == 0:
#         print(symbol, end=' ')
#     if orient == 1:
#         print(symbol)
#     i += 1


# n = input("Введите целое число: ")
#
# while type(n) is not int:
#     try:
#         n = int(n)
#     except ValueError:
#         print("Число не целое!")
#         n = input("Введите целое число: ")
#
# if n % 2 == 0:
#     print("Четное")
# else:
#     print("Нечетное")


# i = 0
# while i < 10:
#     if i == 3:
#         i += 1
#         continue
#     print(i, end=" ")
#     if i == 5:
#         break
#     i += 1
# print("\n Цикл завершен")

# i = 0
# while True:
#     n = int(input("Введите положительное число:"))
#     i += 1
#     if n < 0:
#         break

# res = 1
# while True:
#     n = int(input("Введите число: "))
#     if n == 0:
#         break
#     res *= n
# print(res)

# i = 0
# while i < 10:
#     print(i, end=" ")
#     i += 1
# else:
#     print("\nЦикл окончен, i=", i)

# i = 1
# while i < 5:
#     print("Внешний цикл: i =", i)
#     j = 1
#     while j < 4:
#         print("\t Внутренний цикл: j =", j)
#         j += 1
#     i += 1

# i = 1
# while i < 10:
#     j = 1
#     while j < 10:
#         print(i, "*", j, "=", i * j , end="\t\t")
#         j += 1
#     print()
#     i += 1

# i = 1
# while i < 5:
#     j = 0
#     while j < 16:
#         if i % 2 == 0:
#
#             print("+", end="")
#         else:
#             print("-", end="")
#         j += 1
#     print()
#     i += 1

# i = 0
# while i < 5:
#     j = 0
#     while j < i:
#         print(" ", end="")
#         j += 1
#     print("*")
#     i += 1

# i = 0
# while i < 5:
#     print(" " * i, "*")
#     i += 1

# for i in "Hello!":
#     print(i)

# for i in range(2,9):
#     print(i)

# a = int(input("Введите целое число: "))
# for i in range(1, a + 1):
#     if a % i == 0:
#
#         print(i, end=" ")


# for i in range(10, 100):
#     if i % 10 == i // 10:
#         print(i, end=' ')

# for i in range(3):
#     print(i)
#     if i == 1:
#         break
# else:
#     print("done")

# for i in range(3):
#     print("+++ i =", i)
#     for j in range(2):
#         print("----- j =", j)

# w = 16
# h = 4
# for i in range(h):
#     for j in range(w):
#         print("*", end="")
#     print()
#
# w = 16
# h = 4
# for i in range(h):
#     for j in range(w):
#         if i == 0 or i == h - 1 or j == 0 or j == w - 1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

# nums = [letter for letter in "Banana"]
# print(nums)

# nums = [i for i in range(30) if i % 2 == 0]
# print(nums)

# Список (list)
# nums = [8, 3, 9, 4, 1, "one"]
# print(nums)
# for i in range(len(nums)):
#     print(i)

# s = []
# print(s)
#
# b = list("Hello")
# print(b)

# n = list(range(1, 6, 2))
# print(n)


# [выражение for переменная in последовательность]

# a =[0 for i in range(5)]
# print(a)
# b =[i for i in range(5)]
# print(b)
#
# a, b = [1, 2, 3], [4, 5]
# c = a + b
# print(c)
# d = b * 3
# print(d)

# a = [0] * int(input("Введите количество элементов списка: "))
# print(a)
# for i in range(len(a)):
#     a[i] = input("-> ")
# print(a)

# a = [input() for i in range(int(input("Введите количество элементов списка: ")))]
# print(a)

# a = [int(input()) for i in range(int(input("Введите количество элементов списка: ")))]
# print(a)
# j = 0
# for i in a:
#     if i < 0:
#         j += i
# print(j)

# a = list(range(10, 200, 10))
# print(a)
#
# for i in range(len(a)):
#     print(a[i], end=" ")
# print()
#
# for i in a:
#     print(i, end=" ")

# n = list(range(21, 41))
# print(n)
# s = k = 0
# for i in range(len(n)):
#     if n[i] % 2 == 0:
#         k += 1
#     else:
#         s += n[i]

# for i in n:
#     if i % 2 == 0:
#         k += 1
#     else:
#         s += i
#
# print(k)
# print("sum нечетных элементов: ", s)

# a = [int(input()) for i in range(int(input("Введите количество элементов списка: ")))]
# for i in range(1, len(a)):
#     if a[i] > a[i - 1]:
#         print(a[i], end=" ")
# a = [7, 8, 2, 1, 17, 9]
# print(a)
# # a[0], a[1] = a[1], a[0]
# # print(a)
# print(a[1:4])
# print(a[1:])
# print(a[:3])
# print(a[::-1])

# s = [5, 9, 3, 7, 1, 8]
# s[1:3] = [0, 0, 0, 0]
# print(s)
# s[1:2] = [20]
# print(s)
# s[2:5] = []
# print(s)
# Методы списков
# s = [5, 9, 3, 7, 1, 8]
# print(s)
# s.append(99)  # добавляет элемент в конец списка
# print(s)
# s.extend([1, 2, 3])  # добавляет список элементов в конец списка
# print(s)
# s.extend('add')
# print(s)
# s.insert(0, 100)  # добавляет элемент (второй параметр), в заданный индекс (первый параметр)
# print(s)
# s = []
# n = int(input("Кол0во элементов в списке: "))
# for num in range(n):
#     while True:
#         x = int(input("Введите число:"))
#         if x % 3 == 0:
#             s.insert(0, x)
#             break
#         else:
#             print(x, "не кратное 3")
# print(s)

# s = []
# n = int(input("Кол-во элементов: "))
# for num in range(n):
#     x = int(input("Введите число кратное 3: "))
#     if x % 3 == 0:
#         s.append(x)
#     else:
#         print("Число не кратно 3: ")
#
# print(s)
#
# a = [5, 9, 2, 1, 4, 3]
# b = [4, 2, 1, 3, 7]
# c = []
# for i in a:
#     for j in b:
#         if i in c:
#             continue
#         if i == j:
#             c.append(i)
#             break
# print(c)


# s = []
# n = int(input("Кол-во элементов: "))
# for num in range(n):
#     x = int(input("Введите число: "))
#     s.append(x)
# a = int(input("Введите индекс: "))
# s.pop(a)
#
# print(s)
#
# a = [1, 2, 3]
# b = a.copy()
# a.append(20)
# print(a, b)
# b.append(120)
# print(a, b)

# a = [5, 4, 1, 2, 3]
# print(a)
# a.reverse()
# print(a)
# a.sort()
# print(a)
# a.sort(reverse=True)
# print(a)

# b = ["Виталий", "Сергей", "Александр", "Анна"]
# b.sort(key=len, reverse=True)
# print(b)

# a = [5, 4, 1, 2, 3]
# print(a)
# sort = sorted(a, reverse=True)
# print(sort)

# Генерация случайных данных
# import random
#
# print(random.random())
# print(random.randint(3, 9))
# print(random.randrange(3, 9))
# print(random.uniform(10.5, 25.5))
# city_list = ['Москва', 'Новосибирск', 'Воронеж', 'Сочи', 'Екатеринбург']
# # print(random.choices(city_list, k=3))
# random.shuffle(city_list)
# print(city_list)

# import random
# mas = [random.randint(0, 20) for i in range(10)]
# max_ = max(mas)
# print(max_)
# mas.remove(max_)
# mas.insert(0, max_)
# print(mas)
# import random
# mas = [random.randint(0, 100) for i in range(10)]
# print(mas)
#
# min_ch = min(mas)
# print(min_ch)
#
# ind_min = mas.index(min_ch)
# print(ind_min)
# del mas[:ind_min]
# print(mas)

# x = list('1a2b3c4d')
# print(x)
# print('a' in x)
# print('e' in x)

# n1 = int(input("Введите размер первого списка: "))
# n2 = int(input("Введите размер второго списка: "))
# a = [random.randint(0, 10) for i in range(n1)]
# b = [random.randint(0, 10) for j in range(n2)]
# print("Первый список:", a)
# print("Второй список:", b)
# c = a + b
# print("Третий список:", c)
#
# c = []
# for i in a:
#     if i in b and i not in c:
#         c.append(i)
# print("Элементы общие для двух списков:", c)
#
# c = [min(a), min(b), max(a), max(b)]
# print(c)

# import random
# w, h = 4, 3
# matrix = [[random.randint(1,30) for x in range(w)]for y in range(h)]
# matrix = []
# for y in range(h):
#     new_row = []
#     for x in range(w):
#         new_row.append(0)
#     matrix.append(new_row)
# print(matrix)

# for row in matrix:
#     for x in row:
#         print(x, end="\t")
#     print()
#
# import random
# w, h = 3, 4
# matrix = [[random.randint(-20,10) for x in range(w)]for y in range(h)]
#
# m = 0
# for row in matrix:
#     for x in row:
#         print(x, end="\t")
#         if x < 0:
#             m += 1
#     print()
#
# print("Количество отрицательных элементов:", m)

# for x, y in [[1,2], [3,4], [5,6], [7,8]]:
#     print(x, "+", y, "=", x + y)

# import math as m
# from math import *
# num1 = sqrt(4)
# print(num1)

# import time
# seconds = time.time()
# print("Количество секунд", seconds)
# locale_time = time.ctime()
# print("Местное время:", locale_time)

# Function

# def hello():
#     print("Hello")
# hello()


# def get_sum(a, b, c=0, d=1):
#     return a + b + c + d
#
#
# print(get_sum(1, 5, 2, 7))
# print(get_sum(1, 5, 2))
# print(get_sum(1, 5))
# n1 = 1
# n2 = 5
# n4 = 2
# print(get_sum(1, 5, d=n4))


# def set_param(c=20, s='-'):
#     print(s * c)
#
#
# set_param()
# set_param(7)
# set_param(5, '*')
# set_param(s="#")


# def digit_sum(n, even=True):
#     s = 0
#     while n > 0:
#         current = n % 10
#         if even and current % 2 == 0:
#             s += current
#         elif not even and current % 2:
#             s += current
#         n //= 10
#     return s
#
#
# print("\nСумма четных цифр: ")
# print(digit_sum(9874023))
# print(digit_sum(38271))
# print(digit_sum(123456789))
# print("\nСумма нечетных цифр: ")
# print(digit_sum(9874023, even=False))
# print(digit_sum(38271, even=False))
# print(digit_sum(123456789, even=False))

# def display_info(name, age):
#     print("Name:", name, "\nAge:", age)
#
#
# display_info("Ira", 23)

# Изменяемые и неизменяемые объекты

# lt1 = [1, 2, 3]
# lt2 = [1, 2, 3]
# print(id(lt1))
# print(id(lt2))
# print(lt1 == lt2)
# print(lt1 is lt2)
#
# a = "Hello"
# b = "Hello"
# print(id(a))
# print(id(b))
# print(a == b)
# print(a is b)

# n = 5
# print(id(n))
# n = 6
# print(id(n))

# n = [1, 2, 3]
# print(id(n))
#
# n.append(4)
# print(n)
# print(id(n))

# Кортеж(tuple)

# lst = [10, 20, 30]
# tpl = (10, 20, 30)
# print(lst.__sizeof__())
# print(tpl.__sizeof__())


# a = (5,)
# print(type(a))
# print(a)
# b = tuple()
# print(type(b))

# n = [1, 2, 3]
# b = tuple(("Hello", "Python"))
# print(type(b))
# print(b)

# a = (1, 2, 3, 4, 5, 6)
#
# print(a[3])
# print(a[1:3])

# from random import randint
# s = tuple(randint(0, 100) for i in range(5))
# print(s)

# tpl = tuple(2 ** i for i in range(1, 13))
# print(tpl)

# t1 = tuple("hello")
# t2 = tuple('world')
# print(t1)
# print(t2)
# # print(t1 * 2)
# t3 = t1 + t2
# print(t3.)


# def slicer(tpl, el):
#     if el in tpl:
#         if tpl.count(el) > 1:
#             a = tpl.index(el)
#             b = tpl.index(el, a+1)
#             return tpl[a:b + 1]
#         else:
#             return tpl[tpl.index(el):]
#     else:
#         return ()
#
#
# print(slicer((1, 2, 3), 8))
# print(slicer((1, 8, 3, 4, 8, 8, 9, 2), 8))
# print(slicer((1, 2, 8, 5, 1, 2, 9), 8))

# countries = (
#     ("Германия", 80.2, (("Берлин", 3.326), ("Гамбург", 1.718))),
#     ("Франция", 66, (("Париж", 2.2), ("Марсель", 1.6)))
# )
# print(countries, end="\n\n")
#
# for country in countries:
#     country_name, country_population, cities = country
#     print("\nСтрана:", country_name, "население =", country_population)
#     for city in cities:
#         city_name, city_population = city
#         print("\tГород:", city_name, "население =", city_population)


# print("Вносим изменения")

# print("Склонированный репозиторий")

# Множества (set)

# s = {"banana", "apple", "orange", "banana", "apple"}
# print(s)

# c = ["red", "blue", "green", "red"]
# a = set(c)
# print(a, type(a))

# mas = [1, 2, 3, 2, 3, 4, 4, 5]
# s = {x for x in mas}
# print(s)

#
# def to_set(elem):
#     return set(elem), len(elem)
#
#
# print(to_set("я обычная строка"))
# print(to_set([4, 5, 4, 6, 2, 9, 11, 3, 4, 2]))


# def to_set(element):
#     st = set(element)
#     return st, len(st)
#
#
# print(to_set('я обычная строка'))
# print(to_set([4, 5, 4, 6, 2, 9, 11, 3, 4, 2]))

# t = {"red", "green", "blue"}
# for i in t:
#     print(i)

# r = ['ab_1', 'ac_2', 'bc_1', 'bc_2']
# # a = ["A" + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in r]
# a = ["A" + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in r if i[1] == 'c']
# print(a)

# a = {'Tom', 'Bob', 'Alice'}
# print(a)
# a.add('Ann')
# print(a)
# a.remove("Ann")  # при обращении к несуществующему элементу - ошибка KeyError
# print(a)
# user = "Ann"
# if user in a:
#     a.remove(user)
# print(a)


# a.discard("Ann")
# n = a.pop()
# print(n)
# a.pop()
# a.clear()
# print(a)
# print(n)


# a = {0, 1, 2, 3}
# b = {4, 3, 2, 1}
# # # c = a | b
# # a |= b
# # print(a)
#
# a ^= b
# print(a)

# s1 = {1, 2}
# s2 = {3}
# s3 = {4, 5}
# s4 = {3, 2, 6}
# s5 = {6}
# s6 = {7,8}
# s7 = {9, 8}
#
# # s = s1.union(s2, s3, s4, s5, s6, s7)
# s = s1 | s2 | s3 | s4 | s5 | s6 | s7
# print(s)

# s1 = "Hello"
# s2 = "How are you"
# a = set(s1) & set(s2)
# print(a)
# for i in a:
#     print(i, end=" ")

# drawing = {"Марина", "Женя", "Света"}
# music = {"Костя", "Женя", "Илья"}
#
# one_hobby = drawing ^ music
# print("Один кружок: ", one_hobby)
#
# both_hobbies = drawing & music
# print("Оба кружка", both_hobbies)
#
# drawing -= both_hobbies
# print(drawing)

# a = {0, 1, 2, 3, 4}
# b = {3, 2, 1}
# print(a <= b)
# print(a >= b)


# Тип frozenset
# s = frozenset([1, 2, 3, 4, 5])
# print(s)
# print(type(s))
# a = frozenset({"hello", "world"})

# Словарь (dict)
# lst = [1, 2, 3]
# d = {'one': 1, 'two': 2, 'three': 3, 4: 'four'}
# lst[0] = 10
# print(lst[0])
#
# d['one'] = 10
# print(d['one'])
# print(d[4])

# d = {}
# print(d)
# print(type(d))
# d1 = dict(one=1, two=2)

# d = {'x1': 3, 'x2': 7, 'x3': 5, 'x4': -1}
# m = 1
# for i in d:
#     m *= d[i]
#
# print(m)


# goods = {
#     '1': ['Core-i3-4330', 9, 4500],
#     '2': ['Core-i5-4670K', 3, 8500],
#     '3': ['AMD FX-6300', 6, 3700],
#     '4': ['Pentium G3220', 8, 2100],
#     '5': ['Core-i5-3450', 5, 6400],
# }
#
# for i in goods:
#     print(i, ")", goods[i][0], ' - ', goods[i][1], " шт. по ", goods[i][2], 'руб', sep="")
#
# while True:
#     n = input('№: ')
#     if n != '0':
#         qty = int(input('Количество: '))
#     try:
#         goods[n][1] = qty
#     except KeyError:
#         pass
#     else:
#         break
#
# for i in goods:
#     print(i, ")", goods[i][0], ' - ', goods[i][1], " шт. по ", goods[i][2], 'руб', sep="")


# d = {'x1': 3, 'x2': 7, 'x3': 5, 'x4': -1}
# item = d.popitem()
# print(item)


# Задание 1
# vowels = set('аеёиоуыэюя')
# message = input("Введите строку: ")
# count = 0
# for i in message:
#     if i in vowels:
#         count += 1
# print("Количество гласных равно: ", count)


# Задание 2
# dict1 = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
# dict2 = {'name': dict1.pop('name'), 'salary': dict1.pop('salary')}
# print(dict1)
# print(dict2)

# d = {'a': 1, 'c': 3, 'b': 2}
# d1 = {'r': 7, 'q': 40}
# d. update(d1)
# d2 = [('a', 20), ('b', 9)]
# d.update(d2)
# print(d)

# x = {'a': 1, 'b': 2}
# y = {'b': 3, 'c': 4}
# z = x | y
# # z.update(x)
# # z.update(y)
# print(z)

# a = {
#     'first': {
#         1: 'one',
#         2: 'two',
#         3: 'three'
#     },
#     'second': {
#         4: 'four',
#         5: 'five'
#     }
# }
# print(a)
# for x in a:
#     print(x)
#     for y in a[x]:
#         print('\t', y, ": ", a[x][y], sep='')


# sales = {"John": {"N": 3056, "S": 8463, "E": 8441, "W": 2694},
#          "Tom": {"N": 4832, "S": 6786, "E": 4737, "W": 3612},
#          "Anne": {"N": 5239, "S": 4802, "E": 5820, "W": 1859},
#          "Fiona": {"N": 3904, "S": 3645, "E": 8821, "W": 2451}}
#
# for x in sales:
#     print(x)
#     for y in sales[x]:
#         print('\t', y, ": ", sales[x][y], sep='')

# person = input("Имя: ")
# region = input("Регион: ")
# print(sales[person][region])
# new_data = int(input("Новое значение: "))
#
# sales[person][region] = new_data
# print(sales[person])


# d = {"N": 3056, "S": 8463, "E": 8441, "W": 2694}
# d = {value: key for key, value in d.items()}
# print(d)


# d = {"N": 1, "S": 2, "E": 3, "W": 4}
# new_d = {k: v for k, v in d.items() if v <= 2}
# print(new_d)

# a = ["one", 1, 2, 3, "two", 10, 20, "three", 15, 36, 60, "four", -20]
#
# d = dict()
# current_key = ""
# for item in a:
#
#     if type(item) is str:
#         d[item] = []
#         current_key = item
#     else:
#         d[current_key].append(item)
#
# print(d)

# d = dict(zip([1, 2, 3, 4], ['one', 'two', 'three']))
# print(d)
#
# a = [1, 2, 3]
# b = ['one', 'two', 'three']
# f = {k: v for k, v in zip(a, b)}
# print(f)


# one = {'apple': 0.45, 'orange': 0.35}
# two = {'pepper': 0.2, 'onion': 0.55}
# print({**one, **two})

# month = ["January", "February", "March"]
# total_sales = [52000.00, 51000.00, 48000.00]
# prod_cost = [46800.00, 45900.00, 43200.00]
#
# for sales, costs, m in zip(total_sales, prod_cost, month):
#     profit = sales - costs
#     print("Чистая прибыль в", m, "=", profit)


# a = [1, 2, 3]
# b = [*a, 4, 5, 6]
# print(b)


# def func(*args):
#     return args
#
#
# print(func(2))
# print(func(2, 3, 4, "abc"))

# def summa(*params):
#     res = 0
#     for i in params:
#         res += i
#     return res
#
#
# print(summa(1, 2, 3, 4, 5, 6, 7, 8, 9))
# print(summa(3, 4, 5))


# def to_dict(*args):
#     return {element: element for element in args}
#
#
# print(to_dict(1, 2, 3, 4))
# print(to_dict("grey", (2, 17), 3.11, -4))


# def num(*args):
#     res = 0
#     for i in args:
#         res += i
#     c = res / len(args)
#     for i in args:
#         if i < c:
#             print(i)
#
#
# print(num(1, 2, 3, 4, 5, 6, 7, 8, 9))
# print(num(3, 6, 1, 9, 5))


#
# def func(**kwargs):
#     return kwargs
#
#
# print(func(a=1, b=2, c=3))
# print(func())
# print(func(d=9))


# def outer(who):
#     def inner():
#         print("Hello,", who)
#
#     inner()
#
#
# outer("World!")


# def fun1():
#     a = 6
#
#     def fun2(b):
#         a = 4
#         print(a + b)
#
#     print('a:', a)
#     fun2(4)
#
#
# fun1()
# x = 25
# t = 0
#
#
# def fn():
#     global t
#     a = 30
#
#     def inner():
#         nonlocal a
#         a = 35
#         print("a:", a)
#
#     inner()
#     t = a
#
#
# fn()
# c = x + t
# print(c)
# x = 5
#
# def fn1():
#     x = 25
#
#     def fn2():
#         # x = 33
#
#         def fn3():
#             nonlocal x
#             x = 55
#
#         fn3()
#         print("fn2.x =", x)
#
#     fn2()
#     print("fn1.x =", x)
#
# fn1()


# def outer(a1, b1, a2, b2):
#     a = 0
#     b = 0
#
#     def inner():
#         nonlocal a, b
#         a = a1 + a2
#         b = b1 + b2
#
#     inner()
#     return [a, b]
#
#
# res = outer(2, 3, -1, 4)
# print(res)


# Замыкание

# def outer(n):
#     def inner(x):
#         return n + x
#
#     return inner
#
#
# item1 = outer(5)
# print(item1(10))
#
# item2 = outer(5)
# print(item1(1))


# def func1():
#     a = 1
#     b = 'line'
#     c = [1, 2, 3]
#
#     def func2():
#         nonlocal a, b
#         c.append(4)
#         a = a + 1
#         b += "_new"
#         return a, b, c
#
#     return func2
#
#
# func = func1()
# print(func())


# def func(city):
#     s = 0
#
#     def inner():
#         nonlocal s
#         s += 1
#         print(city, s)
#
#     return inner
#
#
# res1 = func("Москва")
# res1()
# res1()
# res1()
# res2 = func('Сочи')
# res2()
# res1()


# lambda(анонимные функции)

# print((lambda x, y: x + y)(1, 2))
#
# func = lambda x, y: x + y
# print(func(1, 2))


# print((lambda x, y: x ** 2 + y ** 2)(2, 5))

# y = (
#     lambda x: x * 2,
#     lambda x: x * 3,
#     lambda x: x * 4
# )
# for i in y:
#     print(i('abc__'))

# def outer(n):
#     def inner(x):
#         return x + n
#
#     return inner
#
#
# f = outer(5)
# print(f(10))
#
#
# def outer1(n):
#     return lambda x: x + n
#
#
# f1 = outer(5)
# print(f1(10))
#
# outer2 = lambda n: lambda x: + n
# f2 = outer2(5)
# print(f1(10))
#
# print((lambda n: lambda x: x + n)(5)(10))


# func = (lambda a, b, c: a + b + c)
# print(func(2, 4, 5))


# d = {'b': 3, 'c': 1, 'a': 2}
# lst = list(d.items())
# print(lst)
# lst.sort(key=lambda i: i[1])
# print(lst)
# d1 = dict(lst)
# print(d1)

# players = [
#     {'name': 'Антон', 'last name': 'Бирюков', 'rating': 9}
# ]

# a = [
#     lambda x, y: x + y,
#     lambda x, y: x - y,
#     lambda x, y: x * y,
#     lambda x, y: x / y
# ]
#
# print(a[0](5, 2))


# d = {
#     1: lambda: print('Понедельник'),
#     2: lambda: print('Вторник'),
#     3: lambda: print('Среда'),
#     4: lambda: print('Четверг'),
#     5: lambda: print('Пятница'),
#     6: lambda: print('Суббота'),
#     7: lambda: print('Воскресенье')
# }
#
# d[6]()


# print((lambda a, b, c: a if (a < b and a < c) else b if (b < c and b < a) else c)(15, 13, 1))


# 1

# month = ["January", "February", "March"]
# total_sales = [52000.00, 51000.00, 48000.00]
# prod_cost = [46800.00, 45900.00, 43200.00]
# for t, p, m in zip(total_sales, prod_cost, month):
#     print("Общая прибыль в", m, "=", t - p)

# 2

# n = int(input("Количество студентов: "))
# data = dict()
# for i in range(n):
#     name = input(f'{i + 1}-й студент: ')
#     numb = int(input("Балл: "))
#     a = {name: numb}
#     data.update(a)
# 
# 
# def func(args):
#     middle = sum(args) // len(args)
#     print(middle)
#     for k, v in data.items():
#         if v > middle:
#             print(k)
#     res = []
#     for element in args:
#         if element > middle:
#             res.append(element)
#     return res
# 
# 
# f = func(data.values())


# import math
#
# d = {
#     'circle': lambda x: math.pi * x * x,
#     'rectangle': lambda x, y: x * y,
#     'trapezoid': lambda x, y, z: (x + y) * z / 2
# }
# print("Площадь окружности:", d['circle'](2))
# print("Площадь прямоугольника:", d['rectangle'](10, 13))
# print("Площадь трапеции:", d['trapezoid'](7, 5, 3))


# 13/1/2024

# map(func, *iterables)

# def mult(t):
#     return t * 2


# lst1 = [2, 8, 12, -5, -10]

# lst2 = list(map(mult, lst1))  # к каждому элементу применил функцию mult
# lst2 = list(map(lambda t: t * 2, lst1))
# print(lst2)

# t = (2.88, -1.75, 100.55)
# t2 = tuple(map(lambda x: int(x), t))
# t2 = tuple(map(int, t))
# print(t2)


# st = ['a', 'b', 'c', 'd', 'e']
# num = [1, 2, 3, 4, 5]
#
# res = list(map(lambda x, y: (x, y), st, num))
# print(res)

# num = ['1', '2', '3', '4', '5']
# print(list(map(int, num)))

# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
# res = list(map(lambda x, y: x + y, l1, l2))
# print(res)


# t = ('abcd', 'abc', 'asdfg', 'def', 'grt')
# t2 = tuple(filter(lambda s: len(s) == 3, t))
# print(t2)

# b = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
# res = list(filter(lambda s: s > 75, b))
# print(res)


# m = list(map(lambda x: x ** 2, filter(lambda x: x % 2, range(10))))
# print(m)
# n = [x ** 2 for x in range(10) if x % 2]
# print(n)

# import random
#
# b = [random.randint(1, 40) for i in range(40)]
# c = list(filter(lambda num: 10 <= num <= 20, b))
# print(c)

# def hello():
#     return 'Hello, I am func "hello"'
#
#
# def super_func(func):
#     print("Hello, i am func 'super_func'")
#     print(func())
#
#
# super_func(hello)


# def hello():
#     return 'Hello, I am func "hello"'
#
#
# test = hello
# print(test())


# def my_decorator(func):
#     def wrap():
#         print("Код до функции")
#         func()
#         print("Код после функции")
#
#     return wrap
#
#
# def func_test():
#     print("Hello, I am func 'func_test'")
#
#
# test = my_decorator(func_test())
# test()


# def my_decorator(func):  # декорирующая функция
#     def wrap():
#         print("Код до функции")
#         func()
#         print("Код после функции")
#
#     return wrap
#
#
# @my_decorator  # декоратор
# def func_test():  # декорируемая функция
#     print("Hello, I am func 'func_test'")
#
#
# @my_decorator
# def hello():
#     return 'Hello, I am func "hello"'
#
#
# func_test()
# hello()


# def bold(fn):
#     def wrap():
#         return "<b>" + fn() + "</b>"
#
#     return wrap
#
#
# def italic(fn):
#     def wrap():
#         return "<i>" + fn() + "</i>"
#
#     return wrap
#
#
# @italic
# @bold
# def hello():
#     return "text"
#
#
# print(hello())

# def cnt(fn):
#     count = 0
#
#     def wrap(arg1, arg2):
#         nonlocal count
#         count += 1
#         fn(arg1, arg2)
#         print("Вызов функции:", count)
#
#     return wrap
#
#
# @cnt
# def hello(a, b):
#     print("Hello,", a, "\nHello,", b)
#
#
# hello("Python", "JavaScript")

# def args_decorator(fn):
#     def wrap(*args, **kwargs):
#         print("args", args)
#         print("kwargs", kwargs)
#         fn(*args, **kwargs)
#
#     return wrap
#
#
# @args_decorator
# def print_data(a, b, c, study="Python"):
#     print(a, b, c, "изучают", study, "\n")
#
#
# print_data("Борис", "Елизавета", "Светлана", study="JavaScript")
# print_data("Владимир", "Екатерина", "Виктор")

# def decor(args1, args2):
#     def args_dec(fn):
#         def wrap(x, y):
#             print(args1, x, args2, y, "=", end=" ")
#             fn(x, y)
#
#         return wrap
#
#     return args_dec
#
#
# @decor("Сумма:", "+")
# def summa(a, b):
#     print(a + b)
#
#
# @decor("Разность:", "-")
# def sub(a, b):
#     print(a - b)
#
#
# summa(5, 2)
# sub(5, 2)


# def multiply(arg):
#     def test(fn):
#         def wrap(x):
#             return fn(x) * arg
#
#         return wrap
#
#     return test
#
#
# @multiply(3)
# def return_num(num):
#     return num
#
#
# print(return_num(5))

# def avg(fn):
#     def wrap(*a):
#         print(fn(*a) / len(a))
#
#     return wrap
#
#
# @avg
# def summa(*args):
#     print(sum(args))
#     return sum(args)
#
#
# summa(2, 3, 3, 4)


# 14/1/2024

# print(int('18'))
# print(int(18.5))
# print(int('18.5'))


# print(int('100', 2))  # 4
# print(int('100', 8))  # 64
# print(int('100', 10))  # 100
# print(int('100', 16))  # 256
#
# print(bin(18))  # 0b10010
# print(oct(18))  # 0o22
# print(hex(18))  # 0x12


# q = 'Pyt'
# w = 'hon'
# e = q + w
# print(e)
# print(e * 3)

# def changeCharToStr(s, c_old, c_new):
#     s2 = ''
#     i = 0
#
#     while i < len(s):
#         if s[i] == c_old:
#             s2 += c_new
#         else:
#             s2 += s[i]
#         i += 1
#     return s2
#
#
# str1 = "Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования. "
# str2 = changeCharToStr(str1, "N", "P")
# print(str2)


# print("Привет")
# print(u"Привет")

# print("C:\\Folder\\file.txt\\")
# print(r"C:\Folder\file.txt\\"[:-1])
# print(r"C:\Folder\file.txt" + '\\')


# name = "Дмитрий"
# age = 25
# print(f'Меня зовут {name}, мне {age} лет')
#
# m = 2.532236256
# print(f'Число: {m:.3f}')


# s = """
# Многострочный
# текст
# """

# def square(n):
#     """Принимает число n, возвращает квадрат числа n"""
#     return n ** 2
#
#
# print(square(5))
# print(square.__doc__)
# print(sum.__doc__)


# from math import pi
#
#
# def cylinder(r, h):
#     """
#     Вычисляет площадь цилиндра
#
#     Вычисляет площадь цилиндра на основании заданной высоты и радиуса основания
#     :param r: положительное число, радиус основания цилиндра
#     :param h: положительное число, высота цилиндра
#     :return:  положительное число, площадь цилиндра
#     """
#     return 2 * pi * r * (r + h)
#
#
# print(cylinder(2, 4))


# s = "Test string for me"
# arr = [ord(x) for x in s]
# print("ASCII коды", arr)
# arr = [int(sum(arr) / len(arr))] + arr
# print(arr)
# arr += [x for x in input("-> ")[:3]]
# print(arr)

# a = 122
# b = 97
# if a > b:
#     for i in range(b, a + 1):
#         print(chr(i), end=' ')
# elif a < b:
#     for i in range(a, b + 1):
#         print(chr(i), end=' ')
# else:
#     print(chr(a))


# from random import randint
#
# SHORTEST = 7
# LONGEST = 10
# MIN_ASCII = 33
# MAX_ASCII = 126
#
#
# def random_password():
#     random_length = randint(SHORTEST, LONGEST)
#     result = ""
#     for i in range(random_length):
#         result += chr(randint(MIN_ASCII, MAX_ASCII))
#     return result
#
#
# print("Ваш случайный пароль:", random_password())


# s = "hello, WORLD! I am learning Python."
# print(s.capitalize())  # преобразует первый символ в верхний регистр, а все остальные - в нижний
# print(s.lower())  # возвращает строку, в которой все буквы в нижний регистр
# print(s.upper())  # возвращает строку, в которой все буквы в верхний регистр
# print(s.swapcase())  # возвращает строку, в которой все символы строки находятся в противоположном исходному регистре
# print(s.title())  # возвращает строку, в которой все первые буквы слов в верхний регистр
# print(s)
# print(s.count("h"))  # возвращает количество точных вхождение подстроки в строку
# print(s.count('h', 1, -4))
# print(s.find("Python"))  # Ищет в строке подстроку и возвращает ее индекс, если совпадения не найдено,
# то возвращает -1
# print(s.find("Python", 10, -20))
# print(s.find("l"))
# print(s.rfind("l"))

# print(s.index("l"))  # Ищет в строке подстроку и возвращает ее индекс, если совпадения не найдено,
# # возвращает исключение ValueError
# print(s.rindex("l"))


# s = input("Введите два слова через пробел: ")
# word1 = s[:s.find(" ")]
# word2 = s[s.find(" ") + 1:]
# print(word2 + " " + word1)

# s = "hello, WORLD! I am learning Python."
# print(s.startswith("hello"))  # возвращает True, если строка начинается с указанной подстроки
# print(s.find("I am"))
# print(s.startswith("I am", 14))
#
# print(s.endswith("on."))  # возвращает True, если строка заканчивается с указанной подстроки

# print("abc123".isalpha())
# print('123'.isdigit())
# print('abc123'.isalnum())

# print('abc'. islower())

# print('py'.center(10, "-"))

# удаляют пробельные символы слева или справа
# print("     p y".lstrip())
# print("p y     ".rstrip())

# print("https://www.python.org".lstrip("/:pths"))


# str1 = "Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования."
# print(str1.replace("Nython", "Python"))
# print(str1.replace("Nython", "Python", 2))

# s1 = '-'
# seq = ('a', 'b', 'c')
# print(s1.join(seq))
# print("..".join(['1', '2']))  # объединение итерируемой последовательности (состоит из строковых значений) в строку
# print(":".join("Hello"))

# s = "hello, WORLD! I am learning Python."
# print(s.split())
# print('www.python.org'.split('.', 1))

# a = input("Введите ФИО: ").split()
# print(a[0], a[1][0] + ".", a[2][0] + ".")

# a = input("Введите коды символов через пробел: ").split()
# print(a)
# b = list(map(int, a))
# print(b)
# import re
#
# s = "Я ищу совпадения в 2024 году. И я их найду в 2 счёта. 198765 Hello[-World]"
# reg = r'[a-zA-Z\]\[-]'
# print(re.findall(reg, s))  # возвращает список, который содержит все совпадения с шаблоном регулярных выражений
#
# print(re.search(reg, s))  # возвращает месторасположение первого совпадения с шаблоном
# print(re.search(reg, s).span())
# print(re.search(reg, s).start())
# print(re.search(reg, s).end())
# print(re.search(reg, s).group())

# print(re.match(reg, s))  # возвращает месторасположение совпадения с шаблоном, но только в начале строки


# st = "Час в 24-часовом формате от 00 до 23. 2021-06-15Е21:59. Минуты, в диапазоне от 00 до 59. 2021-06-15T01:09."
# reg = r'\d'
# print(re.findall(reg, st))

# d = "Цифры: 7, +17, -42, 0013, 0.3"
# print(re.findall(r"[+-]?\d+", d))

# st = "05-03-1987 # Дата рождения"
# # print("Дата рождения:", re.sub(r'#.*', '', st).replace('-', '.'))
# print("Дата рождения:", re.sub('-', '.',re.sub(r'#.*', '', st)))


# import re
#
# st = "author=Пушкин A.C.; title = 'Евгений Онегин'; price =200; year= 1831"
# req = r"\w+\s*=\s*[^;]+"
# print(re.findall(req, st))


# import re
#
# st = '+74994564578, 74994564578'
# req = r'[+]?7[\d]*'
# print(re.findall(req, st))

# 1
# s = "I am learning Python. hello, WORLD!"
# new_s = s[:s.find('h') + 1] + s[s.find('h') + 1:s.rfind('h')][::-1] + s[s.rfind('h'):]
# print(new_s)

# 2
# import re
# s = "123456@i.ru, 123_456@ru.name.ru, login@i.ru, логин-1@i.ru, login.3@i.ru, login.3-67@i.ru, 1login@ru.name.ru"
# print(re.findall(r'[\w.-]+@\w+[.\w+]+', s))


# 27/1/2024
# import re

# text = "<body>Пример жадного соответствия регулярных выражений</body>"
# print(re.findall("<.*?>", text))


# s = "<p>Изображение <img  alt='картинка' src='bg.jpg'> - фон страницы</p>"
# # reg = r'<img.*?>'
# reg = r'<img\s+[^>]*src\s*=\s*[^>]+>'
# print(re.findall(reg, s))


# text = "Python (в русском языке встречаются названия пито́н[16]или па́йтон[17]) — высокоуровневый язык " \
#        "программирования общего назначения с динамической строгой типизацией " \
#        "и автоматическим управлением памятью[18][19]."
# print(re.findall(r'\[.*?]', text))

# s = "Петр, Ольга и Виталий отлично учатся!"
# reg = 'Петр|Виктор|Ольга'
# print(re.findall(reg, s))

# s = "int = 4, float = 4.0f, double = 8.0"
# # reg = r'\w+\s*=\s*\d[.\w]*'
# # reg = r'(?:int|float)\s*=\s*\d[.\w]*'
# reg = r'(int|float)\s*=\s*(\d[.\w]*)'
# print(re.findall(reg, s))


# (?:...) - это группирующая скобка является не сохраняющей


# s = "127.168.255.255"
# # reg = r'\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}'
# reg = r'(?:\d{1,3}.){3}\d{1,3}.'
# print(re.findall(reg, s))

# s = '5 + 7*2 - 4'
# reg = r'\s*([+*-])\s*'
# print(re.split(reg, s))

# a = '01-08-2021'
# pattern = '(0[1-9]|[12][0-9]|[3][01])-(0[1-9]|1[0-2])-(19[0-9][0-9]|20[0-9][0-9])'
# print(re.findall(pattern, a))

# text = """
# Самара
# Москва
# Тверь
# Уфа
# Казань
# """


# count = 0
#
#
# def repl_find(m):
#     global count
#     count += 1
#     return f"<option value='{count}'>{m.group(1)}</option>\n"
#
#
# print(re.sub(r'\s*(\w+)\s*', repl_find, text))


# s = "<p>Изображение <img src=\"bg.jpg\" - фон страницы</p>"
# reg = r'<img\s+[^>]*src\s*=(['\"])(.+?)\1>'

# s = "<p>Изображение <img src=\"bg.jpg\"> - фон страницы </p>"
# # reg = r"<img\s+[^>]*src\s*=(['\"])(.+?)\1>"
# reg = r"<img\s+[^>]*src\s*=(['\"])(.+?)(?P=q)>"
# print(re.findall(reg, s))


# s = "Самолет прилетает 10/23/2024. Будем рады вас видеть после 10/24/2024"
# reg = r'(\d{2})/(\d{2})/(\d{4})'
# print(re.sub(reg, r'\2.\1.\3', s))

# s = "yandex.com and yandex.ru"
# reg = r'(([a-z0-9-]{0,}\.)+[a-z]{2,4})'
# print(re.sub(reg, r'http://\1', s, re.IGNORECASE))


# 28.01.2024
# Рекурсивная функция - это функция, вызывающая саму себя


# def elevator(n):
#     if n == 0:
#         print("Вы в подвале")
#         return
#     print("=>", n)
#     elevator(n - 1)
#     print(n, end=' ')
#
#
# n1 = int(input("На каком вы этаже: "))
# elevator(n1)


# def sum_list(lst):
#     if len(lst) == 1:
#         print(lst, "=> lst[0]", lst[0])
#         return lst[0]
#     else:
#         print(lst, "=> lst[0]", lst[0])
#         return lst[0] + sum_list(lst[1:])
#
#
# print(sum_list([1, 3, 5, 7, 9]))


# def to_str(n, base):
#     convert = '0123456789ABCDEF'
#     if n < base:
#         return convert[n]
#     else:
#         return to_str(n // base, base) + convert[n % base]
#
#
# print(to_str(254, 16))


# names = ['Adam', ['Bob', ['Chet', 'Cat'], 'Bard', 'Bert'], 'Alex', ['Bea', 'Bill'], 'Ann']
# print(names)


# print(isinstance(names[0], list))
# def count_item(lst):
#     count = 0
#     for item in lst:
#         if isinstance(item, list):
#             count += count_item(item)
#         else:
#             count += 1
#     return count
#
#
# print(count_item(names))


# def remove(text):
#     if not text:
#         return ""
#     if text[0] == "\t" or text[0] == " ":
#         return remove(text[1:])
#     else:
#         return text[0] + remove(text[1:])
#
# print(remove(" Hello\tWorld"))


# Файлы

# Текстовые
# Бинарные

# f = open("text.txt", "r")
# count = 0
# for i in f:
#     count += 1
# print(count)
# f.close()

# f = open("xyz.txt", 'w')
# f.write("Hello\nWorld\n")
# f.close()


# 1
# import re
#
# s = "+7 499 456-45-78, +74994564578, 7 (499) 456 45 78, 7 (499) 456-45-78"
# print(re.findall(r"[+]?7\s?[(]?\d{3}[)]?\s?\d{3}-?\s?\d{2}-?\s?\d{2}", s))

# 2
# def count_negative(numbers):
#     if len(numbers) == 0:
#         return 0
#     elif numbers[0] < 0:
#         return 1 + count_negative(numbers[1:])
#     else:
#         return count_negative(numbers[1:])
#
#
# print('n =', count_negative([-2, 3, 8, -11, -4, 6]))


# 2/1/2024


# def negative_numbers(a):
#     if not a:
#         return 0
#     else:
#         count = negative_numbers(a[1:])
#         if a[0] < 0:
#             count += 1
#         return count
#
#
# lst = [-2, 3, 8, -11, -4, 6]
# print(negative_numbers(lst))


# f = open('xyz.txt', 'w')
# lst = [str(i) for i in range(1, 20)]
# print(lst)
# for index in lst:
#     f.write(index + '\t')
# f.close()


# f = open("text2.txt", "w")
# f.write("Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл;\n")
#
# f.close()

# f = open('text2.txt')
# rl = f.readlines()
# f.close()
# print(rl)
# rl[1] = "Hello World\n"
# print(rl)
#
#
# f = open('text2.txt', 'w')
# f.writelines(rl)
# f.close()

# filename = "text2.txt"
# f = open(filename, "r")
# rl = f.readlines()
# f.close()
#
# print(rl)
#
# pos = 1
# if pos < len(rl):
#     rl.pop(pos)
#
# print(rl)
#
# f = open(filename, "w")
# f.writelines(rl)
# f.close()

# f = open('text.txt', 'r')
# print(f.read(3))
# print(f.tell())  # возвращает текущую позицию уловного курсора в файле
# print(f.seek(1))  # переместил условный курсор в заданную позицию
# f.close()

#
# f = open('text.txt', 'r+')
# print(f.write("I am learning Python"))
# f.close()

# with open('test.txt', 'w+') as f:
#     print(f.write('01234\n56789'))
#
# with open('test.txt', 'r') as f:
#     for line in f:
#         print(line)


# def longest_worlds(file):
#     with open(file, encoding="utf-8") as text:
#         w = text.read().split()
#         max_length = len(max(w, key=len))
#         res = [word for word in w if len(word) == max_length]
#         return res
#
#
# print(longest_worlds('words.txt'))


# 4/2/2024

# Модуль OS и OS.PATH


# print(os.getcwd())  # путь к текущей директории
# print(os.listdir())  # список директорий и файлов
# print(os.listdir(".."))

# os.mkdir('folder1')  # создание папки
# os.makedirs("nested/nested2/nested3")  # создание папки с промежуточными директориями

# os.rmdir("folder1")  # удаление папки

# os.remove('xyz.txt')

# os.rename("nested1", 'test')  # переименовали папку

# for root, dirs, files in os.walk('test'):
#     print("Root:", root)
#     print('Subdirs', dirs)
#     print("Files:", files)

# def remove_empty_dirs(root_tree):
#     print(f'Удаление пустых директорий в ветви {root_tree}')
#     print('-' * 50)
#
#     for root, dirs, files in os.walk(root_tree):
#         if not os.listdir(root):
#             os.rmdir(root)
#             print(f'Директория {root} удалена')
#     print('-' * 50)
#
#
# remove_empty_dirs('test')


# import os
#
# # dirs = [r'Work\F1', r'Work\F2\F21']
# # for d in dirs:
# #     os.makedirs(d)
#
# # files = {
# #     'Work': ['w.txt'],
# #     r'Work\F1': ['f11.txt', 'f12.txt', 'f13.txt'],
# #     r'Work\F2\F21': ['f211.txt', 'f212.txt']
# # }
# #
# # for d, f in files.items():
# #     for file in f:
# #         file_path = os.path.join(d, file)
# #         open(file_path, 'w').close()
#
# print(os.path.exists(r'C:\Users\shevc\OneDrive\Documents\Python_code\Work\F2\F21'))


# 1
# f = open("text2.txt", "w")
# f.write("Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл;\n")
# f.close()
#
# f = open("text2.txt", "r")
# rl = f.readlines()
# f.close()
#
# pos1 = 1
# pos2 = 2
#
# rl1 = rl[pos1]
# rl[pos1] = rl[pos2]
# rl[pos2] = rl1
#
# f = open("text2.txt", "w")
# f.writelines(rl)
# f.close()


# 2

# import os
#
# directory = 'Work'

# for file in os.listdir(directory):
#     path = os.path.join(directory, file)
#     if os.path.isfile(path):
#         print(f"{file} file {os.path.getsize(path)} bytes")
#     elif os.path.isdir(path):
#         print(file, '- dir')


# ООП (свойства(переменные), методы(функции))

# class Point:
#     x = 1
#     y = 1
#
#     def set_coord(self, x, y):
#         self.x = x
#         self.y = y
#         print(self.__dict__)


# p1 = Point()  # экземпляр класса
# p1.x = 5
# p1.y = 24
# p1.set_coord(5, 24)
# print(p1.x)
# print(p1.y)
# print(p1.__dict__)
# print(id(p1))

# p2 = Point()
# p2.set_coord(10, 30)
# print(p2.x)
# print(p2.y)
# print(p2.__dict__)
# print(id(p2))

# class Human:
#     name = "name"
#     birthday = "00.00.0000"
#     phone = "00-00-00"
#     country = 'country'
#     city = 'city'
#     address = "street, house"
#
#     def print_info(self):
#         print(" Персональные данные ".center(40, '*'))
#         print(f'Имя: {self.name}\nДата рождения: {self.birthday}\nНомер телефона: {self.phone}\n'
#               f'Страна: {self.country}\nГород: {self.city}"\nДомашний адрес: {self.address} ')
#         print('=' * 40)
#
#     def input_info(self, first_name, birthday, phone, country, city, address):
#         self.name = first_name
#         self.birthday = birthday
#         self.phone = phone
#         self.country = country
#         self.city = city
#         self.address = address
#
#     def set_address(self, address):
#         self.address = address
#
#     def get_address(self):
#         return self.address
#
#     def set_name(self, name):
#         self.name = name
#
#     def get_name(self):
#         return self.name
#
#
# h1 = Human()
#
# h1.input_info("Юля", "23.05.1986", "45-46-98", "Россия", "Москва", "Чистопрудный бульвар, 1А")
#
# # h1.set_address("ул. Ленина, 56")
# # print(h1.get_address())
# #
# # h1.set_name("Аня")
# # print(h1.get_name())
#
# h1.print_info()
#
# h1.set_address("ул. Ленина, 56")
# print(h1.get_address())
#
# h1.set_name("Аня")
# print(h1.get_name())

# class Person:
#     skill = 10 # статическое свойство
#     count = 0
#
#     def __init__(self, name, surname): # инициализатор
#         self.name = name # динамическое свойство
#         self.surname = surname
#         Person.count += 1

# def __del__(self):
#     print("Удаление экземпляра", self)
#
# def print_info(self, name, surname):
#     self.name = name
#     self.surname = surname
#     print("Данные сотрудника:", self.name, self.surname)
#
# def add_skill(self, k):
#     self.skill += k
#     print("Квалификация сотрудника:", self.skill, end='\n\n')


# p1 = Person("Виктор", "Резник")
# print(p1.count)
# # p2 = Person("Анна", "Долгих")
#
# print(Person.count)


# class Robot:
#     k = 0
#
#     def __init__(self, name):
#         self.name = name
#         print("Инициализация робота:", self.name)
#         Robot.k += 1
#
#     def __del__(self):
#         print(self.name, "выключается")
#
#         Robot.k -= 1
#
#         if Robot.k == 0:
#             print(self.name, "был последним")
#         else:
#             print("Работающих роботов осталось", Robot.k)
#
#     def say_hi(self):
#         print("Приветствую! Меня зовут:", self.name)
#
#
# droid1 = Robot('R2-D2')
# droid1.say_hi()
# print("Численность роботов:", Robot.k)
#
# droid2 = Robot('C-3PO')
# droid2.say_hi()
# print("Численность роботов:", Robot.k)
#
# droid3 = Robot('HP-2PO')
# droid3.say_hi()
# print("Численность роботов:", Robot.k)
# print("\nЗдесь роботы могут проделать какую-то работу\n")
#
# print("Роботы закончили свою работу. Давайте их выключим")
# del droid1
# del droid2
# del droid3
#
# print("Численность роботов:", Robot.k)


# 1
# class Car:
#     def __init__(self, model_name, year, company, power, color, price):
#         self.model_name = model_name
#         self.year = year
#         self.company = company
#         self.power = power
#         self.color = color
#         self.price = price
#
#     def print_info(self):
#         print(" Данные автомобиля ".center(40, '*'))
#         print(f'Название модели: {self.model_name}\nГода выпуска: {self.year}\nПроизводитель: {self.company}\n'
#               f'Мощность двигателя: {self.power} л.с.\nЦвет машины: {self.color}\nЦена: {self.price}')
#         print("=" * 40)
#
#
# p1 = Car('Х7 М50i', '2021', 'BMW', '530', 'white', '10790000')
# p1.print_info()


# 17/2/2024

# class Point:
#     __slots__ = ('__x', '__y')
#     def __init__(self, x, y):
#         self.__x = self.__y = 0
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
#
#     def __check_value(c):
#         if isinstance(c, int) or isinstance(c, float):
#             return True
#         return False
#
#     def get_cord(self):
#         return self.__x, self.__y
#
#     def set_cord(self, x, y):
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
#         else:
#             print("Координаты должны быть числами")
#
#     def get_x(self):
#         return self.__x
#
#     def get_y(self):
#         return self.__y
#
#     def set_x(self, x):
#         if Point.__check_value(x):
#             self.__x = x
#         else:
#             print("Координата", x, "должна быть числом")
#
#     def set_y(self, y):
#
#         if Point.__check_value(y):
#             self.__x = y
#         else:
#             print("Координата", y, "должна быть числом")
#
#
# p1 = Point(5, 10)
# p1.set_x(20.6)
# p1.set_y("aaa")
# # print(p1.get_cord())
# # p1.set_cord("6", 7)
# # print(p1.__x, p1.__y)
# # p1.x = 100
# # p1.y = 'abc'
# # print(p1.x, p1.y)
# print(p1.get_x())
# print(p1.get_y())
# print(p1.__dict__)

# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __get_x(self):
#         return self.__x
#
#     def __get_y(self):
#         return self.__y
#
#     def __set_x(self, x):
#         self.__x = x
#
#     def __set_y(self, y):
#         self.__y = y
#
#     x = property(__get_x, __set_x)
#
#
# p1 = Point(5, 10)
# p1.x = 100
# print(p1.__dict__)

# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __get_x(self):
#         return self.__x
#
#     def __get_y(self):
#         return self.__y
#
#     def __set_x(self, x):
#         self.__x = x
#
#     def __set_y(self, y):
#         self.__y = y
#
#     def __del_x(self):
#         print("Удаление свойства")
#     x = property(__get_x, __set_x)
#
#
# p1 = Point(5, 10)
# p1.x = 100
# print(p1.__dict__)


# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     @property
#     def x(self):
#         return self.__x
#
#     @x.setter
#     def x(self, x):
#         if not isinstance(x, (int, float)):
#             raise TypeError("Устанавливаемое значение должно быть числом")
#         self.__x = x
#
#     @x.deleter
#     def x(self):
#         print("Удаление свойства")
#         del self.__x
#
#     def __get_y(self):
#         return self.__y
#
#     def __set_y(self, y):
#         self.__y = y
#
#
# p1 = Point(5, 10)
# p1.x = 100
# print(p1.x)


# class KgToPounds:
#     def __init__(self, kg):
#         self.__kg = kg
#
#     @property
#     def kg(self):
#         return self.__kg
#
#     @kg.setter
#     def kg(self, new_kg):
#         if isinstance(new_kg, (int, float)):
#             self.__kg = new_kg
#         else:
#             print("Килограммы задаются только числами")
#
#     def to_pounds(self):
#         return self.__kg * 2.205
#
#     def print_data(self):
#         print(self.kg, "кг => ", end='')
#         print(self.to_pounds(), "фунтов")
#
#
# weight = KgToPounds(12)
# weight.print_data()


# class Point:
#     __count = 0
#
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#         Point.__count += 1
#
#     @staticmethod
#     def get_count():
#         return Point.__count
#
#
# p1 = Point()
# p2 = Point()
# p3 = Point()
#
# print(Point.get_count())


# class Change:
#     @staticmethod
#     def inc(x):
#         return x + 1
#
#     @staticmethod
#     def dex(x):
#         return x - 1
#
#
# print(Change.inc(10), Change.dex(10))


# class Tools:
#     @staticmethod
#     def maximum(my_list):
#         return max(my_list)
#
#     @staticmethod
#     def minimum(my_list):
#         return min(my_list)
#
#     @staticmethod
#     def middle(my_list):
#         return sum(my_list) / len(my_list)  # среднее арифметическое
#
#     # @staticmethod
#     # def factorial(number):
#     #     if number == 1:
#     #         return 1
#     #     else:
#     #         return Tools.factorial(number - 1) * number
#     @staticmethod
#     def factorial(number):
#         fact = 1
#         for i in range(number):
#             fact *= i
#         return fact
#
#
# print(f'Максимальное число: {Tools.maximum([3, 5, 7, 9])}')
# print(f'Минимум число: {Tools.minimum([3, 5, 7, 9])}')
# print(f'Среднее арифметическое: {Tools.middle([3, 5, 7, 9])}')
# print(f'Факториал числа {5}: {Tools.factorial(5)}')

# from math import sqrt
#
#
# class Square:
#     count = 0
#
#     @staticmethod
#     def square_triangle1(a, b, c):
#         Square.count += 1
#         p = (a + b + c) / 2
#         return sqrt(p * (p - a) * (p - b) * (p - c))
#
#     @staticmethod
#     def square_triangle2(a, b):
#         Square.count += 1
#         return 0.5 * a * b
#
#     @staticmethod
#     def square_area(a):
#         Square.count += 1
#         return a * a
#
#     @staticmethod
#     def square_rectangle(a, b):
#         Square.count += 1
#         return a * b
#
#     @staticmethod
#     def get_count():
#         return Square.count
#
#
# print('Площадь треугольника по формуле Герона:', Square.square_triangle1(3, 4, 5))
# print('Площадь треугольника через основание и высоту:', Square.square_triangle2(6, 7))
# print('Площадь квадрата:', Square.square_area(7))
# print('Площадь прямоугольника:', Square.square_rectangle(2, 6))
# print('Количество подсчетов площади:', Square.get_count())


# 1
# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#
#     def print_info(self):
#         print(f'Длина прямоугольника: {self.length}')
#         print(f'Ширина прямоугольника: {self.width}')
#
#     def square(self):
#         print(f'Площадь прямоугольника: {self.length * self.width}')
#
#     def perimeter(self):
#         print(f'Периметр прямоугольника: {self.length * 2 + self.width * 2}')
#
#     def diagonal(self):
#         print(f'Диагональ прямоугольника: {round((self.length ** 2 + self.width ** 2) ** 0.5, 2)}')
#
#     def draw_rectangle(self):
#         for i in range(self.length):
#             print('*' * self.width)
#
#
# p1 = Rectangle(3, 9)
# p1.print_info()
# p1.square()
# p1.perimeter()
# p1.diagonal()
# p1.draw_rectangle()


# 2
# class Person:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#
#     @property
#     def name(self):
#         return self.__name
#
#     @property
#     def age(self):
#         return self.__age
#
#     @name.setter
#     def name(self, new_name):
#         self.__name = new_name
#
#     @age.setter
#     def age(self, new_age):
#         self.__age = new_age
#
#     @name.deleter
#     def name(self):
#         del self.__name
#
#     @age.deleter
#     def age(self):
#         del self.__age
#
#
# p1 = Person('Irina', '26')
# print(p1.__dict__)
# p1.name = 'Igor'
# p1.age = '31'
# print(p1.name)
# print(p1.age)
# del p1.name
# print(p1.__dict__)

# 3 (1)
# class Account:
#     rate_usd = 0.013
#     rate_eur = 0.011
#     suffix = 'RUB'
#     suffix_usd = 'USD'
#     suffix_eur = 'EUR'
#
#     def __init__(self, surname, num, percent, value=0):
#         self.surname = surname
#         self.num = num
#         self.percent = percent
#         self.value = value
#         print(f"Счет #{self.num} принадлежащий {self.surname} был открыт.")
#         print("*" * 50)
#
#     def __del__(self):
#         print("*" * 50)
#         print(f"Счет #{self.num} принадлежащий {self.surname} был закрыт.")
#
#     @property
#     def value(self):
#         return self.__value
#
#     @value.setter
#     def value(self, v):
#         self.__verify_value(v)
#         self.__value = v
#
#     @staticmethod
#     def __verify_value(value):
#         if value < 0:
#             if not isinstance(value, (int, float)):
#                 raise TypeError("Баланс долен быть числом")
#             if value < 0:
#                 raise ValueError("Баланс не может быть меньше нуля")
#
#     @classmethod
#     def set_usd_rate(cls, rate):
#         cls.rate_usd = rate
#
#     @classmethod
#     def set_eur_rate(cls, rate):
#         cls.rate_eur = rate
#
#     @staticmethod
#     def convert(value, rate):
#         return value * rate
#
#     def add_money(self, val):
#         self.value += val
#         print(f"{val} {Account.suffix} было успешно добавлено!")
#         self.print_balance()
#
#     def convert_to_usd(self):
#         usd_val = Account.convert(self.value, Account.rate_usd)
#         print(f"Состояние счета: {usd_val} {Account.suffix_usd}")
#
#     def convert_to_eur(self):
#         uer_val = Account.convert(self.value, Account.rate_eur)
#         print(f"Состояние счёта: {uer_val} {Account.suffix_eur}")
#
#     def print_balance(self):
#         print(f"Текущий баланс {self.value} {Account.suffix}")
#
#     def edit_owner(self, surname):
#         self.surname = surname
#
#     def add_percent(self):
#         self.value += self.value * self.percent
#         print("Проценты были успешно начислены")
#         self.print_balance()
#
#     def withdraw_money(self, val):
#         if val > self.value:
#             print(f"К сожалению у вас нет {val} {Account.suffix}")
#         else:
#             self.value -= val
#             print(f"{val} {Account.suffix} было успешно снять!")
#         self.print_balance()
#
#     def print_info(self):
#         print('Информация о счете:')
#         print("-" * 20)
#         print(f"#{self.num}")
#         print(f"Владелец: {self.surname}")
#         self.print_balance()
#         print(f"Проценты: {self.percent:.0%}")
#         print("-" * 20)
#
#
# acc = Account("Долгих", "12345", 0.03, 1000)
# acc.print_info()
# acc.convert_to_usd()
# acc.convert_to_eur()
# Account.set_usd_rate(2)
# Account.set_eur_rate(3)
# print()
# acc.convert_to_usd()
# acc.convert_to_eur()
# acc.edit_owner("Дюма")
# acc.print_info()
# print()
# acc.add_percent()
# print()
# acc.withdraw_money(100)
# print()
# acc.withdraw_money(3000)
# print()
# acc.add_money(5000)
# print()
# acc.withdraw_money(3000)


# 3(2)
# class Account:
#     rate_usd = 0.013
#     rate_eur = 0.011
#     suffix = 'RUB'
#     suffix_usd = 'USD'
#     suffix_eur = 'EUR'
#
#     def __init__(self, surname, num, percent, value=0):
#         self.surname = surname
#         self.num = num
#         print(f"Счет #{self.num} принадлежащий {self.surname} был открыт.")
#         print("*" * 50)
#         self.percent = percent
#         self.value = value
#         self.set_value(value)
#
#     def __del__(self):
#         print("*" * 50)
#         print(f"Счет #{self.num} принадлежащий {self.surname} был закрыт.")
#
#     def get_value(self):
#         return self.value
#
#     def set_value(self, v):
#         self.__verify_value(v)
#         self.value = v
#
#     @staticmethod
#     def __verify_value(value):
#         if value < 0:
#             if not isinstance(value, (int, float)):
#                 raise TypeError("Баланс долен быть числом")
#             if value < 0:
#                 raise ValueError("Баланс не может быть меньше нуля")
#
#     @classmethod
#     def set_usd_rate(cls, rate):
#         cls.rate_usd = rate
#
#     @classmethod
#     def set_eur_rate(cls, rate):
#         cls.rate_eur = rate
#
#     @staticmethod
#     def convert(value, rate):
#         return value * rate
#
#     def add_money(self, val):
#         self.value += val
#         print(f"{val} {Account.suffix} было успешно добавлено!")
#         self.print_balance()
#
#     def convert_to_usd(self):
#         usd_val = Account.convert(self.value, Account.rate_usd)
#         print(f"Состояние счета: {usd_val} {Account.suffix_usd}")
#
#     def convert_to_eur(self):
#         uer_val = Account.convert(self.value, Account.rate_eur)
#         print(f"Состояние счёта: {uer_val} {Account.suffix_eur}")
#
#     def print_balance(self):
#         print(f"Текущий баланс {self.value} {Account.suffix}")
#
#     def edit_owner(self, surname):
#         self.surname = surname
#
#     def add_percent(self):
#         self.value += self.value * self.percent
#         print("Проценты были успешно начислены")
#         self.print_balance()
#
#     def withdraw_money(self, val):
#         if val > self.value:
#             print(f"К сожалению у вас нет {val} {Account.suffix}")
#         else:
#             self.value -= val
#             print(f"{val} {Account.suffix} было успешно снять!")
#         self.print_balance()
#
#     def print_info(self):
#         print('Информация о счете:')
#         print("-" * 20)
#         print(f"#{self.num}")
#         print(f"Владелец: {self.surname}")
#         self.print_balance()
#         print(f"Проценты: {self.percent:.0%}")
#         print("-" * 20)
#
#
# acc = Account("Долгих", "12345", 0.03, -1000)
# acc.print_info()
# acc.convert_to_usd()
# acc.convert_to_eur()
# Account.set_usd_rate(2)
# Account.set_eur_rate(3)
# print()
# acc.convert_to_usd()
# acc.convert_to_eur()
# acc.edit_owner("Дюма")
# acc.print_info()
# print()
# acc.add_percent()
# print()
# acc.withdraw_money(100)
# print()
# acc.withdraw_money(3000)
# print()
# acc.add_money(5000)
# print()
# acc.withdraw_money(3000)


# class KgToPounds:
#     def __init__(self, kg):
#         self.__kg = kg
#
#     @property
#     def kg(self):
#         return self.__kg
#
#     @kg.setter
#     def kg(self, new_kg):
#         if isinstance(new_kg, (int, float)):
#             self.__kg = new_kg
#         else:
#             print("Килограммы задаются только числами")
#
#     def to_pounds(self):
#         return self.__kg * 2.205
#
#     def print_data(self):
#         print(self.kg, "кг => ", end="")
#         print(self.to_pounds(), "фунтов")
#
#
# weight = KgToPounds(12)
# weight.print_data()
# weight.kg = 41
# weight.print_data()
# weight.kg = "десять"


# class Date:
#     def __init__(self, day, month, year):
#         self.day = day
#         self.month = month
#         self.year = year
#
#     @classmethod
#     def from_string(cls, date_as_string):
#         day, month, year = map(int, date_as_string.split("."))
#         date1 = cls(day, month, year)  # date1 = Date(23, 10, 2024)
#         return date1
#
#     def string_to_db(self):
#         return f'{self.year}-{self.month}-{self.day}'
#
#     @staticmethod
#     def is_date_valid(date_as_string):
#         if date_as_string.count('.') == 2:
#             day, month, year = map(int, date_as_string.split("."))
#             return day <= 31 and month <= 12 and year <= 3999
#
#
# dates = [
#     '30.12.2023',
#     '30-12-2020',
#     '01.01.2024',
#     '12.31.2020'
# ]
# for string_date in dates:
#     if Date.is_date_valid(string_date):
#         date = Date.from_string(string_date)
#         print(date.string_to_db())
#     else:
#         print('Неправильная дата или формат строки с датой')
# date2 = Date.from_string("23.10.2024")
# print(date2.string_to_db())

# string_date = "23.10.2024"
# day, month, year = map(int, string_date.split("."))
# print(day, month, year)
#
# date = Date(day, month, year)
# print(date.string_to_db())


# class Account:
#     rate_usd = 0.013
#     rate_eur = 0.011
#     suffix = 'RUB'
#     suffix_usd = 'USD'
#     suffix_eur = 'EUR'
#
#     def __init__(self, surname, num, percent, value=0):
#         self.surname = surname
#         self.num = num
#         self.percent = percent
#         self.value = value
#         print(f"Счет #{self.num} принадлежащий {self.surname} был открыт.")
#         print("*" * 50)
#
#     def __del__(self):
#         print("*" * 50)
#         print(f"Счет #{self.num} принадлежащий {self.surname} был закрыт.")
#
#     @classmethod
#     def set_usd_rate(cls, rate):
#         cls.rate_usd = rate
#
#     @classmethod
#     def set_eur_rate(cls, rate):
#         cls.rate_eur = rate
#
#     @staticmethod
#     def convert(value, rate):
#         return value * rate
#
#     def add_money(self, val):
#         self.value += val
#         print(f"{val} {Account.suffix} было успешно добавлено!")
#         self.print_balance()
#
#     def convert_to_usd(self):
#         usd_val = Account.convert(self.value, Account.rate_usd)
#         print(f"Состояние счета: {usd_val} {Account.suffix_usd}")
#
#     def convert_to_eur(self):
#         uer_val = Account.convert(self.value, Account.rate_eur)
#         print(f"Состояние счёта: {uer_val} {Account.suffix_eur}")
#
#     def print_balance(self):
#         print(f"Текущий баланс {self.value} {Account.suffix}")
#
#     def edit_owner(self, surname):
#         self.surname = surname
#
#     def add_percent(self):
#         self.value += self.value * self.percent
#         print("Проценты были успешно начислены")
#         self.print_balance()
#
#     def withdraw_money(self, val):
#         if val > self.value:
#             print(f"К сожалению у вас нет {val} {Account.suffix}")
#         else:
#             self.value -= val
#             print(f"{val} {Account.suffix} было успешно снять!")
#         self.print_balance()
#
#     def print_info(self):
#         print('Информация о счете:')
#         print("-" * 20)
#         print(f"#{self.num}")
#         print(f"Владелец: {self.surname}")
#         self.print_balance()
#         print(f"Проценты: {self.percent:.0%}")
#         print("-" * 20)
#
#
# acc = Account("Долгих", "12345", 0.03, 1000)
# acc.print_info()
# acc.convert_to_usd()
# acc.convert_to_eur()
# Account.set_usd_rate(2)
# Account.set_eur_rate(3)
# print()
# acc.convert_to_usd()
# acc.convert_to_eur()
# acc.edit_owner("Дюма")
# acc.print_info()
# print()
# acc.add_percent()
# print()
# acc.withdraw_money(100)
# print()
# acc.withdraw_money(3000)
# print()
# acc.add_money(5000)
# print()
# acc.withdraw_money(3000)


# class Point:
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#
#
# print(issubclass(Point, object))
# print(issubclass(Point, int))


# class Point:
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):  # строковое представление объекта
#         return f"({self.__x}, {self.__y})"
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = 'red', width=1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self.__width = width
#         print("Инициализатор базового класса Prop")
#
#     def get_width(self):
#         return self.__width
#
#
# class Line(Prop):
#     def __init__(self, *args):
#         super().__init__(*args)
#         # Prop.__init__(self, *args)
#         print("Переопределенный инициализатор Line")
#
#     def draw_line(self):
#         print(f'Рисование линии: {self._sp}, {self._ep}, {self._color}, {self.get_width()}')
#
#
# class Rect(Prop):
#
#     def draw_rect(self):
#         print(f'Рисование прямоугольника: {self._sp}, {self._ep}, {self._color}, {self.get_width()}')
#
#
# line = Line(Point(1, 2), Point(10, 20), "yellow", 5)
# line.draw_line()
# rect = Rect(Point(30, 40), Point(70, 80))
# rect.draw_rect()

# DRY (Don't Repeat Yourself) - не повторяйся


# class Figure:
#     def __init__(self, color):
#         self.__color = color
#
#     @property
#     def color(self):
#         return self.__color
#
#     @color.setter
#     def color(self, c):
#         self.__color = c
#
#
# class Rectangle(Figure):
#     def __init__(self, width, height, color):
#         self.width = width
#         self.height = height
#         super().__init__(color)
#
#     @property
#     def width(self):
#         return self.__width
#
#     @width.setter
#     def width(self, w):
#         if w > 0:
#             self.__width = w
#         else:
#             raise ValueError('Некорректное значение ширины')
#
#     @property
#     def height(self):
#         return self.__height
#
#     @height.setter
#     def height(self, h):
#         if h > 0:
#             self.__height = h
#         else:
#             raise ValueError('Некорректное значение высоты')
#
#     def area(self):
#         print(f'Площадь {self.color} прямоугольника = ', end='')
#         return self.__width * self.__height
#
#
# rect = Rectangle(10, -20, "green")
# print(rect.area())


# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):  # строковое представление объекта
#         return f"({self.__x}, {self.__y})"
#
#     def is_digit(self):
#         if isinstance(self.__x, (int, float)) and isinstance(self.__y, (int, float)):
#             return True
#         else:
#             return False
#
#     def is_int(self):
#         if isinstance(self.__x, int) and isinstance(self.__y, int):
#             return True
#         else:
#             return False
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = 'red', width=1) -> None:
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#     def set_coord(self, sp, ep):
#         if sp.is_digit() and ep.is_digit():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print("Координаты должны быть числами")
#
#
# class Line(Prop):
#
#     def set_coord(self, sp, ep):
#         if sp.is_int() and ep.is_int():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print("Координаты должны быть целыми числами")
#
#     def draw_line(self):
#         print(f'Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}')
#
#
# class Rect(Prop):
#
#     def draw_rect(self):
#         print(f'Рисование прямоугольника: {self._sp}, {self._ep}, {self._color}, {self._width}')
#
#
# line = Line(Point(1, 2), Point(10, 20), "yellow", 5)
# line.set_coord(Point(15.5, 45), Point(100, 200))
# line.draw_line()
#
# rect = Rect(Point(55.5, 45.6), Point(70, 80))
# rect.draw_rect()


# class Rect:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def show_rect(self):
#         print(f"Прямоугольник:\nШирина: {self.width}\nВысота: {self.height}")
#
#
# class RectFon(Rect):
#     def __init__(self, width, height, background):
#         self.fon = background
#         super().__init__(width, height)
#
#     def show_rect(self):
#         super().show_rect()
#         print("Фон:", self.fon)
#
#
# class RectBorder(Rect):
#     def __init__(self, width, height, px, type1, color):
#         self.px = px
#         self.type1 = type1
#         self.color = color
#         super().__init__(width, height)
#
#     def show_rect(self):
#         super().show_rect()
#         print(f"Толщина рамки: {self.px},  Тип рамки: {self.type1}, Цвет рамки: {self.color}")
#
#
# shape1 = RectFon(400, 200, "yellow")
# shape1.show_rect()
#
# shape2 = RectBorder(680, 300, "1px", 'solid', 'red')
# shape2.show_rect()

# class Vector(list):
#     def __init__(self, lst):
#
#         self.lst = lst
#
#     def __str__(self):
#         return ' '.join(map(str, self.lst))
#
#
# v = Vector([1, 2, 3])
# print(sum(v))
# print(v)
# print(type(v))


# Перегрузка методов
# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
#     def is_digit(self):
#         if isinstance(self.__x, (int, float)) and isinstance(self.__y, (int, float)):
#             return True
#         return False
#
#     def is_int(self):
#         if isinstance(self.__x, int) and isinstance(self.__y, int):
#             return True
#         return False
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1) -> None:
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#     def set_coord(self, sp, ep):
#         if sp.is_digit() and ep.is_digit():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print("Координаты должны быть числами")
#
#
# class Line(Prop):
#     def set_coord(self, sp=None, ep=None):
#         if ep is None:
#             if sp.is_int():
#                 self._sp = sp
#             else:
#                 print("Координата sp должна быть целочисленным значением")
#         elif sp is None:
#             if ep.is_int():
#                 self._ep = ep
#             else:
#                 print("Координата ep должна быть целочисленным значением")
#         else:
#             if sp.is_int() and ep.is_int():
#                 self._sp = sp
#                 self._ep = ep
#             else:
#                 print("Координаты должны быть целочисленными значениями")
#
#     def draw_line(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# line = Line(Point(1, 2), Point(10, 20), "yellow", 5)
# line.draw_line()
# line.set_coord(ep=Point(15, 45))
# line.draw_line()


# Абстрактные методы
# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
#     def is_digit(self):
#         if isinstance(self.__x, (int, float)) and isinstance(self.__y, (int, float)):
#             return True
#         return False
#
#     def is_int(self):
#         if isinstance(self.__x, int) and isinstance(self.__y, int):
#             return True
#         return False
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1) -> None:
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#
# class Line(Prop):
#     def draw(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# class Rect(Prop):
#     def draw(self):


# Абстрактные классы

# from abc import ABC, abstractmethod
#
#
# class Chess(ABC):  # Абстрактный класс
#     def draw(self):
#         print("Нарисовал шахматную фигуру")
#
#     @abstractmethod
#     def move(self):
#         print("Метод move() в базовом классе")
#
#
# class Queen(Chess):
#     def move(self):
#         super().move()
#         print("Ферзь перемещен на e2e4")
#
#
# # q = Chess()
# q = Queen()
# q.draw()
# q.move()

# from abc import ABC, abstractmethod
#
#
# class Currency(ABC):
#     def __init__(self, value):
#         self.value = value
#
#     @abstractmethod
#     def convert_to_rub(self):
#         pass
#
#     @abstractmethod
#     def print_value(self):
#         print(self.value, end=' ')
#
#     def show(self):
#         print(f' = {self.convert_to_rub():.2f} RUB')
#
#
# class Dollar(Currency):
#     rate_to_rub = 74.16
#     suffix = 'USD'
#
#     def convert_to_rub(self):
#         return self.value * Dollar.rate_to_rub
#
#     def print_value(self):
#         super().print_value()
#         print(Dollar.suffix, end=' ')
#
#
# class Euro(Currency):
#     rate_to_rub = 90.14
#     suffix = 'EUR'
#
#     def convert_to_rub(self):
#         return self.value * Euro.rate_to_rub
#
#     def print_value(self):
#         super().print_value()
#         print(Euro.suffix, end=' ')
#
#
# d = [Dollar(5), Dollar(10), Dollar(50), Dollar(100)]
# e = [Euro(5), Euro(10), Euro(50), Euro(100)]
# d += e
# for elem in d:
#     elem.print_value()
#     # print(f' = {elem.convert_to_rub():.2f} RUB')
#     elem.show()


# Интерфейсы

# from abc import ABC, abstractmethod
#
#
# class Father(ABC):
#     @abstractmethod
#     def display1(self):
#         pass
#
#     @abstractmethod
#     def display2(self):
#         pass
#
#
# class Child(Father):
#     def display1(self):
#         print("Child")
#
#
# class GrandChild(Child):
#     def display2(self):
#         print("GrandChild")
#
#
# gc = GrandChild()
# gc.display2()
# gc.display1()


# class MyOuter:
#     age = 18
#
#     def __init__(self, name):
#         self.name = name
#
#     @staticmethod
#     def static_method():
#         print("Статический метод")
#
#     def outer_method(self):
#         print("Метод в наружном классе")
#
#     class MyInner:
#         def __init__(self, inner_name, obj):
#             self.inner_name = inner_name
#             self.obj = obj
#
#         def inner_method(self):
#             print("Вложенный класс", MyOuter.age, self.obj.name)
#             MyOuter.static_method()
#             self.obj.outer_method()
#
#
# out = MyOuter('внешний')
# inner = out.MyInner('внутренний', out)
# print(inner.inner_name)
# inner.inner_method()


# class Color:
#     def __init__(self):
#         self.name = 'Green'
#         self.lg = self.LightGreen()
#
#     def show(self):
#         print("Name:", self.name)
#
#     class LightGreen:
#         def __init__(self):
#             self.name = 'Light Green'
#
#         def display(self):
#             print("Name:", self.name)
#
#
# outer = Color()
# outer.show()
# # outer.lg.display()
# g = outer.lg
# g.display()


# class Employee:
#     def __init__(self):
#         self.name = "Employee"
#         self.intern = self.Intern()
#         self.head = self.Head()
#
#     def show(self):
#         print("Name:", self.name)
#
#     class Intern:
#         def __init__(self):
#             self.name = "Smith"
#
#         def display(self):
#             print("Name:", self.name)
#
#     class Head:
#
#         def __init__(self):
#             self.name = "Alba"
#
#         def display(self):
#             print("Name:", self.name)
#
#
# outer = Employee()
# outer.show()
# d1 = outer.intern
# d2 = outer.head
# d1.display()
# d2.display()


# class Student:
#     def __init__(self, name):
#         self.name = name
#
#     def print_info(self):
#         print(f'{self.name} => {self.Notebook().model}, {self.Notebook().cpu}, {self.Notebook().ram}')
#
#     class Notebook:
#         def __init__(self):
#             self.model = 'HP'
#             self.cpu = 'i7'
#             self.ram = '16'
#
#
# student1 = Student('Roman')
# notebook1 = student1.Notebook()
# student1.print_info()
# student1.name = 'Vladimir'
# student1.print_info()

from math import pi


class Table:
    def __init__(self, width=None, length=None, radius=None):
        if radius is None:
            self._width = width
            self._length = length
        else:
            self._radius = radius


class RectangularTables(Table):
    def square(self):
        print('Площадь прямоугольного стола:', self._width * self._length)


class CircleTables(Table):
    def square(self):
        print('Площадь круглого стола:', round(pi * self._radius ** 2, 2))


rt = RectangularTables(20, 10)
rt.square()

ct = CircleTables(radius=20)
ct.square()
