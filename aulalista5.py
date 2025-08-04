valores = []
quantidade = 0
valor_5 = False
continua = 'S'

while True:
    num = int(input('Digite um valor: '))
    valores.append(num)
    quantidade += 1
    if num == 5:
        valor_5 = True
    continua = str(input('Quer continuar? [S/N]').upper())
    if continua == 'N':
        break

valores.sort(reverse = -1)
print(f'Você digitou {quantidade} números')
print(f'Os valores em ordem decrescente: {valores}')
print(f'O valor 5 não foi encontrado na lista' if valor_5 == False else f'O valor 5 está na posição {valores.index(5)}')