import re
txt=str(input())
x=re.sub(r"([A-Z])", lambda fdf:"_" + fdf.group(1).lower(),txt)
print (x)