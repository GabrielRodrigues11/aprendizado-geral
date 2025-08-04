alunos = list()
continua = "S"
opcao = 0

while True:
    nome = str(input('Nome: '))
    nota1 = int(input('Nota 1: '))
    nota2 = int(input('Nota 2: '))
    alunos.append([nome, [nota1, nota2]])
    continua = str(input('Deseja continuar? [S/N]')).upper()
    if continua == "N":
        break

print('-=' * 20)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 30)

for pos, n in enumerate(alunos):
    media = (alunos[pos][1][0] + alunos[pos][1][1]) / 2
    print(f'{pos:<3} {alunos[pos][0]: <10} {media:>5}')
print('-' * 30)

while True:
    opcao = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opcao == 999:
        break
    print(f'Notas de {alunos[opcao][0]} são {alunos[opcao][1]} ')

print('Programa finalizado')