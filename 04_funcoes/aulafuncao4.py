from time import sleep

def contagem(i,f,p):
    print('-=' * 20)

    if p == 0:
        p = 1
    p = abs(p)

    print(f'Contagem de {i} até {f} de {abs(p) if p != 0 else 1} em {abs(p) if p != 0 else 1}')

    if i < f:
        for c in range(i, f + 1, p):
            print(c, end = ' ', flush=True)
            sleep(0.3)
    else:
        for c in range(i, f - 1, -p):
            print(c, end = ' ', flush=True)
            sleep(0.3)
    print('FIM!')

contagem(1, 10, 1)
contagem(10,1,2)

inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

contagem(inicio,fim,passo)