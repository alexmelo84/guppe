"""
Teste de velocidade com expressões geradoras
"""

import time

# Generator expression
gen_inicio = time.time()
print(sum(num for num in range(1, 10000000)))
gen_tempo = time.time() - gen_inicio
print(f'Tempo total do generator expression: {gen_tempo}')

# List comprehension
list_inicio = time.time()
print(sum([num for num in range(1, 10000000)]))
list_tempo = time.time() - list_inicio
print(f'Tempo total da list comprehension: {list_tempo}')
