from time import sleep

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
print('-=' * 10)

opcao = 0

while opcao != 5:
    sleep(1)
    opcao = int(input('''O que deseja fazer com so 2 valores?
    [1] - Somar
    [2] - Multiplicar
    [3] - Maior
    [4] - Novos números
    [5] - Sair do programa
    OPCÃO: '''))
    print('-=' * 10)
    sleep(1)
    if opcao == 1:
        soma = n1 + n2
        print(f'Soma : {n1} + {n2} = {soma}')
        print('-=' * 10)
    elif opcao == 2:
        multi = n1 * n2
        print(f'Multiplicação : {n1} * {n2} = {multi}')
        print('-=' * 10)
    elif opcao == 3:
        maior = max(n1, n2)
        if n1 == n2:
            print('Os números tem o mesmo valor!')
            print('-=' * 10)
        else:
            print(f'O maior número entre {n1} e {n2} é: {maior}')
            print('-=' * 10)
    elif opcao == 4:
        n1 = int(input('Digite um novo valor para n1: '))
        n2 = int(input('Digite um novo valor para n2: '))
        print('Valores atualizados!')
        print('-=' * 10)
    elif opcao == 5:
        break
    else:
        print('Opção Invalida.')
print('Programa finalizado!')
