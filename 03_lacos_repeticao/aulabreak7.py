print('=' * 20)
print('BANCO CEV')
print('=' * 20)

valor = int(input('Que valor você quer sacar? '))

cedula_50 = cedula_20 = cedula_10 = cedula_1 = 0

while True:
    # 50
    if valor >= 50:
        cedula_50 += 1
        valor -= 50
    # 20
    elif valor >= 20:
        cedula_20 += 1
        valor -= 20
    # 10
    elif valor >= 10:
        cedula_10 += 1
        valor -= 10
    # 1
    elif valor >= 1:
        cedula_1 += 1
        valor -= 1
    else:
        break

print('=' * 20)
print(f'Total de {cedula_50} cédulas de R$50')
print(f'Total de {cedula_20} cédulas de R$20')
print(f'Total de {cedula_10} cédulas de R$10')
print(f'Total de {cedula_1} cédulas de R$1')