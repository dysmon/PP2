import os

path = "D:\\Desktop\\KBTU_PP2" 

# 1 Write a Python program to list only directories, files and all directories, files in a specified path.
def directorites():
    # List only directories
    print("Directories:")
    for dir in os.listdir(path):
        if os.path.isdir(os.path.join(path, dir)):
            print(dir)
    
    # List only files
    print("\nFiles:")
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            print(file)
    
    # List all directories and files
    print("\nAll directories and files:")
    for item in os.listdir(path):
        print(item)

# 2 Write a Python program to check for access to a specified path. Test the existence, readability, writability and executability of the specified path
def Accessing():
    # Check if path exists
    if os.path.exists(path):
        print(f"{path} exists")

    # Check if path is readable
        if os.access(path, os.R_OK):
            print(f"{path} is readable")
        else:
            print(f"{path} is not readable")

    # Check if path is writable
        if os.access(path, os.W_OK):
            print(f"{path} is writable")
        else:
            print(f"{path} is not writable")

    # Check if path is executable
        if os.access(path, os.X_OK):
            print(f"{path} is executable")
        else:
            print(f"{path} is not executable")
    else:
        print(f"{path} does not exist")

# 3 Write a Python program to test whether a given path exists or not. If the path exist find the filename and directory portion of the given path.
def Existance():
    if os.path.exists(path):
        print(f"{path} exists")

    # Get the directory portion of the path
        directory = os.path.dirname(path)
        print(f"The directory portion of {path} is {directory}")

    # Get the filename portion of the path
        filename = os.path.basename(path)
        print(f"The filename portion of {path} is {filename}")
    else:
        print(f"{path} does not exist")

# 4 Write a Python program to count the number of lines in a text file.
def number_of_lines():
    path = "D:\\Desktop\\KBTU_PP2\\PP2\\lab5\\regex.py"
    with open(path, "r", encoding="UTF-8") as f:
       lines = f.readlines() # -> reads all lines  
       print(len(lines))

# 5 Write a Python program to write a list to a file.
def write_list():
    list_to_write = ["Java", "Python", "Golang"]
    with open("text1.txt", "w", encoding="UTF-8") as f:
        for item in list_to_write:
            f.write(item + "\n")
    with open("text1.txt", "r", encoding="UTF-8") as fi:
        print(fi.read())

# 6 Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt
def a_to_z():
    for i in range(65,91):
        with open(f"{chr(i)}.txt", "x") as _:
            pass

# 7 Write a Python program to copy the contents of a file to another file
def copy_files():
    with open("text1.txt", "r", encoding="UTF-8") as f:
        content = f.read()
    with open("copy.txt", "a", encoding="UTF-8") as fi:
        fi.write(content)

# 8 Write a Python program to delete file by specified path. Before deleting check for access and whether a given path exists or not.
def delete():
    path = ""
    if os.path.exists(path) and os.access(path, os.R_OK) and os.access(path, os.W_OK):
        os.remove(path)
    else:
        print("the file does not exist or you do not have permission")