import yaml
import json


# # Запись и чтение файлов yaml
# l_connections = [
#     {
#         "name": "zekken",
#         "password": "123"
#     },
#     {
#         "name": "test_user",
#         "password": "456"
#     }
# ]
# # Запись файла в проект
# with open(r'connections', 'w') as file:
#     documents = yaml.dump(l_connections, file)

# Чтение файла, который находится в директории
# with open(r'connections') as file:
#     list = yaml.load(file, Loader=yaml.FullLoader)
#     print(list)
#     print(type(list))

# Запись и чтение файлов json

# dictionary = {
#     "name": "sasavot",
#     "password": "bebe21",
#     "temperature": 36.6,
#     "number_phone": "89504761010"
# }
#
# # Сохрание файла в json
# json_object = json.dumps(dictionary, indent=4)
#
# with open("sample.json", "w") as outfile:
#     outfile.write(json_object)
#
# # Чтение файла в json
#
# with open("sample.json", "r") as openfile:
#     json_object = json.load(openfile)
#
# print(json_object)
# print(type(json_object))

# Формат csv.py

