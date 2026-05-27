# import os

# file_path = "File Handling/test0.txt"
# file_path1 = "C:/Users/Suleyman/Desktop/"

# print("Python is currently looking inside:", os.getcwd())

# if os.path.exists(file_path1):
#     print(f"The location '{file_path1}' exists")
    
#     if os.path.isfile(file_path1):
#         print("Yes it is file")
#     elif os.path.isdir(file_path1):

#         print("It is a directory")
# else:
#     print("File location doesn't exist")
# ===============================================
    
# import os

# txt_data = "Information in text file"

# file_path = "output.txt"

# try:
#     if not(os.path.exists(file_path)):
#         with open(file= file_path, mode="x") as file:
#             file.write(txt_data)
#             print("Succesfully created fresh file")
#     else:
#         with open(file=file_path, mode="a") as file:
#             file.write("(This message is added)")
#             print("additional message is added")
# except Exception as e:
#     print(f"Something went wrong :{e}")

# try:
#     with open(file=file_path, mode="x") as file:
#         file.write(txt_data)
#         print("great1")
# except FileExistsError:
#     with open(file=file_path, mode="a") as file:
#         file.write("[Additional]")
#         print("great2")

# employees = ["Hasan", "Arif", "Kamil", "Kazim"]
# file_path2 = "C:/Users/Suleyman/Documents/Coding/Python/Scripting/File Handling/Employees.txt"
# for name in employees:
#     try:
#         with open(file=file_path2, mode="x") as file1:
#             file1.write(name)
#     except FileExistsError:
#         with open(file=file_path2, mode="a") as file1:
#             file1.write("\n" + name)
#======================
#This variant is fastest
# with open(file=file_path2, mode= "a") as file1:
#     for name in employees:
#         file1.write(name)
#================================================================================

# import json
# employee1 = {
#             "Name" : "Kim",
#              "Age" : 19,
#              "Job" : "Cooker"
#             }

# file_path = "C:/Users/Suleyman/Documents/Coding/Python/Scripting/File Handling/Employees.json"

# try:
#     with open(file=file_path, mode="w") as file:
#     # with open(file=file_path, mode="x") as file:
#         json.dump(employee1, file, indent = 3)
#         print(f"JSON file was created at {file_path}")
# except FileExistsError:
#     pass
#     # with open(file=file_path, mode="a") as file:
#     #     json.dump("Added part", file)
#     #     print("Added part is ok")

#============================================================

# import os 
# import json
# import csv

# employees = [
#     ["Name", "Age", "Job"],
#     ["SpongeBob", 20, "Cook"],
#     ["Patrick", 23, "Engineer"],
#     ["Ken", 18, "Ofisiant"]
#              ]

# file_path = "C:/Users/Suleyman/Documents/Coding/Python/Scripting/File Handling/Employees.csv"

# try:
#     with open(file=file_path, mode="w", newline='') as file:
#         writer = csv.writer(file)
#         for row in employees:
#             writer.writerow(row) 
#         print(f"csv file {file_path} created")
# except FileExistsError:
#     print("File already exists")




#====================
#Reading files in python
import os
import csv
import json

file_path = "C:/Users/Suleyman/Documents/Coding/Python/Scripting/File Handling/Employees.txt"

try:
    with open(file=file_path, mode="r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("There is no such file")
except PermissionError:
    print("Permission denied")

file_path_json = "C:/Users/Suleyman/Documents/Coding/Python/Scripting/File Handling/Employees.json"


try:
    with open(file=file_path_json, mode="r") as file:
        content = json.load(file)
        print(content["Job"])
except FileNotFoundError:
    print("File not found")
except KeyError:
    print("This keyword not found")

file_path_csv = "C:/Users/Suleyman/Documents/Coding/Python/Scripting/File Handling/Employees.csv"
try:
    with open(file=file_path_csv, mode = "r") as file:
        content = csv.reader(file)
        for line in content:
            print(line[0])
except FileNotFoundError:
    print("File not found")