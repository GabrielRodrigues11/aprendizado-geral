from random import randint
from time import sleep
from operator import itemgetter

jogo = dict()

print('VALORES SORTEADOS ')
sleep(0.5)

for c in range(4):
    sleep(1)
    dado = randint(1,6)
    jogo[f'jogador{c + 1}'] = dado
    print(f'O Jogador {c + 1} tirou {dado} no dado.')

sleep(1)
print('RANKING DOS JOGADORES')
sleep(1)

ranking = list()
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

for i, v in enumerate(ranking):
    print(f'O {i + 1}º Lugar: {v[0]} com {v[1]}.')
    sleep(1)

print(jogo)