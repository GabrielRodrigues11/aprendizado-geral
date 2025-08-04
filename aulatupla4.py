from random import randint

# UTILIZANDO TUPLE()
"""
numeros = tuple(randint(1,10) for c in range(5))
maior = max(numeros)
menor = min(numeros)

print(f'Os 5 números gerados foram: {numeros}')
print(f'O maior número foi: {maior}')
print(f'O maior número foi: {menor}')
print(f'Número em ordem crescente: {sorted(numeros)}')
"""

# JEITO MAIS SIMPLE

n = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10),)

print(f'Os 5 números gerados foram:', end=' ')
for c in n:
    print(f'{c}', end=' ')
    
print(f'\nO maior número foi: {max(n)}')
print(f'O maior número foi: {min(n)}')
print(f'Número em ordem crescente: {sorted(n)}')