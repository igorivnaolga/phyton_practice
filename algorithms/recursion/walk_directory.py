import os

def walk_directory(path, depth=0):
    all_dirs = list(os.listdir(path))
    print(all_dirs)
    try:
        for entry in os.listdir(path): #get all files and dirs
            full_path = os.path.join(path, entry)
            print(" " * depth + "|--" + entry)
            if os.path.isdir(full_path):
                walk_directory(full_path, depth + 1)
    except PermissionError:
        print(" " * depth + "|--[Permission denied]")


root_path = r"C:\Users\igori\GoIt\homeworks zip"
walk_directory(root_path)