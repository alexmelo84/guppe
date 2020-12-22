"""
Len - len() retorna o número de itens de um iterável.

Sum - sum() retorna a soma dos itens de um iterável, podendo receber um valor inicial e somá-lo junto dos valores do
iterável. O valor padrão do valor inicial é 0 (zero).

Abs - abs() retorna o valor absoluto de um núemro real ou inteiro.

Round - round() retorna o valor arredondado de um número com n dígitos decimais. Caso o número de casas decimais
não for informado ele retorna o valor inteiro mais próximo.
"""

# Len
print(len('Alex Melo'))
print(len([1, 2, 3]))
print('Corinthians'.__len__())  # Internamente o len() executa essa função.

# Abs
print(abs(-5))
print(abs(5))
print(abs(9.123))
print(abs(100))

# Sum
print(sum(range(1, 6)))
print(sum(range(1, 6), 5))
print(sum(range(1, 6), -10))

# Round
print(round(1.23))
print(round(1.7))
print(round(1.234234234, 3))
print(round(1.7123123123, 5))
