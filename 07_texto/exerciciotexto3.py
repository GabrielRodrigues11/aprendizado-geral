nome = input('Digite o nome da sua cidade: ')

nome = nome.upper().lstrip()

# Resolução 1
print(nome[:5].upper() == "SANTO")


# Resolução 2
"""
if nome.startswith('SANTO'):
    print('O nome da sua cidade começa com SANTO')
else:
    print('O nome da sua cidade não começa com SANTO')
"""