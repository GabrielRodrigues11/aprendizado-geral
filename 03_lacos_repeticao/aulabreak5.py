masculino = mulher_menos_20 = mais_18 = 0
continua = 'S'

while True:
    print('-' * 20)
    print('CADASTRE UMA PESSOA')
    print('-' * 20)
    idade = int(input('Idade: '))

    if idade > 18:
        mais_18 += 1

    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ').upper())

    if sexo == 'F' and idade < 20:
        mulher_menos_20 += 1
    elif sexo == 'M':
        masculino += 1
    
    print('-' * 20)
    continua = ' '
    while continua not in 'SN': 
        continua = str(input('Quer continuar? [S/N]').upper())

    if continua == 'N':
        break

print('===== FIM DO PROGRAMA =====')
print(f'Total de pessoas com mais de 18 anos: {mais_18}')
print(f'Aoo todo temos {masculino} cadastrados')
print(f'E temos {mulher_menos_20} com menos de 20 anos')