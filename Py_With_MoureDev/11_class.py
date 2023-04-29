### CLASES ###

class MyEmptyPerson:
    pass


class Person:
    def __init__(self, name, surname) -> None:
        self.name = name
        self.surname = surname
        self.full_name = f"{name} {surname}"

    def walk(self):
        print(f"{self.full_name} está caminando")


my_person = Person("Collins", "Alvarez")
print(my_person.name)
print(my_person.full_name)
my_person.walk()
