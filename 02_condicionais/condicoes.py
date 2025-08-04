from random import randint

num = randint(5, 5)

n = int(input('Qual número de 0 a 5 estou pensando? '))

if num == n:
    print(f'\033[1;32mParabéns, você acertou! O número é 5!\033[m')
else:
     print(f'\033[1;31mErrou, o número era {num}\033[m')