from Python.project.salary_system import employee


class HourlyEmployee(employee.Employee):
    """Сотрудники с почасовой оплатой"""

    def __init__(self, id_employee, name, hours_worked, hour_rate):
        super().__init__(id_employee, name)
        self.hours_worked = hours_worked
        self.hours_rate = hour_rate

    def calculate_payroll(self):
        return self.hours_worked * self.hours_rate
