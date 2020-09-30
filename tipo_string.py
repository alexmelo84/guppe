"""
Tipo string
"""

# No Python as strings são armazenadas da seguinte maneira: 'A', 'l', 'e', 'x', '_', 'M', 'e', 'l', 'o'
nome = 'Alex_Melo Teste'

# maiúsculo
print(nome.upper())
# minúsculo
print(nome.lower())
# quebra de string
print(nome.split('_'))
print(nome.split()[0])
# slice
print(nome[0:5])
# inversão de string Pythônica
# : = primeiro elemento; : = segundo elemento; -1 = inverta
print(nome[::-1])
# substituição
print(nome.replace('e', 'u'))
