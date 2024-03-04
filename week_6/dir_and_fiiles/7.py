import os
def copy(src, dest):
    with open(src, 'rb') as source:
        content = source.read()
    with open(dest, 'wb') as destination:
        destination.write(content)
source__path = "A.txt"
destination__path = "A_copy.txt"
copy_file(source_path, destination__path)
if os.path.exists(destination__path):
    print(f"has been copied successfully.")
else:
    print(f"Failed")