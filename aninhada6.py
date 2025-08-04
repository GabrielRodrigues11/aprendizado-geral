from datetime import date

ano = int(input('Qual seu ano de nascimento? '))

idade = date.today().year - ano

if idade <= 9:
    print(f'{idade} anos --- Categoria MIRIM')
elif idade <= 14:
    print(f'{idade} anos --- Categoria INFANTIL')
elif idade <= 19:
    print(f'{idade} anos --- Categoria JUNIOR')
elif idade <= 20:
    print(f'{idade} anos --- Categoria SÊNIOR')
else:
    print(f'{idade} anos --- Categoria MASTER')

