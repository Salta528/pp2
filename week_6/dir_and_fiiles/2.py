import os
path = os.getcwd()                                       #retrieves the current working directory
file_name = input()
path_file = os.path.join(path, file_name)                #combines the path and file name to create the full path to the file.
print(f"exitence: {os.access(path_file, os.F_OK)}")      #if the file exists.
print(f"readability: {os.access(path_file, os.R_OK)}")   #readable 
print(f"writability: {os.access(path_file, os.W_OK)}")   #writable
print(f"executability: {os.access(path_file, os.X_OK)}") #executable