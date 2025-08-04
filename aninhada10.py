from random import choice
from time import sleep

opcoes = ['PEDRA', 'PAPEL', 'TESOURA']
computador = choice(opcoes)

print('-=' * 10)
print('''Vamos jogar JOKENPO!
Suas opções: 
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
print('-=' * 10)

escolha = int(input('Qual é sua jogada? '))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')\
sleep(1)
print('-=' * 10)

jogador = opcoes[escolha]

if jogador not in opcoes:
    print('Opção inválida! Escolha entre pedra, papel ou tesoura.')
else:
    print(f'Eu escolhi {computador}!')
    if jogador == computador:
        print('EMPATE!')
    elif (jogador == 'pedra' and computador == 'tesoura') or \
         (jogador == 'tesoura' and computador == 'papel') or \
         (jogador == 'papel' and computador == 'pedra'):
        print('VITÓRIA! Você venceu!')
    else:
        print('DERROTA! Você perdeu!')
