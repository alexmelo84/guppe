"""
Listas

É o equivalente a matrizes e vetores (arrays) em outras linguagens, com a diferença que listas são
dinâmicas (não tem tamanho físico) e aceitam qualquer tipo de dado

As listas são representadas por colchetes: []
"""

lista1 = [1, 12, 787, 7, 9, 9012, 132, 85, 131, 7, 9128]
lista2 = ['A', 'l', 'e', 'x', ' ', 'M', 'e', 'l', 'o']
lista3 = []
lista4 = list(range(11))
lista5 = list('Alex Melo')

# Verifica se um valor existe na lista
num = 8
if num in lista4:
    print(f'O {num} está contido na lista4.\n')
else:
    print(f'O {num} não está contido na lista4.\n')

# Ordenação
lista1.sort()
print(lista1)

# Total de ocorrências de um valor
print(lista1.count(7))
print(lista2.count('e'))

# Adicionar 1 elemento por vez (adiciona ao final da lista)
lista1.append(90)
print(lista1)

# Adicionar 1 elemento por vez (informando qual a posição da lista será inserido, sem substituir valor, apenas acresce)
lista1.insert(0, 909090)
print(lista1)

# Adicionar lista numa lista
lista1.append([1212, 4, 7607, 5])
print(lista1)

# Adicionar múltiplos itens individualmente (só aceita objetos iteráveis, como lista ou string, por exemplo)
lista1.extend([12, 13, 14, 15])
print(lista1)

# Juntar duas listas (mesma ação que o 'extend')
lista6 = lista1 + lista2
print(lista6)
