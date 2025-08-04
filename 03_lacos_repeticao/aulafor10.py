maior = 0
menor = float('inf')

for c in range(1,6):
    peso = float(input(f'Digite o peso da {c}ª pessoa: '))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print(f'O maior peso é o {maior}Kg.')
print(f'O menor peso é o {menor}Kg.')