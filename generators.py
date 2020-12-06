"""
Generators

São o tuple comprehension.
"""

from sys import getsizeof

nomes = ['Alex', 'Alida', 'Angelina', 'Carlos']

res1 = [nome[0] == 'A' for nome in nomes]
print(type(res1))
print(res1)
print(getsizeof(res1))

res2 = (nome[0] == 'A' for nome in nomes)
print(type(res2))
print(res2)
print(getsizeof(res2))

# Comparação de uso de memória
list_comp = getsizeof([x * 10 for x in range(1000)])
set_comp = getsizeof({x * 10 for x in range(1000)})
dict_comp = getsizeof({x: x * 10 for x in range(1000)})
gen_comp = getsizeof(x * 10 for x in range(1000))

print('Uso de memória:')
print(f'List comprehension: {list_comp} bytes')
print(f'Set comprehension: {set_comp} bytes')
print(f'Dictionary comprehension: {dict_comp} bytes')
print(f'Generator expresion: {gen_comp} bytes')

# Iteração
iteravel = (x * 10 for x in range(10))
for numero in iteravel:
    print(numero)
