
# 5. Сделать 2 метода для работы с JSON - для сохранения в файл и для чтения из файла. Название фала должно передаваться в метод входным параметром.
# 6. В другом поле хранить Pandas DataFrame с данными. Написать ещё 2 метода - для сохранения данных в файл .csv и для чтения данных из .csv файла в датафрейм.
# Так же написать для 4, 5, 6 пунктов методы, которые будут просто отображать данные, которые внутри объекта хранятся.
# 7. Попробовать при помощи объекта класса прочитать данные из YAML формата, а сохранить - в JSON.
# 8. Наоборот: прочитать данные из JSON, сохранить в YAML.
import classEmployee as ce

yandex = ce.Employee() #ЭТО ФАЙЛ В КОТОРЫЙ ДОБАВЛЯЮТСЯ ДАННЫЕ
yandex.add_employee(1,"Ilya", "Data Engineer")
yandex.add_employee(2,"Igor", "Data Analytic")
# print(ce.Employee.get_employees(yandex))

ce.load_yaml_file("employees.yaml")
ce.load_json_file("employees.json")