valores = []
maior = None
menor = None
pos_maior = []
pos_menor = []

for c in range(5):
    num = int(input(f'Digite um valor para a posição {c}: '))
    valores.append(num)

    if maior is None or num > maior:
        maior = num
        pos_maior = [c]
    elif num == maior:
        pos_maior.append(c)

    if menor is None or num < menor:
        menor = num
        pos_menor = [c]
    elif num == menor:
        pos_menor.append(c)

print(f'Valores: {valores}')
print(f'O maior valor digitado foi {maior} na posição {pos_maior}...')
print(f'O menor valor digitado foi {menor} na posição {pos_menor}...')