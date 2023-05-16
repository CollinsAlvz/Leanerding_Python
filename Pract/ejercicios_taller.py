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
