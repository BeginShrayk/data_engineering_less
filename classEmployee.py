import yaml
import json
import pandas as pd

class Employee():

    def __init__(self):
        self.employees = {}

    def add_employee(self,employee_id, name, department):
        """Добавление сотрудника"""
        if employee_id in self.employees:
            print(f"Сотрудник с ID {employee_id} уже существует.")
            return False
        self.employees[employee_id] = {
            "name": name,
            "department": department
        }
        return True

    def remove_employee(self, employee_id):
        """Удалить сотрудника"""
        if employee_id in self.employees:
            del self.employees[employee_id]

    def get_employee(self, employee_id):
        return self.employees.get(employee_id, None)

    def get_employees(self):
        return self.employees

    def save_yaml_file(self, filename):
        """Запись в файл yaml"""
        try:
            with open(filename, 'w') as file:
                yaml.dump(self.employees, file, default_flow_style=False)
            return True
        except Exception as e:
            print(f"Ошибка при записи файла: {e}")
            return False

    def save_json_file(self, filename):
        """Запись файла в json"""
        try:
            json_file = json.dumps(self.employees, indent=4)
            with open(filename, "w") as file:
                file.write(json_file)
        except Exception as e:
            print(f"Ошибка при записи файла: {e}")

def load_json_file( filename):
    """Чтение из файла json"""
    try:
        with open(filename, "r") as file:
            json_object = json.load(file)
            print(json_object)
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
def load_yaml_file( filename):
    """Чтение из файла yaml"""
    try:
        with open(filename, 'r') as file:
            data = yaml.safe_load(file)
            print(data)
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        return None