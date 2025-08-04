def ajuda():
    from time import sleep
    while True:
        sleep(1)
        print('\033[1;34m' + '~~' * 20)
        print('SISTEMA DE AJUDA PyHELP')
        print('~~' * 20 + '\033[m')

        palavra = str(input('\033[1;33mFunção ou Biblioteca: \033[m'))

        if palavra.lower() == 'fim':
                print('\033[1;35mATÉ LOGO!\033[m')
                break

        sleep(1)
        print('\033[1;35m' + '~~' * 20)
        print(f'Acessando o manual do comando {palavra}')
        print('~~' * 20 + '\033[m')

        sleep(1)
        print('\033[0;30;42m')
        help(palavra)
        print('\033[m')

ajuda()