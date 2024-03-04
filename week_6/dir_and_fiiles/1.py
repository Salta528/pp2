import os
def f(path):                        #takes a single argument
    all_items = os.listdir(path)                 #it retrieves a list of all items (files and directories) in the specified directory.
    dirs = [item for item in all_items if os.path.isdir(os.path.join(path, item))]
    files = [item for item in all_items if os.path.isfile(os.path.join(path, item))]           #the function creates two lists - one for subdirectories (dirs), and another for files (files)

    print("Directories:", dirs)
    print("Files:", files)
    print("All Items:", all_items)
directory_path=input()
f(directory_path)