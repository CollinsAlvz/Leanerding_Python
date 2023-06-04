### List Comprehesion ###

# Se utiliza para crear una nueva lista a partir de
# una lista existente aplicando una expresión a cada elemento de la lista.

my_original_list = [22, 23, 24, 25, 26, 27, 28, 29]
my_list = [i//2 for i in my_original_list]
my_other_list = [i for i in range(10)]


def sum_five(number):
    return number * 5


my_list_example = [sum_five(i) for i in range(8)]
print(my_list, my_other_list, my_list_example)
