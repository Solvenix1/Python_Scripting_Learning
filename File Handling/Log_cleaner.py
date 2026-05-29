import os
import csv
import json



file_path = "raw_logs.txt"
error_file_path = "critical_errors.txt"

txt_data = """[INFO] 10:00 AM - System started
[DEBUG] 10:01 AM - Database connection initialized
[ERROR] 10:05 AM - Failed to connect to server
[INFO] 10:06 AM - Retrying connection
[ERROR] 10:10 AM - Connection timeout
[DEBUG] 10:11 AM - Clearing cache memory
"""

with open(file_path, "w") as file:
    file.write(txt_data)


if os.path.exists(file_path):
    print("File exists. Proceeding...")

    with open(file_path, mode="r") as file:
        content = file.read().splitlines()

    with open(file_path, "r") as file:
        content = file.read().splitlines()

    with open(error_file_path, "w") as file:
        for line in content:
            if "[ERROR]" in line:
                file.write(line + "\n")
    print("Critical errors found")
    with open(error_file_path, "r") as file:
        errors = file.read()
        print(errors)
else:
    print("File doesn't exists")

#continue







