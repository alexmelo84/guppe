"""
StringIO

Usado para criar e ler arquivos em memória, evitando criar em disco e ter problemas de permissão.
"""

from io import StringIO

texto = 'String simples'

# Criando o arquivo em memória de uma variável, mas poderia criá-lo vazio e adicionar o texto posteriormente
arquivo = StringIO(texto)

# Manipulando o arquivo em memória como um arquivo em disco
print(arquivo.read())

arquivo.write('Nova linha')
arquivo.seek(0)

print(arquivo.read())
