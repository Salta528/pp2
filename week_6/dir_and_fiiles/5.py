list = []
x=int(input())
for i in range(x):
    list.append(input())
with open("txt.txt", "w") as f:
    for item in list:
        f.write(f"{item}\n" )