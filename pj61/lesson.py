# class Point3D:
#     RIGHT = 'Правый операнд должен быть типом Point3D'
#
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#
#     def __str__(self):
#         return f'{self.x}, {self.y}, {self.z} '
#
#     def __add__(self, other):
#         if not isinstance(other, Point3D):
#             raise ValueError(self.RIGHT)
#         else:
#             return Point3D(self.x + other.x, self.y + other.y, self.z + other.z)
#
#     def __eq__(self, other):
#         if not isinstance(other, Point3D):
#             raise ValueError(self.RIGHT)
#         else:
#             return self.x == other.x and self.y == other.y and self.z == other.z
#
#     def __getitem__(self, item):
#         if not isinstance(item, str):
#             raise ValueError('Ключ должен быть строкой')
#         elif item == 'x':
#             return self.x
#         elif item == 'y':
#             return self.y
#         elif item == 'z':
#             return self.z
#         else:
#             print("Неверный ключ")
#
#     def __setitem__(self, key, value):
#         if not isinstance(key, str):
#             raise ValueError('Ключ должен быть строкой')
#         if key == 'x':
#             self.x = value
#         elif key == 'y':
#             self.y = value
#         elif key == 'z':
#             self.z = value
#         else:
#             print("Неверный ключ")
#
#
# pt1 = Point3D(12, 15, 18)
# pt2 = Point3D(6, 3, 9)
# print("Координаты 1-й точки:", pt1)
# print("Координаты 2-й точки:", pt2)
# pt3 = pt1 + pt2
# print(f'Сложение координат: ({pt3})')
# print(f'Равенство координат: ({pt1 == pt2})')
#
# print(f'x1 ={pt1['x']}, x2 = {pt2['x']}')
# print(f'x1 ={pt1['y']}, x2 = {pt2['y']}')
# print(f'x1 ={pt1['z']}, x2 = {pt2['z']}\n')
#
# pt1['x'] = 20
#
# print(f'x1 ={pt1['x']}, x2 = {pt2['x']}')
# print(f'x1 ={pt1['y']}, x2 = {pt2['y']}')
# print(f'x1 ={pt1['z']}, x2 = {pt2['z']}\n')


# Функторы

# class Counter:
#     def __init__(self):
#         self.__count = 0
#
#     def __call__(self, *args, **kwargs):
#         self.__count += 1
#         print(self.__count)
#
#
# c1 = Counter()
# c1()
# c1()
# c1()
# c2 = Counter()
# c2()
# c2()
# c2()

# class StripChars:
#     def __init__(self, chars):
#         self.__chars = chars
#
#     def __call__(self, string):
#         if not isinstance(string, str):
#             raise ValueError("Аргумент должен быть строкой")
#         return string.strip(self.__chars)
#
#
# s1 = StripChars("?:!.; ")
# print(s1(" Hello World!!!!!"))
#
#
# def strip_chars(chars):
#     def wrap(string):
#         if not isinstance(string, str):
#             raise ValueError("Аргумент должен быть строкой")
#         return string.strip(chars)
#
#     return wrap
#
#
# s2 = strip_chars("?:!.; ")
# print(s2(" Hello World!!!!!"))

# class MyDecorator:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self):
#         print("Перед вызовом функции")
#         self.func()
#         print("После вызова функции")
#
#
# @MyDecorator
# def function():
#     print("Текст функции")
#
#
# function()


# class MyDecorator:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, x, y):
#         # print("Перед вызовом функции")
#         # res = self.func(x, y)
#         # print("После вызова функции")
#         return f'Перед вызовом функции\n{self.func(x, y)}\nПосле вызова функции'
#
#
# @MyDecorator
# def function(a, b):
#     return a * b
#
#
# print(function(2, 5))


# class Power:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, x, y):
#         return self.func(x, y) ** 2
#
#
# @Power
# def function(a, b):
#     return a * b
#
#
# print(function(2, 3))


# class MyDecorator:
#     def __init__(self, arg):
#         self.name = arg
#
#     def __call__(self, func):
#         def wrap(*args, **kwargs):
#
#             return f'Перед вызовом функции ({self.name})\n{func(*args, **kwargs)}\nПосле вызова функции'
#         return wrap
#
#
# @MyDecorator("два параметра")
# def function(a, b):
#     return a * b
#
#
# @MyDecorator("три параметра")
# def function1(a, b, c):
#     return a * b * c
#
#
# print(function(2, 5))
# print(function1(2, 5, 5))

# class Power:
#     def __init__(self, num):
#         self.num = num
#
#     def __call__(self, func):
#         def wrap(*args, **kwargs):
#             return f'Результат: {func(*args, **kwargs) ** self.num}\n'
#
#         return wrap
#
#
# @Power(3)
# def function(a, b):
#     return a * b
#
#
# print(function(2, 2))


# Декорирование метода

# def dec(fn):
#     def wrap(*args, **kwargs):
#         print("*" * 20)
#         fn(*args, **kwargs)
#         print("*" * 20)
#     return wrap
#
#
# class Person:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     @dec
#     def info(self):
#         print(f'{self.name} {self.surname}')
#
#
# p1 = Person("Виталий", "Карасев")
# p1.info()

# def decorator(cls):
#     class Wrapper(cls):
#
#         def doubler(self, value):
#             return value * 2
#
#     return Wrapper
#
#
# @decorator
# class ActualClass:
#     def __init__(self):
#         print("Инициализатор ActualClass")
#
#     def quad(self, value):
#         return value * 4
#
#
# obj = ActualClass()
# print(obj.quad(4))
# print(obj.doubler(4))


# Дескрипторы(__get__, __set__, __delete__, __set_name__)

# class ValidString:
#     def __set_name__(self, owner, name):
#         self.__name = name
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.__name]
#
#     def __set__(self, instance, value):
#         if not isinstance(value, str):
#             raise ValueError(f"{self.__name} должно быть строкой")
#         instance.__dict__[self.__name] = value
#
#
# class Person:
#     name = ValidString()
#     surname = ValidString()
#
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#
# p = Person("Ivan", "Petrov")
# # p.surname = "5"
# print(p.name)
# print(p.surname)
# print(p.__dict__)
