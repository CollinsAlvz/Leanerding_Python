### Python Package Manager ###

# PIP

from MyPackages import arithmetics
import requests
# import pandas
import numpy

print(numpy.version.version)

numpy_array = numpy.array([1, 2, 3, 4])
print(type(numpy_array))
print(numpy_array * 2)


# pip list
# pip uninstall pandas
# import requests

respose = requests.get('https://pokeapi.co/api/v2/pokemon?limit=151')
print(respose)
print(respose.status_code)
print(respose.json())

# Arithmetics Package
# from MyPackages import arithmetics

print(arithmetics.sum_two_values(5, 10))
