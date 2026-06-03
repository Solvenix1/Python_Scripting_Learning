import csv
from itertools import islice
# file_path = "simple_co2.csv"

# with open(file_path, 'r') as csvfile:
#     reader = csv.reader(csvfile)
#     reader_b =
#     header = next(reader)
#     print(header)

#     for row in reader:
#         print(row)
#         #break # for only heading


# with open(file_path, 'r') as csvfile:
#     reader = csv.DictReader(csvfile)

#     for row in reader:
#         print(row)

file_path = "simple_co2_skipone.csv"

# with open(file_path , 'r') as csvfile:
#     reader = csv.reader(csvfile)
#     for i in range(7):
#         next(reader)
#     for row in reader:
#         print(row)

with open(file_path, 'r') as csvfile:
    reader = csv.DictReader(islice(csvfile,7,None))

    for row in reader:
        print(row, '\n')