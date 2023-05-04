#  EL FAMOSO "FIZZ BUZZ"

#  Escribe un programa que muestre por consola (con un print) los
#  números de 1 a 100 (ambos incluidos y con un salto de línea entre
#  cada impresión), sustituyendo los siguientes:
#  - Múltiplos de 3 por la palabra "fizz".
#  - Múltiplos de 5 por la palabra "buzz".
#  - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".


# Solucion Propia
def fizzbuzz_while():
    my_condition = 1
    while my_condition <= 100:
        if my_condition % 3 == 0 and my_condition % 5 == 0:
            print("fizzbuzz")
        elif my_condition % 5 == 0:
            print("buzz")
        elif my_condition % 3 == 0:
            print("fizz")
        else:
            print(my_condition)
        my_condition += 1


fizzbuzz_while()


# Solución de MoureDev
def fizzbuzz_for():
    for number in range(1, 101):

        if number % 3 == 0 and number % 5 == 0:
            print("fizzbuzz")
        elif number % 3 == 0:
            print("fizz")
        elif number % 5 == 0:
            print("buzz")
        else:
            print(number)


fizzbuzz_for()
