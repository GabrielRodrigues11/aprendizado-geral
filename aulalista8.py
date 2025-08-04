pessoas = list()
dados = list()
total = 0
continua = 'S'
maior_peso = menor_peso = 0
nome_maior_peso = list()

nome_menor_peso = list()

while True:
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Peso: ')))
    pessoas.append(dados[:])
    dados.clear()
    total += 1

    continua = str(input('Deseja continuar? [S/N]').upper())
    if continua == 'N':
        break

maior_peso = menor_peso = pessoas[0][1]

for p in pessoas:
    if p[1] > maior_peso:
        maior_peso = p[1]
        nome_maior_peso = [p[0]]
    elif p[1] == maior_peso:
        nome_maior_peso.append(p[0])
    
    if p[1] < menor_peso:
        menor_peso = p[1]
        nome_menor_peso = [p[0]]
    elif p[1] == menor_peso:
        nome_menor_peso.append(p[0])

print(f'Ao todo, você cadastrou {total} pessoas.')
print(f'O maior peso foi de {maior_peso}Kg. Peso de {nome_maior_peso}')
print(f'O menor peso foi de {menor_peso}Kg. Peso de {nome_menor_peso}')

