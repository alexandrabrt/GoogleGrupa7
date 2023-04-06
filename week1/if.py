a = 2
b = 2
c = 3
# mesaj, d = "a egal cu b", 0
# if a < b and (d := a + b) and d < a:
#     mesaj = "a mai mic ca b"
# elif a > b and (d := a - b) and d < a:
#     mesaj = "a mai mare ca b"
# elif a < c and (d := a + c) and d < a + b + c:
#     mesaj = "a mai mic ca c"
# print(f"Mesaj: {mesaj}")
# print(f"d: {d}")

rezultatul = a if a < c else c
print(rezultatul)
