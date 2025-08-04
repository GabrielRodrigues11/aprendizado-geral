tupla = ()

# ADICIONANDO NÚMEROS UTILIZANDO TUPLA += (n, )
for c in range(4):
    n = int(input('Digite um numero: '))
    tupla += (n, )
 
# ADICIONANDO NÚMEROS NA TUPLA DE FORMA MAIS SIMPLE
"""
tupla = (int(input('Digite um número: ')),
         int(input('Digite um segundo número: )),
         int(input('Digite um terceiro número: )),
         int(input('Digite um quarto número: )))
"""
print(f'Você digitou os valores: {tupla}')    

# Quantas vezes o 9 aparece
print(f'O número 9 aparece {tupla.count(9)} vezes.')

# Em que posição foi digitado o primeiro 3
if 3 in tupla:
    print(f'O primeiro 3 foi digitado na posição {tupla.index(3)}.')
else:
    print('O número 3 não foi digitado.')

# Quais foram os números pares.

# MODO 1
pares = ()
for c in tupla:
    if c % 2 == 0:
        pares += (c, )
# MODO 2
"""pares = tuple(x for x in tupla if x % 2 == 0)"""

print(f'Os números pares digitados foram: {pares}')