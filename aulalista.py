num = [2,5,6,1]

# ALTERAR VALOR
num[2] = 3

# ADICIONAR VALOR
num.append(7)

# COLOCAR EM ORDEM CRESCENTE
num.sort()

# COLOCAR EM ORDEM DECRESCENTE
num.sort(reverse=True)

# CONTAR VALORES DA LISTA
len(num)

# INSERIR VALORES EM POSIÇÃO ESPECIFICA (não pode ser em uma nova posição)
num.insert(2, 2)

# REMOÇÃO DE ELEMENTOS
# num.pop(2) -> ELIMINA O VALOR NA POSIÇÃO QUE VOCE ESPECIFICOU
"""num.pop(2)"""

# num.remove() -> Faz uma varredura e elimina o primeiro valor da esquerda para direita
"""num.remove(4)"""

if 4 in num:
    num.remove(4)
else:
    print('Não achei o número 4')

print(num)

# VER VALORES COM FOR

valores = []
valores.append(5)
valores.append(7)
valores.append(9)

# 1º maneira
for v in valores:
    print(f'{v}...', end='')
# 2º maneira
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}')
print('Cheguei ao final da lista.')

# ADICIONANDO VALORES COM FOR

valores2 = []

for cont in range(0,5):
    valores2.append(int(input('Digite um valor: ')))
print(valores2)


a = [2,3,6,7]

# b = a                # <- AO IGUALAR UMA LISTA VOCÊ NÃO ESTÁ FAZENDO UMA CÓPIA, E SIM UMA LIGAÇÃO 
# b[2] = 8             # <- AQUI POR EXEMPLO, O 8 DEVERIA  SER INSERIDO APENAS NO B, CERTO? MAS COMO VOCE IGUALOU, ELE SERÁ ALTERADO EM AMBAS AS LISTAS

# b = a[:]             # <- PARA RESOLVER ISSO, DEVE SER FEITO DESSA MANEIRA: b = a[:]   ASSIM ELE CRIARÁ UMA CÓPIA DE A NO B, SEM EXISTIR LIGAÇÕES NENHUMA

b = a 
b = a[:] 

print(f'Lista A: {a}')
print(f'Lista B: {b}')