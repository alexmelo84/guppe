"""
Set comprehension
"""

numeros = {num for num in range(1, 7)}
print(numeros)

numeros2 = {x ** 2 for x in range(10)}
print(numeros2)

letras = {letra for letra in 'Corinthians'}
print(letras)
