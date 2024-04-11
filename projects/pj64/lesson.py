# import json
#
#
# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#
#     def __str__(self):
#         a = ','.join(map(str, self.marks))
#         return f'Студент: {self.name}: {a}'
#
#     def add_mark(self, mark):
#         self.marks.append(mark)
#
#     def delete_mark(self, index):
#         self.marks.pop(index)
#
#     def edit_mark(self, index, new_mark):
#         self.marks[index] = new_mark
#
#     def average_mark(self):
#         return round(sum(self.marks) / len(self.marks), 2)
#
#     def dump_to_json(self, filename):
#         data = {"name": self.name, "marks": self.marks}
#         with open(filename, "w") as f:
#             json.dump(data, f)
#
#     def load_from_file(self, filename):
#         with open(filename, "r") as f:
#             print(json.load(f))
#
#
# class Group:
#     def __init__(self, students, group):
#         self.students = students
#         self.group = group
#
#     def __str__(self):
#         a = '\n'.join(map(str, self.students))
#         return f'\nГруппа: {self.group}\n{a}'
#
#     def add_student(self, student):
#         self.students.append(student)
#
#     def remove_student(self, index):
#         return self.students.pop(index)
#
#     @staticmethod
#     def change_group(group_1, group_2, index):
#         tmp = group_1.remove_student(index)
#         group_2.add_student(tmp)
# #
# #
# st1 = Student("Bodnya", [5, 4, 3, 4, 5, 3])
# st1.dump_to_json("student1.json")
# st1.load_from_file("student1.json")
# st2 = Student("Nikolaenko", [2, 3, 5, 4, 2])
# st3 = Student("Birukov", [3, 5, 3, 2, 5, 4])
# sts1 = [st1, st2]
# group1 = Group(sts1, "ГК Python")
#
# group1.add_student(st3)
#
# group1.remove_student(1)
# print(group1)
# sts2 = [st2]
# group2 = Group(sts2, "ГК Web")
# print(group2)
# Group.change_group(group1, group2, 0)
# print(group1)
# print(group2)
# print(st1)
# st1.add_mark(4)
# print(st1)
# st1.delete_mark(2)
# print(st1)
# st1.edit_mark(4, 5)
# print(st1)
# print(st1.average_mark())

# import json
#
#
# class CountryCapital:
#     @staticmethod
#     def add_country(filename):
#         new_country = input("Введите название страны: ").lower()
#         new_capital = input("Введите название столице: ").lower()
#         try:
#             data = json.load(open(filename))
#         except FileNotFoundError:
#             data = {}
#         data[new_country] = new_capital
#
#         with open(filename, "w", encoding="utf-8") as f:
#             json.dump(data, f, indent=2)
#
#     @staticmethod
#     def load_from_file(filename):
#         with open(filename) as f:
#             print({k.capitalize(): v.capitalize() for k, v in json.load(f).items()})
#
#
# file = "list_capital.json"
# while True:
#     index = input("Выбор действия:\n1 - добавление данных\n2 - удаление данных\n3 - поиск данных\n"
#                   "4 - редактировать данных\n5 - просмотр данных\n6 - завершение работы"
#                   "\nВвод: ")
#
#     if index == "1":
#         CountryCapital.add_country(file)
#     elif index == "5":
#         CountryCapital.load_from_file(file)
#     elif index == "6":
#         break
#     else:
#         print("Введён некорректный номер")
