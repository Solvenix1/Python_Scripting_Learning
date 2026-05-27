import os
import csv
import json

file_path = "visitation_log.txt"
name = input("Enter your name: ")

def log_handling(name, file_path):
    if not(os.path.exists(file_path)):
        with open(file=file_path, mode = "x") as file:
            file.write(name + "\n")
        print(f"Log file not found. Registered name {name}")
    else:
        with open(file=file_path, mode="r") as file:
            registered_names = file.read().splitlines()
        if name in registered_names:
            print(f"Welcome back {name}")
        else:
            with open(file=file_path, mode = "a") as file:
                file.write(name + "\n")
            print(f"Hello, {name}")

log_handling(name, file_path)