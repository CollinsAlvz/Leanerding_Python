### Dates ####

from datetime import timedelta
from datetime import date
from datetime import time
from datetime import datetime

# Creacion de una fecha de datetime para este instante, hora local
now = datetime.now()


def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.day)


print_date(now)

# TIMESTAMP: Se usa principal mente en base de datos cuan
# quiere saber cuando se regirstro algo
timestamp = now.timestamp()
print(timestamp)

# crear una fecha personalida
year_2023 = datetime(2023, 1, 1)

print_date(year_2023)

# Time: es un objeto vacio | se trabaja sobre el
#  solo agrupa el tiempo
current_time = time()
print(current_time.hour)

# DATE: Solo agrupa la fecha
current_time = date.today()
print(current_time.year)
print(current_time.month)
print(current_time.day)

# TIMEDELTA: Se utiliza para realizar cálculos de tiempo y
# fechas, como sumar o restar días, horas, minutos, segundos, etc.

# Obtener la fecha y hora actual
ahora = datetime.now()
print("Hoy es:", ahora)
# Sumar 1 día a la fecha actual
dias = timedelta(days=5)
manana = ahora + dias
print("Mañana es:", manana)
print(f"Dias en total: {manana-ahora}")
