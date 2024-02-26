import re 
file=open("row.txt","r",encoding="utf8")
txt = file.read()
x = re.findall('[А-Я][а-я]+',txt)
print (x)
if (x):
    print("Match")
else:
    print("No match")