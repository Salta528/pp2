import re
txt=str(input())
x=re.sub(r"([A-Z])", lambda fdf:" " + fdf.group(1),txt)
print (x)