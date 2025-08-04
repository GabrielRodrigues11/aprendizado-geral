from datetime import date

usuario = dict()

usuario['nome'] = str(input('Nome: '))
ano_nasc = int(input('Ano de nascimento: '))
usuario['cpts'] = int(input('Cardeira de trabalho (0 não tem): '))
if usuario['cpts'] != 0: 
    usuario['contratação'] = int(input('Ano de contratação: '))
    usuario['salário'] = int(input('Salário: R$'))
    usuario['idade'] = date.today().year - ano_nasc
    usuario['aposentadoria'] = usuario['idade'] + ((usuario['contratação'] + 35) - date.today().year)
    print('-=' * 20)

    

    for v, c in usuario.items():
        print(f'O {v} tem o valor {c}')
    
else:
    usuario['idade'] = date.today().year - ano_nasc

    for v, c in usuario.items():
        print(f' - {v} tem o valor {c}')

print(usuario)