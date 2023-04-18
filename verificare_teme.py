v=0
# CNP=input("Please enter CNP: ")
# CNP = '2890904460082'  # cnp valid
# cnp = '2890231460082'  # ziua din luna nu exista
# cnp = '2890229470086'  # jj nu exista
# cnp = '2890229460011'  # nnn nu exista
cnp = '2890229400014'  # c nu exista
CNP = cnp
if len(CNP)!=13:
    print("CNP invalid")
    v=1

if not CNP.isdigit():
    print("CNP invalid! Please use only digits!")
    v=1
# We verify S
s= int(str(CNP)[0])
if s not in range(1,9):
    print("S invalid")
    v=1

#We verify JJ:

counties = ["%.2d" % i for i in range(1,47)]
counties.append('51')
counties.append('52')
inserted_county = CNP[6:8]
if inserted_county in counties:
    pass
else:
    print('JJ invalid')
    v=1

# We verify NNN:
if CNP[9:12].isdigit() and int((CNP)[9:12]) >= 1:
    pass
else:
    print("NNN Not Valid")
    v=1
#We verify the control number
check_number = "279146358279"
sum = 0
control_digit = 0
for i in range(0,12):
    sum += int(check_number[i]) * int(CNP[i])
if sum % 11 == 10:
    control_digit = 1
else:
    control_digit = sum % 11
print(control_digit)
if control_digit != int(CNP[-1]):
    print("Control digit invalid")
    v = 1

if v == 0:
    print("CNP-ul a fost validat cu succes")
else:
    print("CNP-ul nu a putut fi validat")
