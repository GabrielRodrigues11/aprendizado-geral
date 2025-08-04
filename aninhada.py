casa = float(input('Qual o valor da casa que pretende comprar? '))

salario = float(input('Qual o seu salário? '))

anos = int(input('Em quantos anos você irá pagar?'))

prestacao = casa / (anos * 12)

if prestacao > salario * 0.30:
    print(f'A prestação foi negada pois a prestação de R${prestacao:.2f} é maior que 30% do seu salário')
else:
    print(f'Compra aprovada, você pagará R${prestacao:.2f} por mês durante {anos} anos até completar o valor de R${casa}')
