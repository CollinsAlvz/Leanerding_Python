### SETS ###

"""
Los set no admiten datos repetidos
cuando son nueron los ordena de menor a mayor
"""
my_set = set()
my_other_set = {}

my_other_set = {12, 43, 657, 78}
my_set = my_set.union(my_other_set)

my_other_set.add(1)
my_other_set.add(5)
my_other_set.add(1234)
print(my_other_set)

# comprobar existencia
print(10 in my_other_set)
print(12 in my_other_set)


print(my_set)
print(my_other_set.difference(my_set))
