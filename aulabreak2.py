n = int(input('Digite um valor: '))
cont = 0
soma = 0

while True:
    if n == 999:
        break
    else:
        cont += 1
        soma += n
        n = int(input('Digite um valor: '))
print(f'A soma dos {cont} valores foi {soma}')

