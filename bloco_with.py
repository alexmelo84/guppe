"""
With

O with cria um contexto que é fechado após utilizar o recurso. Essa é a forma Pythônica de se trabalar com arquivos.
"""

with open('teste.txt') as arquivo:
    print(arquivo.readlines())
