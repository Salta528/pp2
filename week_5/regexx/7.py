import re
for row in rows:
    s = ""
    if re.findall("_", row):
        words = row.split("_")
        for i in range(len(words)):
            words[i] = words[i].title()
        s = "".join(words)
        print(s)