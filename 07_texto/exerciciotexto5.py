frase = input('Digite uma frase: ')

frase = frase.upper().strip()

print(f'A letra "a" aparece {frase.count('A')} vezes')

primeiro = frase.find('A')+1

print(f'A primeira letra "a" aparece na posição {primeiro}')

ultimo = frase.rfind('A')+1

print(f'A última letra "a" aparece na posição {ultimo}')