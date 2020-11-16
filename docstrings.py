"""
Documentando com Docstrings
"""


def diz_oi():
    """
    Uma simples função que diz oi ao usuário.
    """
    return 'Oi!'


print(diz_oi())
print(help(diz_oi))
print(diz_oi.__doc__)


def exponencial(numero, potencia=2):
    """
    Calcula uma dada potência de um dado número.
    :param numero: Número que será calculada a potência.
    :param potencia: Valor da potência que será calculada. Padrão 2 se não for informado.
    :return: Retorna o resultado da potência.
    """
    return numero ** potencia


print(exponencial.__doc__)
