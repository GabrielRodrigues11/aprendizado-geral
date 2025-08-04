from random import sample
from time import sleep

jogos = list()

print('-' * 15)
print('JOGO NA MEGA SENA')
print('-' * 15)


num = int(input('Quantos jogos você quer que eu sorteie? '))

print(f'-=-=-= SORTEANDO {num} JOGOS -=-=-=')

for n in range(num):
    numeros = sample(range(1, 61), 6)
    numeros.sort()
    jogos.append([numeros])
    sleep(1)
    print(f'Jogos {n + 1}: {jogos[n]}')
sleep(1)
print('-=-=-=-= < BOA SORTE > -=-=-=-=')
