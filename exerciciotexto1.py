nome = str(input('Digite seu nome completo: '))

print(f'Seu nome em maiúsculo é: {nome.upper()}')

print(f'Seu nome em minúsculo é: {nome.lower()}')

nome_limpo = ' '.join(nome.split())

print(f'Seu nome tem {len(nome_limpo)} letras')

nome = nome.split()

print(f'Seu primeiro nome tem {len(nome[0])} letras')