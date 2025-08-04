from time import sleep

num = int(input('Digite o número para ver sua tabuada: '))
print('-=' * 10)
for c in range(0,11):
    print(f'{num} x {c} = {num * c}')
    sleep(0.2)
print('-=' * 10)
print('fim')
