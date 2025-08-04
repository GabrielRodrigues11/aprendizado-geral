jogadores = list()
continua = 'S'

while True:
    # Cria o jogador
    jogador = dict()
    jogador['nome'] = str(input('Nome do jogador: '))
    jogador['partidas'] = int(input(f'Quantas partidas {jogador['nome']} jogou? '))
    
    gols = list()
    total = 0
    for c in range(jogador['partidas']):
        gol = int(input(f'Quantos gols na partida {c + 1}? '))
        gols.append(gol)
        total += gol

    jogador['gols'] = gols
    jogador['total'] = total

    # Adiciona o jogador na lista de jogadores
    jogadores.append(jogador.copy())

    # Zera os dados
    del gols
    total = 0

    continua = str(input('Deseja continuar? [S/N] ').upper())
    if continua == 'N':
        break

print('-=' * 15)
print(f'{"Cod":<5} {"nome":<5} {"gols":>5} {"total":>10}')
print('-' * 40)

for c, v in enumerate(jogadores):
    print(f'{c} {v['nome']:<10} {v['gols']} {v['total']:>5}')

codigo = 0
while True:
    codigo = int(input('Mostrar dados de qual jogador? '))
    if codigo == 999:
         break

    print(f'LEVANTAMENTO DO JOGADOR {jogadores[codigo]['nome']}')

    for c in range(jogadores[codigo]['partidas']):
            print(f'No jogo {c + 1} fez {jogadores[codigo]['gols'][c]} gols.')
print('Analise finalizada')