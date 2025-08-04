soma_idade = 0
homem_velho = ''
idade_mais_velho = 0
mulheres_menos_20 = 0

for c in range(1,5):
    print(f'----- {c}ª PESSOA -----')
    nome = str(input(f'Nome: '))
    idade = int(input(f'idade: '))
    sexo = str(input(f'Sexo (M/F): ')).lower()
    
    soma_idade += idade

    if sexo == 'm' and idade > idade_mais_velho:
        idade_mais_velho = idade
        homem_velho = nome

    if sexo == 'f' and idade < 20:
        mulheres_menos_20 += 1

media_idade = soma_idade / 4

print(f'A média de idade do grupo é {media_idade}')
print(f'O homem mais velho do grupo é o {homem_velho} com a idade de {idade_mais_velho}')
print(f'O número de mulheres com menos de 20 anos é de {mulheres_menos_20}')

