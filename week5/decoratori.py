# def decorator_simplu(parametru):
#     print(f"Apelam functia {parametru.__name__}")
#     return parametru

#
# @decorator_simplu
# def functie_simpla():
#     return "Buna seara"


# functie_simpla()

# def decorator_depozit(functia_noastra):
#     def ambalaj_metoda(carti):
#         return f"Ambalam produse din {functia_noastra.__name__} care contine cartea {carti}"
#     return ambalaj_metoda


# @decorator_depozit
# def impachetare_carti(nume):
#     return nume

# def decorator_depozit(material):
#     def ambalaj(functia_noastra):
#         def ambalaj_intern(*carte):
#             return f"Ambalam produse din {functia_noastra.__name__} cu {material} care contine cartea {', '.join(x for x in carte)}"
#         return ambalaj_intern
#     return ambalaj


# @decorator_depozit("hartie")
# def impachetare_carti(*nume):
#     return nume

# print(impachetare_carti("Baltagul", "Amintiri din copilarie"))
# print(impachetare_carti("Ion"))
import time


def calculeaza_timpul(functia):
    def functie_interioara(parametru):
        inceput = time.time()
        suma = functia(parametru)
        sfarsit = time.time()
        print(f"Timp total de executie al functiei '{functia.__name__}': {sfarsit - inceput}")
        return suma
    return functie_interioara


@calculeaza_timpul
def adunare(number):
    suma = 0
    for i in range(number):
        suma += i
    return suma


print(adunare(1000000))
