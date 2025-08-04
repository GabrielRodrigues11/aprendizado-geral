nota1 = float(input('Qual foi sua nota da primeira prova? '))
nota2 = float(input('Qual foi sua nota da segunda prova? '))

media = (nota1 + nota2) / 2

if media < 5:
    print(f'Média: {media} -- Aluno reprovado!')
elif media <= 6.9:
    print(f'Média: {media} -- Aluno de recuperação!')
else:
    print(f'Média: {media} -- Aluno aprovado!')