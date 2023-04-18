"""lambda"""
# variabila = lambda x, y: x + y
# print(variabila(2, 3))


# def variabila(x, y):
#     return x + y

# players = [{"prenume": 'Ion',
#             "nume": 'Popescu',
#             "varsta": 32},
#            {"prenume": "Ana",
#             "nume": "Badea",
#             "varsta": 23},
#            {"prenume": "Ileana",
#             "nume": "Oancea",
#             "varsta": 12}]
#
# sortare = sorted(players, key=lambda player: player['varsta'])
# print(sortare)


"""map"""
# list_1 = [1, 5, 4, 6, 8, 11, 3, 12]
# list_3 = map(lambda x: x*2, list_1)
# print(list(list_3))


"""zip"""
# list_with_int = [1, 2, 3, 4, 5]
# list_with_str = ('one', 'two', 'three', 'four', 'five')
# list_with_str_2 = (('unu', 'unu'), 'doi', 'trei', 'patru', 'cinci')
# result = zip(list_with_int, list_with_str, list_with_str_2)
# print(list(result))

"""list comprehension"""
# lista_1 = [1, 2, 3, 4, 5, 6, 7]

# lista_2 = []
# for i in lista_1:
#     if i % 2 == 0:
#         lista_2.append(i)
#     else:
#         lista_2.append(0)
# print(lista_2)

# lista_2 = [i for i in lista_1 if i % 2 == 0]
# lista_2 = [i if i % 2 == 0 else 0 for i in lista_1]
# print(lista_2)

# lista_2 = []
# for x in range(50):
#     if x % 2 == 0:
#         if x % 5 == 0:
#             lista_2.append(x)
# lista_2 = [x for x in range(50) if x % 2 == 0 if x % 5 == 0]
# lista_2 = [x if x % 5 == 0 else [] for x in range(50) if x % 2 == 0]
# print(lista_2)

# dictionar = {}
# for num in range(1, 11):
#     dictionar[num] = num * num
# dictionar = {num: num * num for num in range(1, 11) if num % 2 == 0}
# dictionar = {num: num * num if num % 2 == 0 else 0 for num in range(1, 11) if num % 2 == 0}
# print(dictionar)
