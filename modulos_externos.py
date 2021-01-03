"""
Módulos externos

Utiliza-se o gerenciador de pacotes Pip (Python installer package).

Os pacotes oficiais são encontrados no site:
https://pypi.org/

Síntaxe:
pip install <nome-do-modulo>
"""

from colorama import init
from colorama import Fore, Back, Style

init()

print(Fore.RED + 'Alex Melo')
print(Back.GREEN + 'Alex Melo')
print(Style.DIM + 'Alex Melo')
print(Style.RESET_ALL)
print('Alex Melo')
