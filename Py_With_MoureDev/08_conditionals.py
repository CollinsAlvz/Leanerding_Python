### Conditionals ###

my_conditional = False

if my_conditional:
    print("Se ejecuta la condicion de if")

my_conditional = 4*5
if my_conditional == 15:
    print("Es igual a 20")

if my_conditional > 10 and my_conditional < 20:
    print("Es mayor que 10 y menor que 20")
elif my_conditional == 20:
    print("Es igual 20")
else:
    print("Es menor que 10 y mayor que 20")

my_string = ""

if not my_string:
    print("Mi cadena está vacia")

print("Se ejecución continúa")
