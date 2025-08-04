while True:
    try:
        inteiro = int(input('Digite um inteiro: '))
        break
    except KeyboardInterrupt:
        print('Usuário preferiu não digitar esse número.')
        inteiro = 0
        break
    except:
        print('ERRO: por favor, digite um número inteiro válido.')
while True:
    try:
        real = float(input('Digite um número real: '))
        break
    except KeyboardInterrupt:
        print('Usuário preferiu não digitar esse número.')
        real = 0
        break
    except:
        print('ERRO: por favor, digite um número real válido.')

print(f'O valor inteiro digitado foi {inteiro} e o real foi {real}')