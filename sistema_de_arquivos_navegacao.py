"""
Sistema de arquivos e navegação

Para manipular arquivos do sistema operacional é necessário importar o módulo os.
"""

import os

# Ver o diretório atual
print(os.getcwd())

# Mudar o diretório
os.chdir('..')
print(os.getcwd())

# Verificar se o caminho do diretório é relativo ou absoluto
print(os.path.isabs('C:\\'))
print(os.path.isabs(os.getcwd()))

# Pegar informações do sistema operacional
print(os.name)
# print(os.uname())  # Mac e Linux, Windows não tem essa informação

# Mudar de pasta
print(os.getcwd())
res = os.path.join(os.getcwd(), 'guppe')
os.chdir(res)
print(os.getcwd())

# Listar diretórios
print(os.listdir())  # Lista o diretório atual
print(os.listdir('C:\\'))  # Lista de um diretório específico

# Listando com mais detalhes
scanner = os.scandir()
arquivos = list(scanner)
print(arquivos[0])
print(arquivos[0].inode())
print(arquivos[0].is_dir())
print(arquivos[0].is_file())
print(arquivos[0].is_symlink())
print(arquivos[0].name)
print(arquivos[0].path)
print(arquivos[0].stat())
scanner.close()
