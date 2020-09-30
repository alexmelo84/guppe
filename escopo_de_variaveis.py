"""
Escopo de vairáveis

Python é uma linguagem de tipagem dinâmica, ou seja, ao declarar uma variável, não definimos o tipo dela,
isso é inferido ao atribuir umm valor à variável
"""

# Escopo global: a variável numero é acessível em todos os locais do sistema
numero = 20
print(numero)


# Escopo local: a variável novo só é acessível dentro da função
def teste(parametro):
    novo = parametro + 10
    print(novo)


teste(numero)
# Se tentar acessar a variável novo fora da função dará erro
#print(novo)
