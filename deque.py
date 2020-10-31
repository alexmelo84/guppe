"""
Collections - Deque

É uma lista de alta performance.
"""

from collections import deque

deq = deque('alex')
print(deq)
print(type(deq))

# Adicionar elementos no final da lista
deq.append('s')
print(deq)

# Adicionar elementos no início da lista
deq.appendleft('o')
print(deq)

# Remover elementos do final da lista
print(deq.pop())
print(deq)

# Remover elementos do início da lista
print(deq.popleft())
print(deq)
