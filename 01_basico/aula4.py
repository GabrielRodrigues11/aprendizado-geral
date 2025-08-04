# Desafio 1
n = int(input('Digite um número: '))

sucessor = n + 1
antecessor = n - 1
dobro = n * 2
triplo = n * 3
raiz_quadrada = n * n

print(f'O sucessor de {n} é {sucessor}\n'
      f'O antecessor de {n} é {antecessor}\n'
      f'O dobro de {n} é {dobro}\n'
      f'O triplo de {n} é {triplo}\n'
      f'A raiz quadrada de {n} é {raiz_quadrada}\n')

# Desafio 2
nota = float(input('Digite a nota da prova 1 do aluno: '))
nota1 = float(input('Digite a nota da prova 2 do aluno: '))

media = (nota + nota1) / 2

print(f'A média do aluno é {media}\n')

# Desafio 3
metro = float(input('Digite uma distância em metros: '))

centimetros = metro * 100
milimetro = metro * 1000

print(f'{metro}m tem {centimetros}cm e {milimetro}mm\n')

# Desafio 4
num = float(input('Digite um número para ver sua tabuada: '))

resultado = 0

for i in range(1, 11):
    resultado = num * i
    print(f"{num} x {i} = {resultado}")

    
# Desafio 5
reais = float(input('Quantos R$ você tem na carteira? '))

dolares = reais / 5.75
print(f'Com R${reais} você pode comprar US${dolares:.1f}\n')

# Desafio 6
largura = float(input('Largura da parede? '))
altura = float(input('Altura da parede? '))

area = altura * largura
pintura = area / 2

print(f'Uma parede que tem {altura} metros de altura e {largura} metros de largura\n'
      f'tem a área de {area}m², o que gastaria cerca de {pintura}L de tinta\n')

# Desafio 6
preco = float(input('Qual o preço do produto? '))

promo = 5
desconto = preco - (preco * promo / 100)

print(f'Este produto está com uma promoção de {promo}% e o preço dele fica de R${preco}, por R${desconto}!\n')

# Desafio 6
salario = float(input('Digite seu salário: '))

aumento = salario + (salario * 15 / 100)


print(f'Com o aumento de 15% seu salário aumenta de R${salario} para R${aumento:.1f}!')