

class Exemplu1:

    counter = 1

    def name(self):
        return "Maria"

class Exemplu2(Exemplu1):
    pass
    # counter = 2
    # def name(self):
    #     return "Alexandra"

class Exemplu3(Exemplu2):
    pass

    # def name(self):
    #     return "Diana"


obiect1 = Exemplu3()
# print(obiect1.name())
print(obiect1.counter)
