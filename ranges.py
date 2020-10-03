"""
Ranges
São utilizados para gerar sequências numéricas de forma ordenada não aleatória
"""

# Sem valor de início (o valor de início padrão é 0)
for i in range(8):
    print(i)

print('\n')

# Com valor de início
for i in range(4, 9):
    print(i)

print('\n')

# Com valor do passo
for i in range(1, 6, 2):
    print(i)

print('\n')

# Ordem inversa
for i in range(10, 0, -1):
    print(i)

print('\n')

# List do range
lista = list(range(6))
print(lista)
