f = open("text.txt", "r")
cnt_lines = 0
for item in f.readlines():
    cnt_lines += 1
print(cnt_lines)
f.close()