### FUNCIONES ###

def my_funtion():
    print("Esto es una función")


my_funtion()


def sum_two_values(num_one, num_two):
    print(num_one + num_two)


sum_two_values(12, 4)


def sum_two_values_return(num_one, num_two):
    resultado = num_one + num_two
    return resultado


# my_resultado = sum_two_values_return(2, 6)
print(sum_two_values_return(5, 5))


def print_name(name, surname):
    print(f"{name} {surname}")


print_name("Collins", "Alvarez")
print_name(surname="Alvarez", name="Collins")


def print_name_default(name, surname, alias="Sin alias"):
    print(f"{name} {surname} {alias}")


print_name_default("Collins", "Alvarez")
print_name_default("Collins", "Alvarez", "Co")


def print_texts(*txt):
    print(txt)


print_texts("varias", "palabras", "un_param", 12)


def print_upper_texts(*txt):
    for text in txt:
        print(text.upper())


print_upper_texts("varias", "palabras", "un_param")
