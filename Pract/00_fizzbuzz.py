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
