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
lista5 = list('Alexsandro Melo')

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

# Reverter a ordem (com o reverse)
lista2.reverse()
print(lista2)

# Reverter a ordem (com o slice)
print(lista5[::-1])

# Copiar
lista6 = lista4.copy()
print(lista6)

# Quantidade de itens
print(len(lista1))

# Remover o último elemento (o pop() alén de remover o último item, retorna o valor desse item)
print(lista2)
lista2.pop()
print(lista2)

# Remover elemento pelo índice
print(lista4)
lista4.pop(2)
print(lista4)

# Remover todos os elementos
print(lista5)
lista5.clear()
print(lista5)

# Replicar os itens
lista6 = lista1 * 3
print(lista6)

# Converter string para lista
teste = 'Cidade de São Paulo'
print(teste)
teste = teste.split()
print(teste)

nomeArquivo = 'arquivo_audio_gravacao_10_10_2020'
nomeArquivo = nomeArquivo.split('_')
print(nomeArquivo)

# Converter lista em string (a strig que vem antes do join() é o separador das palavras)
lista7 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
alfabeto = ' ' . join(lista7)
print(alfabeto)

# Aceita qualquer tipo de dado, mesmo misturados
lista8 = [1, 'iasajs', 1803710397093, False, 1243.545, [1, 2, 3]]
print(lista8)

# Iteração
for elemento in lista1:
    print(elemento)

carrinho = []
produto = ''
while produto != 'sair':
    print('Adicione um produto na lista ou digite "sair" para terminar: ')
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)

# Utilizando variáveis como itens
item1 = 'abc'
item2 = 'def'
item3 = 'ghi'
lista9 = [item1, item2, item3]
print(lista9)

# Acesso aos itens pelo índice
cores = ['verde', 'amarelo', 'azul', 'preto', 'branco']
print(cores[3])

# Acesso aos itens pelo índice de forma reversa
print(cores[-3])

# vídeo parado em 1:32:35
