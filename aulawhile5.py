numero = int(input("Digite um número: "))

fatorial = 1
contador = numero

print(f'Calculando {numero}! = ', end='')

while contador > 1:
    print(f'{contador}', end='')
    print(f' x ' if contador > 1 else ' = ', end='')
    fatorial *= contador
    contador -= 1
print(f'{fatorial}')
