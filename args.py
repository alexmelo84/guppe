"""
Entendendo o *args

É um parâmetro como os outros, pode-se nomeá-lo como quiser, desde que comece com asterisco, por convenção, usa-se o
*args para definí-lo.

O *args é utilizado numa função para colocar os argumentos informados numa tupla.
"""


def soma_todos_numeros(*args):
    return sum(args)


print(soma_todos_numeros(1, 5, 10, 20, 37))


def verifica_info(*args):
    if 'Alex' in args and 'Melo' in args:
        return 'Bem-vindo, Alex!'
    return 'Você é um desconhecido.'


print(verifica_info())
print(verifica_info('João', 'Silva'))
print(verifica_info('Alex', 'Melo'))

# Passando uma lista com *args (adicione o * antes do argumento)
print(soma_todos_numeros(*[1, 5, 10, 20, 37]))
