km = int(input('A quantos km você está passando pelo radar? '))

multa = (km - 80) * 7

if km > 80:
    print(f'Você foi multado em R${multa} por estar acima da velocidade permitida!')
else:
    print('Parabéns! Você está no limite de velocidade permitida!')