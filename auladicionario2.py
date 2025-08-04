aluno = dict()

aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno['nome']}: '))

if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado'
else:
    aluno['situacao'] = 'reprovado'

for c, v in aluno.items():
    print(f'O {c} é igual a {v}')
    
print(aluno)

