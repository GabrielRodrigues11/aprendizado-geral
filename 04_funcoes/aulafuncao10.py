def leiaint(msg):
    num = input(msg)
    while not num.isdigit():
        print('\033[1;31mERRO! Digite um número inteiro válido.\033[m')
        num = input(msg)
    return int(num)

n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
