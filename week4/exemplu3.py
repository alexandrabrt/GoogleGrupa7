# class Star:
#
#     def __init__(self, nume, galaxie):
#         self.nume = nume
#         self.galaxie = galaxie
#
#     def __str__(self):
#         return f"{self.nume} in {self.galaxie}"
#
#
# soare = Star("Soare", "Calea Lacteei")
# print(soare)

class Parinte:

    def __init__(self, first_name):
        self.first_name = first_name
        pass

    def __str__(self):
        return f"Numele meu este {self.first_name}"


class Copil(Parinte):

    def __init__(self, name):
        print(name)
        super().__init__("Maria")
        print(self.first_name)
        self.name = name
        # Parinte.__init__(self, name)

    def __str__(self):
        return f"Prenumele meu este {self.name}"


obiect = Copil("Alexandra")
print(obiect)
