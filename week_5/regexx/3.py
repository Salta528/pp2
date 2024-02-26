import re 
txt = "ert_sdfg_df"
x = re.findall('[a-z]+_[a-z]+',txt)
print (x)
if (x):
    print("Match")
else:
    print("No match")