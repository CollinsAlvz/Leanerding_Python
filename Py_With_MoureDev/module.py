def sumrest_numbers(type_data, num_one, num_two):
    if type_data == "suma":
        print(num_one+num_two)
    elif type_data == "resta":
        if num_two > num_one:
            print(num_two-num_one)
        else:
            print(num_one-num_two)


def mayor_menor(num_one, num_two):
    if num_one > num_two:
        print(f"El {num_one} es mayor a {num_two}")
    else:
        print(f"El {num_two} es mayor a {num_one}")
