"""
PDB - Python Debugger

Comandos básicos do PDB:
l = listar onde está no código
n = próxima linha
p = imprime variável
c = continua a execução, finalizando o debugging
"""

import pdb

# Com o import do PDB
nome = 'Alex'
sobrenome = 'Melo'
pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação Essencial em Python'
final = nome_completo + ' fez o curso ' + curso
print(final)

# Com o breakpoint() (não precisa importar o pdb para utilizá-lo)
nome = 'Alex'
sobrenome = 'Melo'
breakpoint()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação Essencial em Python'
final = nome_completo + ' fez o curso ' + curso
print(final)
