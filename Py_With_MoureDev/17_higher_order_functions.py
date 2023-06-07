### HIGHER ORDER FUNTIONS ####

"""
 son capaces de encapsular comportamientos que pueden ser 
 reutilizados en diferentes contextos y aplicados a diferentes tipos de datos.
"""


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
