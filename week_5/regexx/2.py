import re 
txt = "dcefabbbbbsv"
x = re.findall('ab{2,3}',txt)
print (x)
if (x):
    print("Match")
else:
    print("No match")
    