def ficha(jogador, gols):
    print(f'O jogador {jogador} fez {gols} gol(s) no campeonato')

j = str(input('Digite o nome do seu jogador: '))
g = input('Quantos gols ele fez? ')

if j.strip() == '':
    j = '<desconhecido>'
if g.isnumeric():
    g = int(g)
else:
    g = 0

ficha(j,g)



