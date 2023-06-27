### File Handling ###

import xml
import csv
import json
import os

# .txt file
txt_file = open("Py_With_MoureDev/my_file.txt", "r+")  # Lectura y escritura
# print(txt_file.read())
# print(txt_file.readline())
# txt_file.write("\nEscribiendo una nueva linea en mi archivo")
txt_file.close()
# os.remove("Py_With_MoureDev/my_file.txt")

# .json file

json_file = open("Py_With_MoureDev/my_file.json", "w+")


json_test = {
    "name": "Collins",
    "surname": "Alvarez",
    "age": 24,
    "language": "Python",
}

json.dump(json_test, json_file)

json_file.close()

# for line in json_file.readlines():
#     print(line)

# with open("Py_With_MoureDev/my_file.json") as my_other_file:
#     for line in my_other_file.readlines():
#         print(line)

# .csv file
csv_file = open("Py_With_MoureDev/my_file.csv", "w+")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["name", "surname", "age", "language"])
csv_writer.writerow(["Collins", "Alvarez", 24, "python"])

csv_file.close()

with open("Py_With_MoureDev/my_file.csv") as my_other_file:
    for line in my_other_file.readlines():
        print(line)

# .xlsx file | import xlsx Debe intalarse el modulo

# .xml file
