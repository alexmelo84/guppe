"""
Sistema de arquivos - Manipulação
"""

import os

# Verifica se um arquivo existe
print(os.path.exists('teste.txt'))  # True, arquivo existe
print(os.path.exists('test.txt'))  # False, arquivo não existe

# O mesmo vale para diretório
print(os.path.exists('geek'))  # True, diretório existe
print(os.path.exists('alex'))  # False, diretório não existe

# Criar arquivos (se o arquivo existir dará erro FileExistsError)
os.mknod('criado-via-modulo-os.txt')  # Não funciona em Windows

# Criar diretório (se o diretório existir erro FileExistsError)
os.mkdir('criado-via-modulo-os')

# Criar múltiplos diretórios
os.makedirs('criado-via-modulo-2/dir1/dir2')

# Renomear arquivos e diretórios
os.rename('criado-via-modulo-os', 'criado-via-modulo-os-renomeado')

# Deletar arquivo
os.remove('apagar.txt')

# Deletar diretório
os.rmdir('criado-via-modulo-2')

# Temporários
import tempfile

with tempfile.TemporaryDirectory() as tmp:
    print(f'Diretório temporário criado em {tmp}')
    with open(os.path.join(tmp, 'arquivo_temporario.txt'), 'w') as arquivo:
        arquivo.write('Conteúdo do arquivo temporário.\n')
    input()
