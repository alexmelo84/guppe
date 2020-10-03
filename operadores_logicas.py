"""
Operadores lógicas (AND, OR, NOT, IS)

- unários: NOT
- binários: AND, OR e IS
"""

ativo = True
logado = True

if ativo and logado:
    print('Bem-vindo, usuário')
else:
    print('Usuário inativo')

# Pythônico
if not ativo:
    print('Você precisa ativar sua conta.')
else:
    print('Conta ativa')

if ativo is True:
    print('Conta ativa')
else:
    print('Conta inativa')
