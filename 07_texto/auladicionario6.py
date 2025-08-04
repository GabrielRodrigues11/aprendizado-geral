lista = list()
mulheres = list()
maior_que_media = list()

total_pessoas = 0
total_idade = 0
continua = 'S'
media = 0

while True:
    usuario = {}

    usuario['nome'] = str(input('Nome: '))

    while True:
        sexo = input('Sexo: [M/F] ').strip().upper()
        if sexo in ['M', 'F']:
            usuario['sexo'] = sexo 
            break
        print('ERRO! Por favor, responda apenas M ou F')

    usuario['idade'] = int(input('Idade: '))

    lista.append(usuario.copy())

    # Total de pessoas cadastradas
    total_pessoas += 1

    # Média de idade
    total_idade += usuario['idade']
   

    # Lista com todas as mulheres
    if usuario['sexo'] == 'F':
        mulheres.append(usuario.copy())

    while True:
        continua = str(input('Deseja continuar? [S/N]').upper())
        if continua in ['S', 'N']:
                break
        print('ERRO! Por favor, responda apenas S ou N.')

    if continua == 'N':
        break

media = total_idade / total_pessoas
         
print('-=' * 20)

# Lista com os com idade maior que a média
for v in lista: 
    if v['idade'] > media:
        maior_que_media.append(v)

print(f' - O grupo tem {total_pessoas} pessoas.')
print(f' - A média de idade é de {media:.2f} anos.')
print(f' - As mulheres cadastradas foram: ', end = '')

# print(f' - As mulheres cadastradas foram: {", ".join([m["nome"] for m in mulheres])}', end = '') <- modo mais bonito de fazer

for c in mulheres:
    print(f'{c['nome']}', end=' ')
print('')

print(f' - Lista das pessoas que estão acima da média: ')

for c in maior_que_media:
    print(f'nome = {c['nome']}; sexo = {c['sexo']}; idade = {c['idade']}')