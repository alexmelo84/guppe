"""
Listas aninhadas (Nested lists)

Algumas linguagens possuem uma estrutura de dados chamada array:
    - unidimensionais (arrays ou vetores);
    - multidimensionais (matrizes).

Em Python não existem arrays, há as listas.
"""

listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(listas)

# Acesso aos dados
print(listas[0])
print(listas[0][1])

print(listas[1])
print(listas[1][-2])

# Iteração
for lista in listas:
    print(lista)
    for item in lista:
        print(item)

# List comprehension
[[print(valor) for valor in lista] for lista in listas]

# Gerar matriz/tabuleiro 3x3
tabuleiro = [[numero for numero in range(1, 4)] for valor in range(1, 4)]
print(tabuleiro)

# Jogo da velha
velha = [['X' if numero % 2 == 0 else 'O' for numero in range(1, 4)] for valor in range(1, 4)]
print(velha)

# Valores iniciais
print([['*' for i in range(1, 4)] for j in range(1, 4)])
