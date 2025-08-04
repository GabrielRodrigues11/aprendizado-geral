from time import sleep

def maior(*num):
    print('-=' * 25)
    print('Analistando os valores Passados...')
    sleep(1.2)

    total = 0
    maior = 0

    for valor in num:
        total += 1
        print(f'{valor}', end = ' ',flush=True)
        sleep(0.5)

        if valor > maior:
            maior = valor

    print(f'Foram informados {total} valores ao todo.')  
    sleep(0.5)
    print(f'O maior valor informado foi o {maior}.')    
    sleep(0.5)
           
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()