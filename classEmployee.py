

class Employee():

    def __init__(self):
        self.employees = {}

    def add_employee(self, employee_id, name, department):
        """Добавление сотрудника"""
        self.employees[employee_id] = {
            "name": name,
            "department": department
        }

    def remove_employee(self, employee_id):
        """Удалить сотрудника"""
        if employee_id in self.employees:
            del self.employees[employee_id]

    def get_employee(self, employee_id):
        return self.employees.get(employee_id, None)