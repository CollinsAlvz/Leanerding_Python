### TUPLAS ###

# estas no pueden ser modificado (es una estructura fija)
my_tuple = tuple()
my_other_tuple = ()

my_tuple = (1, 2, 3, "coco", "te")
print(my_tuple)
print(type(my_tuple))

my_other_tuple = (1, 2, 3, "pepino", "cola")

# print(my_tuple.count(2))
# print(my_tuple.index("te"))

del my_tuple

for i in my_other_tuple:
    print(i)
