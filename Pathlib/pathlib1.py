import os 
from pathlib import Path


#ls in linux, and you can specify it in path brackets
# for p in Path().iterdir():
#     print(p)

my_dir = Path("folder1")
my_file = Path("text1.txt")

print(my_dir.name)
print(my_file.name, "\n")

print(f"Extension: {my_dir.suffix}")
print(f"Extension: {my_file.suffix}", "\n")

print(my_dir.stem)
print(my_file.stem)