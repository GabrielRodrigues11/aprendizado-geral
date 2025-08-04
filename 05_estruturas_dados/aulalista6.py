valores = []
impares = []
pares = []
continua = 'S'

while True:
    num = int(input('Digite um valor: '))
    valores.append(num)
    continua = str(input('Deseja continuar? [S/N]').upper())
    if continua == 'N':
        break
    
for n, v in valores:
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
    
print(f'A lista completa é {valores}')
print(f'A lista de pares é {pares}')
print(f'A lista de impares é {impares}')

# Modo mais "simples"
"""        
while True:
    num = int(input('Digite um valor: '))
    valores.append(num)
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
    continua = str(input('Deseja continuar? [S/N]').upper())
    if continua == 'N':
        break
"""