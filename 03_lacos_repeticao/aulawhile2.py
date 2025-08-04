"""
while sexo == 'M' or sexo == 'F':
    sexo = str(input('Digite seu sexo: [M/F]').upper())
    if sexo != 'M' and sexo != 'F':
        while sexo != 'M' and sexo != 'F':
            print('O sexo deve ser Masculino (M) ou Feminino (F).')
            sexo = str(input('Tente novamente: (M/F)'))
        break
    print('Continuando...')
print('Ok, tudo certo!')"
"""


sexo = str(input('Digite seu sexo: (M/F)').upper())

while sexo not in 'MmFf':
    print('Errado! Seu sexo deve ser MASCULINO(M) OU FEMININO(F)!! TENTE NOVAMENTE!')
    sexo = str(input('Digite seu sexo: (M/F)').upper())
print('Agora sim, pode prosseguir... Baitola.')
