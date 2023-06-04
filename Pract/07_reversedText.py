# Revertir una cadena sin usar una funcion propia del lenguaje#

def reverse(txt):
    reversed_txt = ""
    for i in range(len(txt)-1, -1, -1):
        reversed_txt += txt[i]
    return reversed_txt


print(reverse("Hola"))
