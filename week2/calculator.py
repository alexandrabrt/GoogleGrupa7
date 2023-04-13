"""impartirea la 0"""
while True:
    operator_1 = input("Adauga primul operator: ")
    operator_2 = input("Adauga al doilea operator: ")
    operatie = input("Alege operatie pe care doresti sa o executi: ")
    if operatie in ['+', '-', '*', '/'] and operator_1.isdigit() and operator_2.isdigit():
        if int(operator_2) == 0 and operatie == '/':
            print('Impartirea la 0 nu este permisa')
            continue
        if operatie == '+':
            print(f"Suma celor doua numere {operator_1} + {operator_2} = {int(operator_1) + int(operator_2)}")
        elif operatie == '-':
            print(f"Diferenta celor doua numere {operator_1} - {operator_2} = {int(operator_1) - int(operator_2)}")
        elif operatie == '*':
            print(f"Produsul celor doua numere {operator_1} * {operator_2} = {int(operator_1) * int(operator_2)}")
        else:
            print(f"Impartirea celor doua numere {operator_1} / {operator_2} = {int(operator_1) / int(operator_2)}")
        break
    else:
        print(f"Alege o operatie din lista: {','.join(['+', '-', '*', '/'])}")


