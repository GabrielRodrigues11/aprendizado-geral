num = ('Zero','Um','Dois','Tres','Quatro','Cinco','Seis','Sete','Oito','Nove','Dez',
'Onze','Doze','Treze','Quatorze','Quinze','Dezeseis','Dezesete','Dezoito','Dezenove','Vinte')

n = (int(input('Digite um número de 0 a 20: ')))
while True: 
    if 0 <= n <= 20:
        print(f'O número que você digitou foi o {num[n]}')
        break
    else:
        n = (int(input('Tente novamente. Digite um número de 1 a 20: ')))
print('Operação finalizada')
