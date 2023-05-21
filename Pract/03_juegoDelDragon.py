import random
import time


def introduccion():
    print("Estamos en una tierra llena de dragones.")
    time.sleep(2)
    print("Delante de nuestro, se ven dos cuevas.")
    time.sleep(2)
    print("En una cueva, el dragon es amigable y compartira el tesoro contigo.")
    time.sleep(2)
    print("El otro dragon es codicioso y hambriento, y te va a comer ni bien te vea")


def cambiar_cueva():
    cueva = 0
    while cueva != 1 and cueva != 2:
        cueva = int(input("¿A qué cueva quieres entrar? 1 o 2\nR: "))

    return cueva


puntos_ganados = 0


def get_puntos_ganados():
    global puntos_ganados
    puntos_ganados += 100

    return puntos_ganados


def check_cueva(op_cueva):

    print("Te acercas a la cueva...")
    time.sleep(2)
    print("Está oscuro y tenebroso.")
    time.sleep(2)
    print("Un gran dragón salta delante tuyo, abre su boca y...")
    print("")
    time.sleep(2)

    friendly_cueva = random.randint(1, 2)

    if op_cueva == friendly_cueva:
        print("Inclinas tu cabeza y extiendes tu mano cuidadosamente.")
        time.sleep(2)
        print("El dragón acepta tu saludo y amablemente te entrega el tesoro...")
        get_puntos_ganados()
    else:
        print("El dragón te ataca y te derrota.")

    empezar_nuevo = input("¿Quieres jugar de nuevo? sí o no\nR: ")

    while empezar_nuevo == "s" or empezar_nuevo == "si":
        check_cueva(cambiar_cueva())

    print(f"Total de puntos obtenidos: {get_puntos_ganados()}")
    puntos_ganados = 0


# introduccion()
check_cueva(cambiar_cueva())
