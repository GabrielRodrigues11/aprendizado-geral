jogador = dict() 
gols = list()
total = 0

jogador['nome'] = str(input('Nome do jogador: '))
jogador['partidas'] = int(input(f'Quantas partidas {jogador['nome']} jogou? '))

for c in range(jogador['partidas']):
    gol = int(input(f'Quantos gols na partida {c + 1}? '))
    gols.append(gol)
    total += gol

jogador['gols'] = gols
jogador['total'] = total

print('-=' * 15)
print(jogador)
print('-=' * 15)

for c, v in jogador.items():
    print(f'O campo {c} tem o valor {v}')
print('-=' * 15)

print(f'O jogador {jogador["nome"]} jogou {jogador["partidas"]} partidas.')

for n, v in enumerate(jogador['gols']):
    print(f'=> na partida {n + 1}, fez {v} gols.')
print(f'foi um total de {total} gols')



