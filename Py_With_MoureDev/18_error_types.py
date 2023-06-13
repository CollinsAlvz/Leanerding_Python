#### Error Types ###

# Syntax Error
# print "¡Hola Comunidad!" # <-ERROR
import math
from math import pi

print("¡Hola Comunidad!")


# Name Error
# print(name) # <-ERROR
idioma = "Español"
print(idioma)


# Index Error
my_list = ["Pythons", "Javas", "Dart"]
# print(my_list[4]) # <-ERROR
print(my_list[2])


# Module Not Found Error
# import maths # <-ERROR


# Attribute Error
# print(math.PI) # <-ERROR
print(math.pi)

# Key Error
my_dict = {"Nombre": "Collins", "Apellido": "Alvarez", "Edad": 24}
# print(my_dict["Nomber"]) # <- Error
print(my_dict["Nombre"])

# Import Error
# from math import PI # <- Error

# Value Error
# my_int = int("10 años") # <- Error
my_int = int("10")

# Zero Division Error
# print(4/0) # <- Error
print(4/2)
