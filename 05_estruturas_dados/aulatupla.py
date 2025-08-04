lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim','Refrigerante', 'Batata frita')

# Tuplas são imutáveis
# lanche[1] = "Refrigerante" <- ERRADO!

# 1 - MANEIRA SIMPLES (SEM POSIÇÃO)
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba!')

# 2 - MANEIRA COM POSIÇÃO UTILIZANDO RANGE()
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
print('Comi pra caramba!')

# 3 - MANEIRA COM POSIÇÃO UTILIZANDO ENUMARATE
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
print('Comi pra caramba!')


# EM ORDEM <- ELE TRANSFORMA A TUPLA EM UMA LISTA

print(sorted(lanche))

# OUTRAS TUPLAS COM INT

a = (2, 5, 4)
b = (5,8,1,2)

c = b + a

print(c)

# MOSTRA A POSIÇÃO
print(c.index(5))

#MOSTRA POSIÇÃO COM DESLOCAMENTO
print(c.index(5, 1))

# DADOS DE TIPOS DIFERENTES EM TUPLAS
pessoa = 'Gustavo', 39, 'M', 99.88
print(pessoa)

# APAGAR TUPLA <- É POSSIVEL APAGAR SOMENTE A TUPLA INTEIRA!! NÃO É POSSIVEL APAGAR SOMENTE UM ELEMENTO DA TUPLA
del(pessoa)
print(pessoa)
