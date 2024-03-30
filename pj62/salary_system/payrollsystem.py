class PayrollSystem:
    @staticmethod
    def calculate(employees):
        print("Расчет заработной платы:")
        print("=" * 50)
        for employee in employees:
            print(f'Заработная плата: {employee.id} - {employee.name}')
            print(f'- Проверить сумму: {employee.calculate_payroll()}')
            print()
