import json


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __str__(self):
        a = ','.join(map(str, self.marks))
        return f'Студент: {self.name}: {a}'

    def add_mark(self, mark):
        self.marks.append(mark)

    def delete_mark(self, index):
        self.marks.pop(index)

    def edit_mark(self, index, new_mark):
        self.marks[index] = new_mark

    def average_mark(self):
        return round(sum(self.marks) / len(self.marks), 2)

    def dump_to_json(self):
        data = {"name": self.name, "marks": self.marks}
        with open(self.get_file_name(), "w") as f:
            json.dump(data, f)

    def load_from_file(self):
        with open(self.get_file_name(), "r") as f:
            print(json.load(f))

    def get_file_name(self):
        return self.name + '.json'


class Group:
    def __init__(self, students, group):
        self.students = students
        self.group = group

    def __str__(self):
        a = '\n'.join(map(str, self.students))
        return f'\nГруппа: {self.group}\n{a}'

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, index):
        return self.students.pop(index)

    @staticmethod
    def change_group(group_1, group_2, index):
        group_2.add_student(group_1.remove_student(index))

    def dump_to_json(self):
        data = {
            f'{self.group}': {
                'students': [
                    {'name': student.name, 'marks': student.marks} for student in self.students
                ]
            }
        }
        with open(self.get_file_name(), 'w') as file:
            json.dump(data, file, indent=2)
        return data

    @staticmethod
    def get_file_name():
        return 'all_groups.json'

    def load_from_file(self):
        with open(self.get_file_name(), 'r') as f:
            print(json.load(f))

    @staticmethod
    def add_group(group):
        try:
            data = json.load(open(Group.get_file_name()))
        except FileNotFoundError:
            data = {}

        data.update(Group.dump_to_json(group))
        with open(Group.get_file_name(), 'w') as file:
            json.dump(data, file, indent=2)


st1 = Student("Bodnya", [5, 4, 3, 4, 5, 3])
st2 = Student("Nikolaenko", [2, 3, 5, 4, 2])
st3 = Student("Birukov", [3, 5, 3, 2, 5, 4])
sts1 = [st1]
sts2 = [st2]
sts3 = [st3]
group1 = Group(sts1, "Group Python")
group2 = Group(sts2, "Group C++")
group3 = Group(sts3, "Group C#")

Group.add_group(group1)
Group.add_group(group2)
Group.add_group(group3)
