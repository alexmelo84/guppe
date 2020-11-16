"""
Funções com parâmetro padrão

Em Python, os parâmetros com valor padrão devem estar no final da declaração (após os parâmetros sem valor padrão)
"""

# Exemplo básico
print('Alex Melo')
print()


def exponencial(numero, potencia=2):
    return numero ** potencia


print(exponencial(4, 2))
print(exponencial(5))


def mostra_informacao(curso='Python', instrutor=False):
    if curso == 'Python' and instrutor:
        return 'Bem-vindo, instrutor!'
    elif curso == 'Python':
        return 'Você não é instrutor'
    return f'Olá, {curso}'


print(mostra_informacao())
print(mostra_informacao(instrutor=True))
print(mostra_informacao('Python'))
print(mostra_informacao('Alex'))


def soma(num1, num2):
    return num1 + num2


def subtracao(num1, num2):
    return num1 - num2


def mat(num1, num2, func=soma):
    return func(num1, num2)


print(mat(10, 5))
print(mat(20,3, subtracao))

# Escopo
instrutor = 'Geek'  # Global


def diz_oi():
    instrutor = 'Alex'  # Local
    return f'Oi, {instrutor}'


print(diz_oi())

# Utilizando uma variável global dentro de uma função (evitar isso, contudo)
total = 0


def incrementa():
    global total

    total = total + 1
    return total


print(incrementa())

# Função dentro de função


def fora():
    contador = 0

    def dentro():
        nonlocal contador  # Equivalente ao global, mas pega a variável da função pai (nesse caso, a função fora())
        contador = contador + 1
        return contador
    return dentro()


print(fora())
