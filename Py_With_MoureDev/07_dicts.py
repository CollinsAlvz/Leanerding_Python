### Dictionaries ###

# tipo de almacenamiento clave/valor

my_dict = dict()

my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre": "Collins", "Apellido": "Alvarez", "Edad": 24}
print(my_other_dict)

my_dict = {"Nombre": "Collins", "Apellido": "Alvarez", "Edad": 24,
           "Lenguajes": {"C#", "JavaScript", "Python"}
           }
print(my_dict)

# Se agrega un nuevo campo
my_dict["BD"] = "SQL"
print(my_dict)

# Eliminacio de un campo
del my_dict["BD"]
print(my_dict)


print("Nombre" in my_dict)

# Operaciones
print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())
