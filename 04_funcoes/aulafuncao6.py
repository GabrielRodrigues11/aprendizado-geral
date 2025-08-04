from random import randint
from time import sleep

def sorteia(lista):
    for c in range(5):
        lista.append(randint(1,10))

    print(f'Sorteando 5 valores da lista: ', end='')
    for num in lista:
        sleep(0.5)
        print(f'{num}', end=' ', flush=True)
    print('PRONTO!')

def soma_par(lista):
    soma = 0
    for num in lista:
        if num % 2 == 0:
            soma += num
    print(f'Somando os valores pares de {lista}, temos {soma}')

numeros = []
sorteia(numeros)
soma_par(numeros)
