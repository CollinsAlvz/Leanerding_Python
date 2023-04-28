### LOOPS / BUCLES ###

# While

my_condition = 0
while my_condition < 5:
    print(my_condition)
    my_condition += 1
    if my_condition == 3:
        print("Es igual a 3")
        break
else:
    print("Mi condicion es mayor o igual que 3")


# FOR (Tambien piede usar el ELSE, BREAK)

my_list = [12, 5, 67, 895, 4, 2, 14, 64]

print("Lista recorrida por un FOR:")
for element in my_list:
    print(element)
    if element == 4:
        break

print("la ejecucion continua")
