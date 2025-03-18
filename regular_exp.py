import re

str = "This is me"

print(re.findall("^[a-zA-Z ]*$", str))