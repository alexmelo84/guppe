"""
Definindo funções

Começa com a palavra reserva 'def'.
O nome da função deve ser no padrão snake case (separado por underline).
Parâmetros de entrada são opcionais e devem ser separados por vírgula.
O corpo da função é onde ocorre o processamento da função, deve ter uma identação de 4 espaços.

def nome_funcao(parametros):
    codigo_da_funcao

Nas funções a ordem dos parâmetros é:
- parâmetros obrigatórios;
- *args;
- parâmetros com valor padrão (não obrigatório);
- e **kwargs.
"""

cores = ['vermelho', 'verde', 'blue']
curso = 'Python Essencial'

# Função builtin (integrada à linguagem)
print(cores)
print(curso)

# Função de um tipo de dado
cores.append('preto')
print(cores)

# Criar função


def diz_oi():
    print('Oi!')


def cantar_parabens():
    print('Parabéns pra você!')
    print('Nessa data querida!')
    print('Muitas felicidades!')
    print('Muitos anos de vida!')


diz_oi()
cantar_parabens()

# Definir variável com o tipo de uma função e executar a função através da variável
cantar = cantar_parabens
cantar()
