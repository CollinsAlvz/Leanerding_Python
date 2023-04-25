### STRINGS ###

my_strings = "Mi Strings"
other_strings = 'Other Strings'

print(len(my_strings))
print(len(other_strings))

print(my_strings+" "+other_strings)

jump_line_string = "Este es un string\ncon salto de linea"
print(jump_line_string)

# Formateo

name, surname, age = "Collins", "Alvarez", 24
print("Mi nombre es {} {} y me edad es {}".format(name, surname, age))
print(f"Mi nombre es {name} {surname} y me edad es {age}")
print("Mi nombre es %s %s y me edad es %d" % (name, surname, age))

# DESEMPAQUETADO DE CARACTERES
lenguage = "Python"
a, b, c, d, e, f = lenguage
print(a, b, c, d, e, f)

# Division of strings
lenguage_slice = lenguage[1:4]
print(lenguage_slice)

# Reverse
reversed_lenguage = lenguage[::-1]
print(reversed_lenguage)

# Funciones

print(lenguage.capitalize())

print(lenguage.upper())

print(lenguage.lower())

print(lenguage.swapcase())

print(lenguage.title())

print(lenguage.isnumeric())

print(lenguage.find("Python"))

print(lenguage.rfind("hon"))

print(lenguage.count("Python"))

print(lenguage.find("Python", 0))

print(lenguage.rfind("Python", 0))
