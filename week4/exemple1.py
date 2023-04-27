"""
Max este o pisica mare care doarme toata ziua.
obiect -> Max (substantive)
clasa -> pisica (substantiv)
proprietatea -> marimea (mare) (adjectiv)
atributul -> doarme (adverb)

O masina Dacia merge repede.
obiectul -> Dacia
clasa -> masina
proprietatea -> repede
atributul -> merge (verb).
"""

# class Pisica:
#     pass
#
# Max = Pisica()
# Tom = Pisica()

stack = []


def push(val):
    stack.append(val)


def pop():
    value = stack[-1]
    del stack[-1]
    return value

push(3)
push(2)
push(1)

print(pop())
print(pop())
print(pop())
