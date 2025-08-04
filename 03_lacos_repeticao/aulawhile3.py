from random import randint
computador = randint(1, 10)
palpites = 0
jogador = 1
acertou = False
print('Vamos jogar!! Adivinhe o número que estou pensando de 0 - 10!')
while not acertou:
    jogador = int(input('Digite o número: (1-10)'))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... tente outra vez.')
        elif jogador > computador:
            print('Menos... tente outra vez.')  
print(f'PARABÉNS, VOCÊ ACERTOU!! O número era {computador} e você acertou em {palpites} tentativas!')