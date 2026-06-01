import os 
from pathlib import Path

# print(Path.cwd())

# for p in Path().iterdir():
#     print(p)
# print(" ")

# my_dir = Path("Folder1")
# my_file = Path("text1.txt")
# # new_file = my_dir / "new_file.txt"
# new_file = my_dir.joinpath("new_file.txt")

# p = Path("TempDir/Subdir")
#p.mkdir(parents=True) 
#parents mode allow us to create subfolders also
#p.rmdir() 
# #delete folder    
# f = Path("renamed.txt")
# # f.touch()
# f.rename("renamed.txt")
# f.unlink()


# print(new_file)

# print(new_file.parent.joinpath("new_file2"))
#absolute() can show us absolute path of directory or file
#resolve() same thing with absolute but ti can resolve sim links and relatives, e.g. below cc is parent dir
# print(" ")
# p0 = Path("..").absolute()
# print(p0)
# p1 = Path("..").resolve()
# print(p1)

#__file__ with resolve can show where currently file is locating
# p = Path(__file__).resolve()
# print(p)

# p = Path("~/dotfiles").expanduser()
# print(p)
# p1 = Path.home() / "dotfiles"
# print(p1)

# dotfiles = Path.home() / "Documents" / "Coding/Python/Scripting_Learning/File Handling/Employees.json"
# with open(dotfiles)as file:
#     print(file.read())

# for file in dotfiles.rglob("*.json",case_sensitive=True):
#     print(file)

#rglob in reccursive, simple glob in only folder 

# print(my_dir.parent.absolute())
# print(my_file.parent.absolute())
# print(new_file.absolute().parent)


# print(my_dir.exists())
# print(my_file.exists())
# print(new_file.exists())

# print(f"Full name: {my_dir.name}")
# print(f"Full name: {my_file.name}")
# print(f"Full name: {new_file.name}")

# print(f"Suffix: {my_dir.suffix}")
# print(f"Suffix: {my_file.suffix}")
# print(f"Suffix: {new_file.suffix}")

# print(f"Only name: {my_dir.stem}")
# print(f"Only name: {my_file.stem}")
# print(f"Only name: {new_file.stem}")