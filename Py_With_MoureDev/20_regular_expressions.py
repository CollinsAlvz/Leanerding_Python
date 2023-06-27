#### Regular Expressions ###

import re

# march
my_string = "Esta es la leccion numero 20: Expresiones Regulares Leccion"
my_other_string = "Esta mo es la leccion numero 20: Expresiones Regulares"

print(re.match("Esta es la leccion", my_string))
match = print(re.match("Esta es la leccion", my_other_string))
if not (match == None):
    print(match)
    start, end = match.span()

# search

search = re.search("Esta es la leccion", my_string, re.I)
print(search)

# find all
findall = re.findall("leccion", my_string, re.I)
print(findall)

# split
print(re.split(":", my_string))

# sub
print(re.sub("Expresiones", "expresiones", my_string))

# patterns
pattern = r"[lL]eccion"
print(re.findall(pattern, my_string))
