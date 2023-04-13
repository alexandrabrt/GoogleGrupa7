"""1"""
# def a(d):
#     d[4] = 'd'
#     return d
#
#
# x = {
#     1: 'a',
#     2: 'b',
#     3: 'c'
# }
#
# y = a(x)
# print(y)


"""2"""
# def functie1(lista_cuvinte):
#     lista = []
#     for n in lista_cuvinte:
#         lista.append((len(n), n))
#     lista.sort()
#     return lista[-1][0], lista[-1][1]
#
#
# rezultat = functie1(['pip', 'Exercitiu', 'Python'])
# print(rezultat[1], rezultat[0])


"""3"""
# def functie(lista):
#     item = 1
#     for x, y in enumerate(lista):
#         item *= x
#         return lista[y+1]
#     print('dddd')
#
#
# lista = [1, 2, 3]
# print(functie(lista))


"""4"""
# def functie1():
#     print("Variabila este definita?", var)
#     # return 'a'
#
# var = 30
# functie1()
# print(var)



"""5"""
# try:
#     i = int("Hello")
# except Exception as e:
#     print(e)


# """6"""
# def function(new_list: list):
#     length = len(new_list)
#     temp_list = new_list[-1]
#     new_list[0] = new_list[length - 1]
#     new_list[length - 1] = temp_list
#     return new_list
#
# param_list = [22, 11, 9, 44, 56]
# function(param_list)


"""7"""
x = input('> ')

try:
    x = int(x)
    print('a value is:', a)
except (ValueError,  NameError) as e:
    print('Eroare de valoare', e)
except NameError as e:
    print('Eroare la declarare', e)
else:
    print('Else')
finally:
    print('Finally')
