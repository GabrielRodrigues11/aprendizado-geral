soma = 0
cont= 0
for num in range(0,501):
    if num % 2 != 0 and num % 3 == 0:
        soma += num
        cont += 1
print(f'A soma de todos os {cont} valores solicitados é: {soma}')