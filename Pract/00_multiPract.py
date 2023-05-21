
def max(a, b):  # Numero Mayor entre dos numeros
    if a > b:
        print(f"{a} es mayor que {b}")
    else:
        print(f"{b} es mayor que {a}")


def max_de_tres(a, b, c):  # Numero Mayor de tres numeros
    if a > b and a > c:
        print(f"{a} es mayor que {b} y {c}")
    elif b > a and b > c:
        print(f"{b} es mayor que {a} y {c}")
    else:
        print(f"{c} es mayor que {a} y {b}")


def longitud_text(txt):  # Longitud de un texto sin usar el "len()"
    # print(len(txt))
    cont = 0
    for i in txt:
        cont += 1
    print(cont)


def vocal(letter):  # si un caracter es vocal
    list_vocals = list(["a", "e", "i", "o", "u"])
    for i in list_vocals:
        if i == letter or i.upper() == letter:
            return print(True)

    return print(False)


def sum_mult(num_1, num_2, num_3, num_4):
    suma = num_1 + num_2 + num_3 + num_4
    mult = num_1 * num_2 * num_3 * num_4
    print(f"La suma es: {suma} \n La multiplcacion es: {mult}")


def invertir(text):
    print(text[::-1])


def es_palindromo(text):  # validar si un texto es igual a revez o al derecho
    text_palidromo = invertir(text)
    if text_palidromo == text:
        return True

    return False


def superposicion(list1, list2):  # valida si dos listas continen al menos 1 dato igual
    for i in list1:
        for j in list2:
            if i == j:
                return print(True)

    return print(False)


def generar_n_caracteres(num, caract):
    return print(caract * num)


def histograma_procedimiento(list):
    imprimir = ""
    ast = "* "

    for i in list:
        imprimir += ast * i + "\n"
    return print(imprimir)


def max_in_list(list):
    mayor = 0
    menor = 0
    for i in list:
        if mayor < i:
            mayor = i
        else:
            menor = i

    return print(f"El nuemero mayor es {mayor}")


def large_txt(list):
    large = ""
    for i in list:
        if len(i) > len(large):
            large = i

    return print(f'"{large}" es el texto mas largo')


def filter_words(list, n):
    word = " "
    for i in list:
        if len(i) == n:
            word += i + " "

    return print(word)


def filter_uppers(cadena):
    cont = 0
    for i in cadena:
        if i == i.upper():
            cont += 1

    if cont == 0:
        return print("No cuenta con letras mayusculas")
    elif cont == 1:
        return print(f"Tiene {cont} mayuscula")
    else:
        return print(f"Tiene {cont} letras mayusculas")


def convert_binary():
    numero_binario = input("Ingrese un número binario: ")

    if not all(c in '01' for c in numero_binario):
        return print("El número ingresado no es un número binario válido.")
    else:
        decimal = 0
        for posicion, digito in enumerate(numero_binario[::-1]):
            decimal += int(digito) * 2 ** posicion

        return print("El número decimal es:", decimal)


def edad_actual():
    edad, año_actual, año_nacimiento, nombre, implimir = 0, "", "", "", ""

    año_actual = input("Ingrese el año actual: ")

    for i in range(1, 4):
        nombre = input("Ingrese su nombre: ")
        año_nacimiento = input("Ingrese el año de su nacimiento: ")

        edad = int(año_actual) - int(año_nacimiento)
        implimir += f"{nombre} cumplira {edad} años en {año_actual} \n"

    return print(implimir)


def edades_mayores_a20(tuple_edades):  # ultimar detalles
    # tuple_edades = ()
    cont = 0

    # for i in range(1, 6):
    #     tuple_edades = input(f"{i}.Ingrese una edad: ")

    for i in tuple_edades:
        if i > 20:
            cont += 1

    return print(f"{cont} es la cantidad de presonas mayores a 20")


def imprimir_nombre_inicial(list_nombs):  # ARREGLAR
    # list_nombs = []
    num_nombs = 0
    cont = 0

    # num_nombs = input("Ingrese cuantos nombre quiere ingresar?: ")

    # for i in range(int(num_nombs)):
    #     list_nombs.append(input(f"{i+1}. Ingrese el nombre: "))

    letra_inicial = input("Ingrese la letra con la que empieza el nombre: ")

    for i in list_nombs:
        if i[0] == letra_inicial.lower or i[0] == letra_inicial.upper():
            cont += 1

    return print(f' La cantidad de nombres que comiezan con la letra "{letra_inicial}" es: {cont}')


def es_bisiesto():
    anio = int(input('Digite el año: '))

    if anio % 4 == 0 and anio % 100 != 0 or anio % 400 == 0:
        print(f'El año {anio} es bisiesto')
    else:
        print(f'El año {anio} No es bisiesto')
