import re

txt = "The rain in Spain, so cold."
y = re.sub("[ ,.]", ":", txt)
print(y)