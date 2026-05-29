import os
import json
import csv

#exercise 1-2
# file_path = "users.txt"
# name = input("Enter your name: ")
# with open(file_path, "w") as file:
#     file.write(name)
# with open(file_path, "r") as file:
#     content = file.read()
# print(content)

# exercise-3
# file_path_line = "lines.txt"
# with open(file_path_line) as file:
#     content = file.readlines()
#     for line in content:
#         print(line.strip())

# exercise 4
# file_path_liste = "liste.txt"
# liste = []
# with open(file_path_liste, "r") as file:
#     for name in file:
#         liste.append(name)
# print(liste)

#exercise 5
# file_path = "orj_cont.txt"
# new_text = "This is a new line"
# with open(file_path, "a") as file:
#     file.write("\n" + new_text)

# #exercise 6
# file_path = "temp.txt"
# with open(file_path, "w") as file:
#     file.write("")
#     #you can also only "pass" instead of file.write()
#     #OR = open(file_path, "w").close()

#exercise 7
file_path = "output.txt" 
# with open(file_path, "w") as file:
#     file.write("First line\n" "Second line\n" "Third line")

#OR
# lines = ["First line\n", "Second line\n", "Third line\n"]
# with open(file_path, "w") as file:
#     file.writelines(lines)

#Even

with open(file_path, "w") as file:
    print("First line", file=file)
    print("Second line", file=file)
    print("Third line", file=file)