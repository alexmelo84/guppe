"""
Tuplas (tuple)
São parecidas com lista, mas há duas diferenças básicas:
- tuplas são representadas por parênteses;
- são imutáveis, ou seja, ao criar uma tupla ela não poderá ser alterada. Toda operação numa tupla gera uma nova.

Por sererem imutáveis não há métodos de inclusão e deleção de elementos das tuplas.
Assim como nas listas, se todos os elementos forem inteiros ou reais dá para usar os métodos de soma, máximo e mínimo.

São mais rápidas do que listas.
São mais seguras por serem imutáveis.

"""

# Obs. 1: os parênteses não são obrigatórios
tupla1 = (1, 2, 3, 4, 5)
print(tupla1)
print(type(tupla1))

tupla2 = 1, 2, 3, 4, 5
print(tupla2)
print(type(tupla2))

# Obs. 2: não há tupla com 1 elemento
tupla3 = (1)
print(tupla3)
print(type(tupla3))

tupla4 = ('abcd')
print(tupla4)
print(type(tupla4))

# Para ser considerado uma tupla de 1 elemento precisa adicionar uma vírgula após o elemento
tupla5 = (1,)
print(tupla5)
print(type(tupla5))

tupla6 = ('abcd',)
print(tupla6)
print(type(tupla6))

# Gerando de um range
tupla7 = tuple(range(11))
print(tupla7)

# Desempacotamento
tupla8 = ('Alex', 'Melo', 'Python')
nome, sobrenome, linguagem = tupla8
print(nome, sobrenome, linguagem)

# Soma dos elementos
print(sum(tupla1))

# Máximo dos elementos
print(max(tupla1))

# Mínimo dos elementos
print(min(tupla1))

# Concatenar tuplas
tupla9 = (1, 2, 3)
print(tupla9)
tupla10 = (4, 5, 6)
print(tupla10)
print(tupla9 + tupla10)
print(tupla9)
print(tupla10)

# Pode-se armazenar a concatenação em uma nova tupla
tupla11 = tupla9 + tupla10
print(tupla11)

# Pode-se armazenar a concatenação em uma das tuplas
tupla9 = tupla9 + tupla10
print(tupla9)

# Verificar se algum elemento está na tupla
tupla12 = (1, 3, 5, 7, 11, 13)
print(3 in tupla12)

# Iterando
for item in tupla8:
    print(item)

for indice, item in enumerate(tupla8):
    print(indice, item)

i = 0
while i < len(tupla8):
    print(tupla8[i])
    i = i + 1

# Contando elementos
tupla13 = ('a', 'b', 'c', 'd', 'e', 'a', 'f', 'a', 'b')
print(tupla13.count('a'))

pessoa = tuple('Alex Melo')
print(pessoa)
print(pessoa.count('e'))

# Acessar elemento pelo índice
print(tupla1[3])

# Verifica o índice de um elemento
print(tupla1.index(2))

# Verifica o índice de um elemento a partir de um índice
print(tupla7.index(9, 5))

# Slicing
print(tupla7[0::2])

# Copiando (nã há shallow copy)
tupla14 = (1, 2, 4, 8, 16, 32)
print(tupla14)
novaTupla = tupla14
print(tupla14)
print(novaTupla)

tupla15 = (64, 128, 256)
print(tupla15)
novaTupla = novaTupla + tupla15
print(novaTupla)
