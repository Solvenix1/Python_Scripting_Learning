import os
import json
import csv
from pathlib import Path

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
# file_path = "read_n_lines.txt"
# with open(file_path, "r") as file:
#     for i, line in enumerate(file):
#         if i > n:
#             break
#         print(line)


# with open(file_path, "r") as file:
#     for _ in range(n):
#         print(file.readline().strip())



#exercise 15
# n = 4
# file_path = "read_n_lines.txt"
# with open(file_path, "r") as file:
#     for i in file.readlines()[-n:]:
#         print(i.strip())

#exercise 16
# targets = {1,3,5}

# file_path = "read_n_lines.txt"
# # with open(file_path, "r") as file:
# #     for i in file.readlines():
# #         for x in i:
# #             if x in targets:
# #                 print(i.strip())

# with open(file_path, "r") as file:
#     for line_num, line in enumerate(file, start = 1):
#         if line_num in targets:
#             print(line.strip())

#exercise 17
# mem = ""
# length = 0
# file_path = "long_words.txt"
# with open(file_path, "r") as file:
#     for word in file.read().split():
#         if len(word) > length:
#             length = len(word)
#             mem = word
# print(f"Longest word: {mem}")

# longest = ""
# with open(file_path, "r") as file:
#     words = file.read().split()
# for word in words:
#     if len(word) > len(longest):
#         longest = word
# print(longest)

#exercise 18
    # freq = {}

    # with open("Letter_count.txt", "r") as file:
    #     content = file.read().lower()
    # for letter in content:
    #     if letter.isalpha():
    #         if letter in freq:
    #             freq[letter] += 1
    #         else:
    #             freq[letter] = 1
    # for key, value in freq.items():
    #     print(f"{key} : {value}")

#exercise 19
# file_path = "search_words.txt"
# c = 1
# target = "Python"
# with open(file_path, "r") as file:
#     content = file.readlines()
#     for i in content:
#         if target in i:
#             print(f"{target} found in line {c}")
#         c += 1


#exercise 20 
# clean_file = "clean.txt"
# messy_file = "messy.txt"

# with open(messy_file, "r") as mfile, open(clean_file, 'w') as cfile:
#     for line in mfile:
#         cfile.write(line.strip() + " ")
# with open(clean_file, 'r') as file:
#     print(file.read())

#exercise 21
# with open("low_up_case.txt", 'r') as mfile:
#     for letter in mfile:
#         print(letter.swapcase())
#sonra da bunu basqa fayla yaz so simple

#exercise 22
words = []
new = []

with open('story.txt', 'r') as file:
    content = file.read()
updated= content.replace("Java", "Python")
with open('story.txt', 'w') as file:
    file.write(updated)

        
        


# with open('story.txt', 'r')as file:
#     print(file.read())