from functii2 import functie2

variabila1 = 2
a = 3
b = 2
msg = 3


def functie_1(a, b):
    # global msg
    # msg = 'Hello'
    variabila1 = a + b
    return variabila1


print(msg, 'rand 16')
suma = functie_1(1, 2)
print(msg, 'rand 14')
print(suma)

functie2(4, 5)
