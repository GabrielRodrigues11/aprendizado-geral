valores = []

for n in range(5):
    num = int(input('Digite um valor: '))
    if n == 0 or num > valores[-1]:
        valores.append(num)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(valores):
            if num <= valores[pos]:
                valores.insert(pos, num)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1
print('-=' * 15)
print(f'Lista ordenada: {valores}')

"""
# UTILIZANDO O BISECT

import bisect

valores = []

for _ in range(5):
    num = int(input("Digite um valor: "))
    bisect.insort(valores, num) 
    print(f"Adicionado na posição {valores.index(num)} da lista...")

print("-=" * 15)
print(f"Lista ordenada: {valores}")
"""