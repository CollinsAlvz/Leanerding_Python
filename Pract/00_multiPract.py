def otra_cosa():
    print('"En este curso aprederemos sobre "Python" en un leguaje de prgramación"')

    type_int = 450
    type_float = 18.5
    mensaje = '"Esta es la segunda sesion sobre el lenguaje Python"'

    print(mensaje, "tipo de dato: ", type(mensaje), type_int, "tipo de dato: ", type(
        type_int), type_float, "tipo de dato: ", type(type_float))

    num_1, num_2, num_3, num_4 = 2, 3, 4, 17

    print(num_2 ** num_3)
    print(num_4 * num_1)
    print(num_4/num_1)
    print(num_4//num_1)
    print(pow(num_1, num_3))


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


large_txt(["texto", "mas", "largo", "esparanza", "cosas"])
