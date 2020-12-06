"""
Any e All

all() -> retorna True se todos os elementos do iterável são verdadeiros ou se o iterável está vazio.
any() -> retorna True se algum elemento do iterável é verdadeiro. Se o iterável estiver vazio retorna falso.
"""

# all()
print('all()')
print(all([0, 1, 2, 3]))  # False (o 0 é falso)
print(all([1, 2, 3]))  # True
print(all([]))  # True

nomes = ['Alex', 'Alida', 'Angelina']
print(all(nome[0] == 'A' for nome in nomes))

# any()
print('any()')
print(any([0, 1, 2, 3]))  # True
print(any([1, 2, 3]))  # True
print(any([0, False, {}]))  # False
print(any([0, False, {}, 1]))  # True
print(any([]))  # False

nomes2 = ['Alex', 'Alida', 'Angelina', 'Carlos']
print(any(nome[0] == 'C' for nome in nomes2))  # True
print(any(nome[0] == 'B' for nome in nomes2))  # False
