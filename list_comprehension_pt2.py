"""
List Comprehension

Pode-se adicionar estruturas condicionais lógicas.
"""

numeros = [1, 2, 3, 4, 5, 6]
pares = [numero for numero in numeros if numero % 2 == 0]
impares = [numero for numero in numeros if numero % 2 != 0]
print(pares)
print(impares)

pares2 = [numero for numero in numeros if not numero % 2]
impares2 = [numero for numero in numeros if numero % 2]
print(pares2)
print(impares2)

res = [numero * 2 if numero % 2 == 0 else numero / 2 for numero in numeros]
print(res)
