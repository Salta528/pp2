import os
for i in range(26):
    file_name = chr(65 + i) + ".txt"
    if not os.path.exists(file_name):
        with open(file_name, "x") as f:
            pass