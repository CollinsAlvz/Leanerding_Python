### Exceptions Haldling ###


num_one, num_two = 5, 1
num_two = "1"

# try except
try:
    print(num_one + num_two)
    print("No se sea producido un error")
except:
    print("Se ha producido un error")

# try except else (opcional)
try:
    print(num_one + num_two)
    print("No se sea producido un error")
except:
    print("Se ha producido un error")
else:  # -> se ejecuta si no hay un exception
    print("La ejecución continúa correctamente")

# try except else fanally (opcional)
try:
    print(num_one + num_two)
    print("No se sea producido un error")
except:
    print("Se ha producido un error")
else:  # -> se ejecuta si no hay un exception
    print("La ejecución continúa correctamente")
finally:  # -> se ejecuta siempre
    print("La ejecución continua")

# Exception for type
try:
    print(num_one + num_two)
    print("No se sea producido un error")
except TypeError:
    print("Se ha producido un TypeError")
except ValueError:
    print("Se ha producido un ValueError")

# Captura de la informacion de la excepcion
try:
    print(num_one + num_two)
    print("No se sea producido un error")
except ValueError as error:  # esto no se cumple
    print(error)
except Exception as e:
    print(e)
