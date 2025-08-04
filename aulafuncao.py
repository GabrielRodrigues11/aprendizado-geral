# INICIO
def título(txt):
    print('-' * 30)
    print(txt)
    print('-' * 30)


# Programa Principal     O programa principal deve sempre ficar a 2 linhas abaixo da função por questões esteticas

título('CURSO EM VIDEO')
título('PYTHON É MUITO BOM!')

# PRÁTICA SIMPLES

# As funções servem principalmente para fugir de rotinas, evitar ficar repetindo códigos desnecessários, encurtar seu código e facilitar sua vida

def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de A + B = {s}')


soma(4, 5)
soma(8, 9)
soma(2, 1)
soma(a=4, b=5)
soma(b=8, a=2)

# EMPACOTAMENTO # <- PODE COLOCAR QUANTOS NUMEROS QUISER COMO PARAMETROS

def contador(*num):  # <- o *num garante que você pode colocar quantos numeros quiser como parametros
    for valor in num:
        print(f'{valor} ', end='')
    print('FIM!')
    
    tam = len(num)
    print(f'Recebi os valores {num} e no total foram {tam} números')


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)      # <- Ele retorna tuplas com os valores passados


def soma2(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')


soma2(5, 2)
soma2(2, 9, 4)


# FUNÇÃO COM LISTAS

def dobra(lst): 
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)

