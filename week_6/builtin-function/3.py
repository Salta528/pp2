word = str(input()) 
lst = [] 
for char in word: 
    lst.append(char) 
reversed_word = "".join(reversed(lst)) 
if word == reversed_word: 
    print(True) 
else: 
    print(False)
