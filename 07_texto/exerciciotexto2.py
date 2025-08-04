num = input('Digite um número de 0 a 9999: ')

num = num.zfill(4)

unidade = num[3]
dezena = num[2]
centena = num[1]
milhar = num[0]

print(f'Unidade: {unidade}')
print(f'Dezena: {dezena}')
print(f'Centena: {centena}')
print(f'Milhar: {milhar}')