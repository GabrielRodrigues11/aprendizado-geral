def calcular_area(l, c):
    a = l * c
    print(f'A área de um terreno {l}x{c} é de {a}m²')


# Programa principal
print('Controle de terrenos')
print('-' * 20)
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))

calcular_area(largura,comprimento)


