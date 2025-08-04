a = int(input('Digite um número qualquer: '))
b = int(input('Digite outro número qualquer: '))

if a > b:
    print(f'O número {a} é maior que o número {b}')
elif b > a:
    print(f'O número {b} é maior que o número {a}')
else:
    print(f'O número {a} e o número {b} são iguais')