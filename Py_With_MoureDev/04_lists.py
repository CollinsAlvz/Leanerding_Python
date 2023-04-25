# LISTS #

my_list = list(
    [1, 2, 3, 4, 5, 3, 3, 3]
)

my_other_list = [32, 45, 3, 23, 66, 34, 12]

print(len(my_list))
print(my_list)
print(len(my_other_list))
print(my_other_list)

my_list.append(12)
my_list.remove(12)
my_other_list.insert(2, 100)  # (posicion,dato)
print(my_other_list)

print(my_list[-1])

print(my_list.count(3))
