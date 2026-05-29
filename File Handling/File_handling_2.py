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
# file_path = "output.txt" 
# with open(file_path, "w") as file:
#     file.write("First line\n" "Second line\n" "Third line")

#OR
# lines = ["First line\n", "Second line\n", "Third line\n"]
# with open(file_path, "w") as file:
#     file.writelines(lines)

#Even

# with open(file_path, "w") as file:
#     print("First line", file=file)
#     print("Second line", file=file)
#     print("Third line", file=file)

#exercise 8
# file_path = "some_data.txt"
# if os.path.exists(file_path):
#     print("File exists")
# else:
#     print("File not found")

#exercise 9
# file_path = "missing.txt"
# try:
#     with open(file_path, "r") as file: pass
# except FileNotFoundError:
#     print("Error: The file was not found.")

#exercise 10
# i = 0
# file_path = "Data_lines.txt"
# with open(file_path, "r") as file:
    # for _ in file:
    #     i += 1
    # for line in file.readlines():
    #     i += 1
# print(i)

#exercise 11
# file_path = "Data_words_lines.txt"

# with open(file_path, "r") as file:
#     # print(len(file.read().split()))
#     content = file.read()
# words = content.split()
# print(f"Total word count: {len(words)}")

#exercise 12
# file_path = "data_words_count.txt"
# with open(file_path, "r") as file:
#     #print(len(file.read().strip()))
#     content = file.read()
    

# print(len(content))
# count = 0
# with open(file_path, "r") as file:
#     for x in file:
#         for c in x:
#             count += 1
# print(count)
#Attention there is an error when i write count = sum(1 for c in x)

#exercise 13
# count = 0
# file_path = "python_count.txt"
# with open(file_path, "r") as file:
#     content = file.read().split()
#     for i in content:
#         if i == "Python":
#             count += 1
# print(count)

#exercise 14
# n = 3
# 
# file_path = "read_n_lines.txt"
# with open(file_path, "r") as file:
#     for _ in range(n):
#         print(file.readline().strip())

#exercise 15
n = 3 
i = 0
file_path = "read_lastn_lines.txt"
with open(file_path, "r") as file:
    content = file.readlines()
    for line in content[-n:]:
        print(line.strip())

        
    
    



     
    
