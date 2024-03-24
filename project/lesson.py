# class Integer:
#     @staticmethod
#     def verify_coord(coord):
#         if not isinstance(coord, int):
#             raise ValueError(f"Координата {coord} должна быть целым числом")
#
#     def __set_name__(self, owner, name):
#         self.__name = name
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.__name]
#         # return getattr(instance, self.__name)
#
#     def __set__(self, instance, value):
#         self.verify_coord(value)
#         instance.__dict__[self.__name] = value
#         # setattr(instance, self.__name, value)
#
#
# class Point3D:
#     x = Integer()
#     y = Integer()
#     z = Integer()
#
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#
#
# p1 = Point3D(1, 2, 3)
# p1.x = 20
# print(p1.__dict__)


# Метаклассы

# a = 5
# print(type(a))
# print(type(int))

# class MyList(list):
#     def get_length(self):
#         return len(self)
#
#
# lst = MyList()
# lst.append(5)
# lst.append(8)
# print(lst, lst.get_length())
#
#
# MyList1 = type(
#     "MyList1",
#     (list,),
#     dict(get_length=lambda self: len(self))
# )
# lst1 = MyList()
# lst1.append(5)
# lst1.append(8)
# print(lst1, lst1.get_length())
#

# print(MyList1.__dict__)

# import Python.project.geometry.rect
# import Python.project.geometry.sq
# import Python.project.geometry.trian
# from geometry import rect, sq, trian
#
# # from geometry import *
# print("Hello")
#
#
# def run():
#     r1 = rect.Rectangle(1, 2)
#     r2 = rect.Rectangle(3, 4)
#
#     s1 = sq.Square(10)
#     s2 = sq.Square(20)
#
#     t1 = trian.Triangle(1, 2, 3)
#     t2 = trian.Triangle(4, 5, 6)
#
#     shape = [r1, r2, s1, s2, t1, t2]
#
#     for g in shape:
#         print(g.get_perimetr())
#
#
# if __name__ == '__main__':
#     run()

# from car.electrical import ElectroCar
#
# e_car = ElectroCar("Tesla", "T", 2018, 99000)
# e_car.show_car()
# e_car.description_battery()

class PayrollSystem:
    @staticmethod
    def calculate(employees):
        print("Расчет заработной платы:")
        print("=" * 50)
        for employee in employees:
            print(f'Заработная плата: {employee.id} - {employee.name}')
            print(f'- Проверить сумму: {employee.calculate_payroll()}')
            print()


class Employee:
    def __init__(self, id_employee, name):
        self.id = id_employee
        self.name = name


class SalaryEmployee(Employee):
    """Административные работники с фиксированной зарплатой"""

    def __init__(self, id_employee, name, weekly_salary):
        super().__init__(id_employee, name)
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary


class HourlyEmployee(Employee):
    """Сотрудники с почасовой оплатой"""

    def __init__(self, id_employee, name, hours_worked, hour_rate):
        super().__init__(id_employee, name)
        self.hours_worked = hours_worked
        self.hours_rate = hour_rate

    def calculate_payroll(self):
        return self.hours_worked * self.hours_rate


class SalaryComEmployee(SalaryEmployee):
    def __init__(self, id_employee, name, weekly_salary, commission):
        super().__init__(id_employee, name, weekly_salary)
        self.commission = commission

    def calculate_payroll(self):
        return self.weekly_salary + self.commission


salary_employee = SalaryEmployee(1, "Валерий Задорожный", 1500)
hourly_employee = HourlyEmployee(2, "Илья Кромин", 40, 15)
salary_com_employee = SalaryComEmployee(3, "Николай Хорольский", 1000, 250)

payroll_system = PayrollSystem()
payroll_system.calculate([
    salary_employee,
    hourly_employee,
    salary_com_employee
])
