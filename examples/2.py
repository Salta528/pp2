"""
import re

#Return a list containing every occurrence of "ai":

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)
"""
"""
import re

txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start()) 
"""
"""
import re

#Split the string at every white-space character:

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)
"""
 """
 import re

#Search for an upper case "S" character in the beginning of a word, and print the word:

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())
.span() returns a tuple containing the start-, and end positions of the match.
.string returns the string passed into the function
.group() returns the part of the string where there was a match
"""
