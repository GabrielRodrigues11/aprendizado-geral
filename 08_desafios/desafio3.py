# calculando fatorial

def fatorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado
    
n = int(input("Digite um número para calcular o fatorial: "))

print(fatorial(n))


# Método mais fácil e útil

import math

num = int(input("Agora digite um número para fazer com o import math: "))

print(f"O fatorial de {num} é {math.factorial(num)}")
