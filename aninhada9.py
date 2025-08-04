valor = float(input('Qual o valor do produto? '))

print('Formas de pagamento')
print('[1] - A vista no dinheiro/cheque (10% de desconto)')
print('[2] - A vista no cartão (5% de desconto)')
print('[3] - Em até 2x no cartão (preço normal)')
print('[4] - 3x ou mais no cartão (20% de juros)')

opcao = int(input('Digite a opção: '))

if opcao == 1:
    valor_final = valor - (valor * 0.10)
    print(f'O valor final com desconto de 10% é de R${valor_final:.2f}')
elif opcao == 2:
    valor_final = valor - (valor * 0.05)
    print(f'O valor final com desconto de % é de R${valor_final:.2f}')
elif opcao == 3:
    valor_final = valor
    print(f'O valor é de R${valor_final}')
elif opcao == 4:
    parcelas = int(input('Em quantas parcelas deseja dividir? '))
    if parcelas >= 3:
        valor_final = valor * 1.2
        parcelas_valor = valor_final / parcelas
        print(f'O valor final com 20% de juros é de R${valor_final}, parcelado em {parcelas}x de R${parcelas_valor}')
    else:
        print('Escolha inválida! As parcelas comecam de 3x ou mais.')
else:
    print('Opção inválida!')

    

