# Modos de ver as documentações de funções

print(input.__doc__)    # Modo 1
help(input)             # Modo 2

# DOCSTRINGS <- Strings de documentação

def contador(i,f,p):    # A docstring entra na linha do comando def, e basta abrir 3 aspas duplas, assim como é feito no comentário
    """
    -> Faz uma contagem e mostra na tela.
    :param i: Início da contagem
    :param f: Fim da contagem
    :param p: Passo da contagem
    :return: Sem retorno
    Função criada por Gabriel Rodrigues, Dev Python.
    """
    c = i
    while c <= f:
        print(f'{c}', end='..')
        c+=p
    print('FIM!')

help(contador)


# PARÂMETROS OPCIONAIS <- Algumas funções podem receber vários parâmetros, mas alguns deles não são obrigatórios...
# Um exemplo de parâmetros opcionais é o "end".
def somar(a=0,b=0,c=0):       # Para resolver isso basta colocar no po parâmetro =0 no final.
                              # Assim quando a função é chamada e o parâmetro nao é preenchido ele já vai ter um valor.
    s = a + b + c
    print(f'A soma vale {s}')

somar(3,2,5)        # Exemplo de parâmetros preenchidos
somar(8,4)             # Exemplo de parâmetros NÃO preenchidos
somar(8)                     # Exemplo de parâmetros NÃO preenchidos
somar()                      # Exemplo de parâmetros NÃO preenchidos


# ESCOPO DE VARIÁVEIS <- É o local onde a variável vai existir, e onde a variável não vai mais existir.

def teste():
    x = 8
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')
# Programa principal
n = 2
print(f'No programa principal, n vale {n}')
teste()
"""print(f'No programa principal, x vale {x}')"""

# Nesse exemplo o n tem escopo global, pois foi declarada fora da função, onde pode ser usada globalmente.
# Enquanto o x, tem o escopo local, pois, ela foi declarada dentro da função teste()

# Outro Exemplo
# Utilizando o "Global" dentro fanção, o escopo que antes era local (dentro da função) passa a valer
# Global também, no exemplo abaixo o a global vale 5, e o a dentro da função vale 8
# Ao utilizar o Global dentro da função, o a global passa a ser o de dentro da função, que no caso é o 8.
def funcao():
    n1 = 4
    print(f'N1 dentro vale {n1}')

n1 = 2
funcao()
print(f'N1 Fora vale {n1}')

def teste(b):
    global a
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')

a = 5
teste(a)
print(f'A fora vale {a}')


# RETORNANDO VALORES

def somar2(a=0, b=0, c=0):
    s = a + b + c
    return s

print(somar2(3,2,5))
# OU
r1 = somar2(3,2,5)
r2 = somar2(2,2)
r3 = somar2(6)
print(f'Meus cálculos deram {r1}, {r2}, {r3}')


# PARTE PRÁTICA

# Parte 1
def fatorial(num = 1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

n = int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são: {f1}, {f2}, {f3}')

# Parte 2

def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False

num = int(input('Digite um número: '))
if par(num):
    print('É par!')
else:
    print('Não é par!')