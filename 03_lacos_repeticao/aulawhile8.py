n = int(input('Digite um número: '))
contador = 0
soma = 0

while n != 999:
    contador += 1
    soma = soma + n
    n = int(input('Digite um número: '))
print('Fim')
print(f'Você digitou {contador} números e a soma de todos eles é: {soma}')