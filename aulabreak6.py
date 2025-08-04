continua = 'S'
total_gasto = acima_1000 = preco = 0
mais_barato = None
nome_mais_barato = ''

print('-=' * 10)
print('LOJA SUPER BARATÃO')
print('-=' * 10)

while True:
    nome_produto = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$'))
    total_gasto = total_gasto + preco

    if preco > 1000:
        acima_1000 += 1

    if mais_barato is None or preco < mais_barato:
        nome_mais_barato = nome_produto
        mais_barato = preco

    print('-' * 20)
    continua = ' '
    while continua not in 'SN': 
        continua = str(input('Quer continuar? [S/N]').upper())

    if continua == 'N':
        break

print('------------ FIM DO PROGRAMA ------------')
print(f'O total da compra foi R${total_gasto}')
print(f'Temos {acima_1000} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nome_mais_barato} que custa {mais_barato}')