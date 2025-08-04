valores = []
continua = 'S'

while True:
    num = int(input('Digite um valor para adicionar na lista: '))
    if num in valores:
        print('Valor repetido, não vou adicionar!')
    else:
        valores.append(num)
        print('Valor adicionado com sucesso!')
    continua = str(input('Quer continuar? [S/N]').upper())
    if continua == 'N':
        break
valores.sort()
print(f'Você digitou os valoes {valores}')