"""1"""
# my_tuple = (1, 10, 100)
# t2 = my_tuple * 3
# print(len(t2))


"""2"""
# x = 10
# while x > 1:
#     x -= 1
#     continue
# print(x)

"""3"""
# x = {
#     "a": 1,
#     "b": 2,
#     "c": 3,
#     "a": 4,
#     "d": 5
# }
# print(x["a"])

"""4"""
# item = 1
# lista = [1, 2, 3]
# for x, y in enumerate(lista):
#     item *= x
#     print(lista[y+1])
#     break


"""5"""
# my_var = ["a", "b", {"x": 1, "z": {"key": 30}, "w": 2}, 10]
# print(my_var[2]["z"]["key"])
# print(my_var[2]["w"])
# print(my_var[3])

"""6"""
# x = ["ab", "cd", "ed"]
# for index, i in enumerate(x):
#     x[index] = i.title()
# print(x)


"""7"""
# i = 2
# while True:
#     if i // 3:
#         # pass
#         break
#     print(i)
#     i += 3


"""8"""
# lista1 = list(set([1, 3, 2, 3, 4, 5, 6]))
# del lista1[1:5]
# print(lista1)


"""9"""
# test_dict = {"element1": 1, "element2": 3, "element3": 2}
# res = list(test_dict.keys()) + list(test_dict.values())
# a = str(res)
# print(a)
# print(type(a))


"""10"""
# cuvant = "cu'va\\'nt"
# print(cuvant[::-1])


"""11"""
# l = list()
# for i in range(1, 3):
#     l.append(i**2)
#     # i = 3
#     print(l)


"""12"""
# print(set(list("pythonista")))

"""13"""
# list1 = [11, 33, 222, 14, 25]
# print(list1[-2:])


"""14"""
# x = [1, 2, 3, 4, 5]
# x.append(6)
# print(x)

"""15"""
# param_list = [22, 11, 9, 44, 56]
# length = len(param_list)
# temp_list = param_list[-1]
# param_list[0] = param_list[length - 1]
# param_list[length - 1] = temp_list
# print(param_list)


"""16"""
# x = []
# i = 0
# while True:
#     if len(x) >= 10:
#         break
#     i += 1
#     if i % 2 == 1:
#         continue
#     x.append(i)
# print(x)

"""17"""
lista = ['a', 'b', '12', 'cde']
new_list = []
for i in lista:
    i = [1, 2, 'abc']
    new_list.append(i)
    # break
print(new_list)
