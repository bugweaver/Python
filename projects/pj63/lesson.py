# Упаковка данных

# import pickle

# file_name = "basket.txt"
#
# shop_list = {
#     "фрукты": ["яблоки", "манго"],
#     "овощи": ['морковь'],
#     "бюджет": 1000
# }
#
# with open(file_name, "wb") as fh:
#     pickle.dump(shop_list, fh)
#
# with open(file_name, 'rb') as fh:
#     shop_list_2 = pickle.load(fh)
#
# print(shop_list_2)


# class Test:
#     num = 35
#     st = "привет"
#     lst = [1, 2, 3]
#     tpl = (22, 34)
#
#     def __str__(self):
#         return f'Число: {Test.num}\nСтрока: {Test.st}\nСписок: {Test.lst}\nКортеж: {Test.tpl}'
#
#
# obj = Test()
# obj1 = pickle.dumps(obj)
# print(f"Сериализация в строку: \n{obj1}")
#
# obj2 = pickle.loads(obj1)
# print(f'Десериализация из строки: \n{obj2}')

# class Test2:
#     def __init__(self):
#         self.a = 35
#         self.b = "test"
#         self.c = lambda x: x * x
#
#     def __str__(self):
#         return f'{self.a} {self.b} {self.c(2)}'
#
#     def __getstate__(self):
#         attr = self.__dict__.copy()
#         del attr['c']
#         return attr
#
#     def __setstate__(self, state):
#         self.__dict__ = state
#         self.c = lambda x: x * x
#
#
# item1 = Test2()
# print(item1)
# item2 = pickle.dumps(item1)
# print(item2)
# item3 = pickle.loads(item2)
# print(item3.__dict__)
# print(item3)


import json


# data = {
#     'name': 'Olga',
#     'age': 35,
#     20: None,
#     'hobbies': ('running', 'singing'),
#     'children': [
#         {
#             'first_name': "Alice",
#             True: 1
#         }
#     ]
# }

# filename = "data_file.json"
# with open(filename, 'w') as fw:
#     json.dump(data, fw, indent=4)
#
# with open(filename, 'r') as fw:
#     data1 = json.load(fw)
#
# print(data1)

# json_string = json.dumps(data)
# print(json_string)
# data1 = json.loads(json_string)
# print(data1['hobbies'])
# print(type(data1))

# x = {
#     "name": "Виктор"
# }
# print(json.dumps(x))
# print(json.loads(json.dumps(x)))
# print(json.dumps(x, ensure_ascii=False))


# import json
# from random import choice
#
#
# def gen_person():
#     name = ''
#     tel = ''
#
#     letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'e']
#     num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
#
#     while len(name) != 7:
#         name += choice(letter)
#
#     while len(tel) != 10:
#         tel += choice(num)
#
#     person = {
#         'name': name,
#         'tel': tel
#     }
#     return person
#
#
# def write_json(person_dict):
#     try:
#         data = json.load(open('person.json'))
#     except FileExistsError:
#         data = []
#
#     data.append(person_dict)
#     with open('person.json', 'w') as f:
#         json.dump(data, f, indent=2)
#
#
# for i in range(5):
#     write_json(gen_person())


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __str__(self):
        a = ','.join(map(str, self.marks))
        return f'Студент: {self.name}: {a}'


st1 = Student("Bodnya", [5, 4, 3, 4, 5, 3])
print(st1)
