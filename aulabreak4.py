from random import randint

print('-=' * 10)
print(('VAMOS JOGAR PAR OU ÍMPAR'))
print('-=' * 10)

computador = randint(0,10)
jogador = int(input('Diga um valor: '))
soma = computador + jogador
par_impar = str(input('Par ou Ímpar? [P/I]').upper())
vitorias = 0

while True:
    if soma % 2 == 0 and par_impar == 'P' or soma % 2 != 0 and par_impar == 'I':    
        print('-' * 30)
        print('Você VENCEU!!')
        print('Vamos jogar novamente...')
        print('-' * 30)
        vitorias += 1
        jogador = int(input('Diga um valor: '))
        par_impar = str(input('Par ou Ímpar? [P/I]').upper())
        computador = randint(0,10)
        soma = computador + jogador
    else:
        break
print('-=' * 10)
print('Você PERDEU!')
print('-=' * 30)
print(f'Você jogou {jogador} e o computador jogou {computador}. Total de {soma} DEU PAR' if soma % 2 == 0  else f'Você jogou {jogador} e o computador jogou {computador}. Total de {soma} DEU IMPAR' )
print(f'GAME OVER! Você venceu {vitorias} vezes.')