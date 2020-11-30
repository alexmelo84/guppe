"""
Maps

Mapeamento de valores para funções.
Após processar o retorno do map() o retorno ficará vazio, ou seja, ele só pode ser processado uma vez.
"""

import math


def area(raio):
    """Calcula a área de um círculo."""
    return math.pi * (raio ** 2)


print(area(2))
print(area(78))

raios = [3, 1.89, 100, 89.2, 50]
areas = map(area, raios)  # função map(função, iterável)
print(list(areas))

# Map com lambda
print(list(map(lambda r: math.pi * (r ** 2), raios)))

# Outro exemplo (convertendo Celsius em Fahrenheit (9/5 * temperatura + 32)
cidades = [('Berlim', 29), ('Cairo', 36), ('Buenos Aires', 19), ('Los Angeles', 26), ('Toquio', 27),
           ('Nova Iorque', 28), ('Londres', 22)]
celsius_fahrenheit = lambda dado: (dado[0], (9/5) * dado[1] + 32)
print(list(map(celsius_fahrenheit, cidades)))
