termo = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))

contador = 0
total = 0

mais = int(input('Quantos termos você quer ver do seu número? '))

while mais != 0:
    total += mais
    while contador < total:
        resultado = termo + contador * razao 
        contador = contador + 1
        print(resultado, end=' -> ')
    print('PAUSA')
    mais = int(input('\nQuer ver mais quantos termos do seu número? [0 para sair!] '))
print(f'Progressão finalizada com {total} termos')