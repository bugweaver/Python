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
#     def dump_to_json(self):
#         data = {"name": self.name, "marks": self.marks}
#         with open(self.get_file_name(), "w") as f:
#             json.dump(data, f)
#
#     def load_from_file(self):
#         with open(self.get_file_name(), "r") as f:
#             print(json.load(f))
#
#     def get_file_name(self):
#         return self.name + '.json'
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
#         group_2.add_student(group_1.remove_student(index))
#
#     def dump_to_json(self):
#         data = {
#             self.group: {
#                 'students': [
#                     {student.name: student.marks} for student in self.students
#                 ]
#             }
#         }
#         with open(self.get_file_name(), 'w') as file:
#             json.dump(data, file, indent=2)
#         return data
#
#     @staticmethod
#     def get_file_name():
#         return 'all_groups.json'
#
#     def load_from_file(self):
#         with open(self.get_file_name(), 'r') as f:
#             print(json.load(f))
#
#     # @staticmethod
#     # def add_group(group):
#     #     try:
#     #         data = json.load(open(Group.get_file_name()))
#     #     except FileNotFoundError:
#     #         data = {}
#     #
#     #     data.update(Group.dump_to_json(group))
#     #     with open(Group.get_file_name(), 'w') as file:
#     #         json.dump(data, file, indent=2)
#
#     @staticmethod
#     def dump_groups(file, group):
#         try:
#             data = json.load(open(file))
#         except FileNotFoundError:
#             data = {}
#
#         with open(file, 'w') as f:
#             stud_list = {}
#             for i in group.students:
#                 stud_list[i.name] = i.marks
#             data[group.group] = stud_list
#             json.dump(data, f, indent=2)
#
#     @staticmethod
#     def load_groups(file):
#         with open(file, "r") as f:
#             print(json.load(f))
#
#
# st1 = Student("Bodnya", [5, 4, 3, 4, 5, 3])
# st2 = Student("Nikolaenko", [2, 3, 5, 4, 2])
# st3 = Student("Birukov", [3, 5, 3, 2, 5, 4])
# sts1 = [st1]
# sts2 = [st2]
# sts3 = [st3]
# group1 = Group(sts1, "Group Python")
# group2 = Group(sts2, "Group C++")
# group3 = Group(sts3, "Group C#")
#
# Group.dump_groups("groups.json", group1)
# Group.dump_groups("groups.json", group2)
# Group.dump_groups("groups.json", group3)
# Group.load_groups("groups.json")


# import json
#
#
# class CountryCapital:
#     @staticmethod
#     def load(filename):
#         try:
#             data = json.load(open(filename))
#         except FileNotFoundError:
#             data = {}
#         finally:
#             return data
#
#     @staticmethod
#     def add_country(filename):
#         new_country = input("Введите название страны: ").lower()
#         new_capital = input("Введите название столице: ").lower()
#
#         data = CountryCapital.load(filename)
#
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
#     @staticmethod
#     def delete_country(filename):
#         del_country = input("Введите название страны: ").lower()
#
#         data = CountryCapital.load(filename)
#
#         if del_country in data:
#             del data[del_country]
#
#             with open(filename, 'w') as f:
#                 json.dump(data, f, indent=2)
#         else:
#             print("Такой страны в базе нет")
#
#     @staticmethod
#     def search_data(filename):
#         country = input("Введите название страны: ").lower()
#
#         data = CountryCapital.load(filename)
#
#         if country in data:
#             print(f'Страна {country.capitalize()} столица {data[country].capitalize()} есть в словаре')
#         else:
#             print(f'Страны {country.capitalize()} нет в словаре')
#
#     @staticmethod
#     def edit_data(filename):
#         country = input("Введите страну для корректировки: ").lower()
#         new_capital = input("Введите новое название столицы: ").lower()
#
#         data = CountryCapital.load(filename)
#
#         if country in data:
#             data[country] = new_capital
#             with open(filename, 'w') as f:
#                 json.dump(data, f, indent=2)
#         else:
#             print("Такой страны в базе нет")
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
#     elif index == "2":
#         CountryCapital.delete_country(file)
#     elif index == "3":
#         CountryCapital.search_data(file)
#     elif index == "4":
#         CountryCapital.edit_data(file)
#     elif index == "5":
#         CountryCapital.load_from_file(file)
#     elif index == "6":
#         break
#     else:
#         print("Введён некорректный номер")

# import requests
# import json
#
# response = requests.get("https://jsonplaceholder.typicode.com/todos")
# todos = json.loads(response.text)
# # print(todos)
#
# todos_by_user = {}  # {1: 10, 2:5, 3: 11}
#
# for todo in todos:
#     if todo['completed']:
#         try:
#             todos_by_user[todo['userId']] += 1
#         except KeyError:
#             todos_by_user[todo['userId']] = 1
#
# print(todos_by_user)
#
# top_users = sorted(todos_by_user.items(), key=lambda x: x[1], reverse=True)
# print(top_users)
#
# max_completed = top_users[0][1]
# print(max_completed)
#
# users = []
# for user, num_complete in top_users:
#     if num_complete < max_completed:
#         break
#     users.append(str(user))
# print(users)
#
# max_users = " and ".join(users)
#
# m = 's' if len(users) > 1 else ''
# print(f'user{m} {max_users} completed {max_completed} TODOs')
#
#
# def keep(todo):
#     is_complete = todo['completed']
#     has_num_count = str(todo["userId"]) in users
#     return is_complete and has_num_count
#
#
# with open('filter.json', 'w') as f:
#     filter_todos = list(filter(keep, todos))
#     json.dump(filter_todos, f, indent=2)

# CSV (Comma Separated Values - переменные разделённые запятыми)

import csv

with open('data.csv', encoding="UTF-8") as f:
    file_reader = csv.reader(f)
    count = 0
    for row in file_reader:
        if count == 0:
            print(f"Файл содержит столбцы: {', '.join(row)}")
        else:
            print(f'{row[0]} - {row[1]}. Родился в {row[2]}')
        count += 1
