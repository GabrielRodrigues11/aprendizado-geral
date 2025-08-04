salario = float(input('Digite o valor do seu salário: '))

if salario <= 1250:
    aumento = salario + (salario * 15 / 100)
    print(f'Você recebeu um aumento de 15% e seu salário aumentou de R${salario} para R${aumento}')
else:
    aumento = salario + (salario * 10 / 100)
    print(f'Você recebeu um aumento de 10% e seu salário aumentou de R${salario} para R${aumento}')