
from random import random, randint, choice


def ejercicio_01(dato):
    tipo = type(dato)

    if isinstance(dato, str):
        replicar = dato * 5
        info = f"Tipo de dato: {tipo}\n Cantidad de palabras: {len(dato)}\n {replicar}"
    else:
        info = f"Tipo de dato: {tipo}\n No aplica \n No aplica"
    return print(info)


def ejercicio_02():
    dato_01 = "84"
    dato_02 = "104"
    dato_03 = "104.6"
    dato_04 = 104
    dato_05 = 104
    dato_06 = 104.3
    dato_07 = 104.56

    print(int(dato_01), type(int(dato_01)))
    print(float(dato_02), type(float(dato_02)))
    print(float(dato_03), type(float(dato_03)))
    print(float(dato_04), type(float(dato_04)))
    print(str(dato_05), type(str(dato_05)))
    print(str(dato_06), type(str(dato_06)))
    print(int(dato_07), type(int(dato_07)))


def ejercicio_03():
    nombre = "Maria"
    primer_apellido = "López"
    segundo_apellido = "Gómez"
    año_nacimiento = 1995
    edad = 2023 - año_nacimiento

    print(f"{nombre} {primer_apellido} {segundo_apellido} \nEdad: {edad}")


def ejercicio_04():
    nombre = input("Ingrese el nombre: ")
    primer_apellido = input("Ingrese el primer apellido: ")
    segundo_apellido = input("Ingrese el segundo apellido: ")
    año_nacimiento = input("Ingrese el año de nacimiento: ")
    nombre_completo = nombre + " " + primer_apellido+" " + segundo_apellido

    edad = 2023 - int(año_nacimiento)

    print(f"{nombre} {primer_apellido} {segundo_apellido}\nEdad: {edad} {type(edad)}")
    print(f"Caracteres del nombre: {len(nombre)}\nCaracteres del primer apellido: {len(primer_apellido)}\nCaracteres del segundo apellido: {len(segundo_apellido)} \nCaracteres del nombre completo: {len(nombre_completo)}")


def ejercicio_05():
    total_ventas_mes = float(input("Digite el total de la ventas del mes: "))
    total_gastos_mes = float(input("Digite el total de los gastos del mes: "))
    impuesto_IVA = total_gastos_mes * 0.13
    ganancia_mes = total_ventas_mes - total_gastos_mes
    renta = ganancia_mes * 0.02
    info = f"----------------------INFORME-----------------------\nTotal de ventas mensual: {total_ventas_mes} | Total de gastos mensual: {total_gastos_mes}\nImpuesto total aplicado a las ventas del mes: {impuesto_IVA}\nGanancias obtenidas del mes: {ganancia_mes}\nRenta a retener: {renta}"

    return print(info)


def ejercicio_06():
    fecha = "Hoy es miercoles 16 de mayo"
    print(
        f"Tamaño de caracteres: {len(fecha)}\nValor de la posición 10: {fecha[10]}\nValor de la posición 3: {fecha[3]}\nValor de la posición -4: {fecha[-4]}\nUltimo caracter: {fecha[-1]}\nCaracteres entre 4 y 18 de la posición : {fecha[4:18]}\nUltimos 5 caracteres: {fecha[-5:]}\nValor de la posición 17: {fecha[17]} | Tipo de dato: {type(fecha[17])}"
    )


def ejercicio_07():
    edad = int(input("Ingrese su edad: "))
    numero = int(input("Ingrese un numero: "))

    if edad >= 18:
        print("El usuario es mayor de edad")
    else:
        print("El usuario es menor de edad")

    if edad % 2 == 0:
        print("La edad del usuario es par")
    else:
        print("La edad del usuario es impar")

    if edad >= numero:
        print(f"La edad del usuario es mayor/igual que el numero {numero}")
    else:
        print(
            f'El numero "{numero}" ingresado por el usuario es mayor que la edad que tiene')


def ejecicio_08():
    list_password = ["a", "b", "c", "d", "e", "f", "g", "h", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
                     "A", "B", "C", "D", "E", "F", "G", "H", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
                     "1", "2", "3", "4", "5", "6", "7", "8", "9", "0" "/", "_", ".", "-", ","]

    number = int(input("Ingrese el tamaño de la contraseña que desea tener: "))
    password = " "

    for i in range(number):
        password += choice(list_password)

    return password


print(f"Password Random: {ejecicio_08()}")
