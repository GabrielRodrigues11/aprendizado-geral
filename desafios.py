import math
import random


num1 = float(input('Digite um valor quebrado: '))
inteiro = round(num1)
print(f'O valor inteiro de {num1} é : {inteiro}')

## Catetos
cateto_oposto = float(input('Cateto oposto: '))
cateto_adjacente = float(input('Cateto adjacente: '))
hipotenusa = math.hypot(cateto_oposto, cateto_adjacente)
print(f'A hipotenusa é: {round(hipotenusa, 2)}')


## Angulos
angulo = float(input("Digite um ângulo qualquer (em graus): "))

radianos = math.radians(angulo)

seno = math.sin(radianos)
cosseno = math.cos(radianos)
tangente = math.tan(radianos)

print(f"Seno: {seno:.2f}")
print(f"Cosseno: {cosseno:.2f}")
print(f"Tangente: {tangente:.2f}")

## Sorteio

alunos = ['Gabriel', 'João', 'Henrique', 'Enzo']
escolhido = random.choice(alunos)
print(f'O aluno escolhido para apagar o quadro foi: {escolhido}')
random.shuffle(alunos)
print('A ordem de apresentação sera: ')
print(alunos)



