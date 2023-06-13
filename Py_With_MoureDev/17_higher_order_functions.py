### HIGHER ORDER FUNTIONS ####

"""
 son capaces de encapsular comportamientos que pueden ser 
 reutilizados en diferentes contextos y aplicados a diferentes tipos de datos.
"""


from functools import reduce


def sum_one(value):
    return value + 1


def higher_order_function(value_one, value_two):
    return sum_one(value_one+value_two)


### Closures ###

"""

"""


def sum_ten():
    def add(value):
        return value + 10
    return add


add_closure = sum_ten()
print(add_closure(10))

### BUILT-IN HIGHER ORDER FUNTIONS ####

numbers = [2, 5, 10, 21]

# Map


def multiply_two(number):
    return number * 2


print(list(map(multiply_two, numbers)))
print(list(map(lambda number: number * 2, numbers)))

# Filter


def filter_greater_that_ten(number):
    if number >= 10:
        return True
    return False


print(list(filter(filter_greater_that_ten, numbers)))
print(list(filter(lambda number: number >= 10, numbers)))

# Reduce


def sum_two_values(value1, value2):
    print(value1)
    print(value2)
    return value1 + value2


print(reduce(sum_two_values, numbers))
