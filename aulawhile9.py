continua = 'S'
contador = 0
soma = 0
maior = 0
menor = float('inf')

while continua != 'N':

    n = int(input('Digite um valor: '))

    contador += 1
    soma += n

    if n > maior:
        maior = n
    if n < menor:
        menor = n

    resultado = str(input('Deseja ver o resultado? (S/N)').upper())

    if resultado == 'S':
        media = soma / contador

        print(f'Números digitados: {contador}')
        print(f'Média dos números: {media:.2f}')
        print(f'A soma de todos eles é: {soma}')

        if maior == menor:
            print(f'O maior e o menor números são iguais: {maior}')
        else:
            print(f'O maior número é: {maior}')
            print(f'O menor número é: {menor}')
        
        continua = str(input('Deseja continuar digitando valores? (S/N)').upper())

print('Programa finalizado.')