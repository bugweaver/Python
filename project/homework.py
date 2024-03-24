from salary_system import payrollsystem, salaryemployee, hourlyemployee, salarycomemployee

salary_employee = salaryemployee.SalaryEmployee(1, "Валерий Задорожный", 1500)
hourly_employee = hourlyemployee.HourlyEmployee(2, "Илья Кромин", 40, 15)
salary_com_employee = salarycomemployee.SalaryComEmployee(3, "Николай Хорольский", 1000, 250)

payroll_system = payrollsystem.PayrollSystem()
payroll_system.calculate([
    salary_employee,
    hourly_employee,
    salary_com_employee
])
