import re 
txt = "dfga"
x = re.findall('ab*',txt)
print (x)
if (x):
    print("Match")
else:
    print("No match")