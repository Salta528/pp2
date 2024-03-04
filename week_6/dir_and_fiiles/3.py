import os
path = input()
if os.path.exists(path):
    print(os.path.basename(path))
    print(os.path.dirname(path))
else:
    print("doesn't exist")
