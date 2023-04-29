### CLASES ###

class MyEmptyPerson:
    pass


class Person:
    def __init__(self, name, surname) -> None:
        self.name = name
        self.__name = name  # se privatiza con dos guiones bajos + el nombre que se le de
        self.surname = surname
        self.full_name = f"{name} {surname}"

    def walk(self):
        print(f"{self.full_name} está caminando")

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name


my_person = Person("Collins", "Alvarez")
print(my_person.name)
print(my_person.full_name)
my_person.walk()
print(my_person.get_name())
