"""
ano = int(input('Qual o seu ano de nascimento? '))

idade = 2025 - ano

if idade < 18:
    faltam = 18 - idade
    print(f'Faltam {faltam} anos para você se alistar!')
elif idade == 18:
    print(f'Você já tem 18 anos! Está na hora de você se alistar')
else:
    print(f'Você já tem {idade}, já passou da hora de você se alistar!')
"""

from datetime import date

ano = int(input('Qual o seu ano de nascimento? '))
hoje = date.today().year

idade = hoje - ano

if idade < 18:
    faltam = 18 - idade
    print(f'Faltam {faltam} anos para você se alistar!')
elif idade == 18:
    print(f'Você já tem 18 anos! Está na hora de você se alistar.')
else:
    passou = idade - 18
    print(f'Você já tem {idade} anos, já passou {passou} anos da idade de alistamento!')
