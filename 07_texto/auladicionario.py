# Declarar

dados = dict()
dados = {'nome': 'Pedro', 'idade':25}

print(dados['nome'])
print(dados['idade'])

# Adicionar elemento ## NÃO UTILIZA APPEND()

dados['sexo'] = 'M'

# Remover elemento

del dados['idade']

# Exemplo

filmes = {'titulo': 'Star Wars',
         'ano': 1977,
         'diretos': 'George Lucas'
        }

print(filmes.values()) # <- Vai printar apenas os valores, como Star Wars, 1977, e George Lucas
print(filmes.keys()) # <- Vai printar as chaves, como titulo, ano, diretor
print(filmes.items()) # <- Vai printar os dois, tantos os valores quanto as chaves

# Outro exemplo

for k, v in filmes.items():
    print(f'O {k} é {v}')


# Prática

pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(pessoas['idade'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

for k in pessoas.keys():
    print(k)

for k in pessoas.values():
    print(k)

for k, v in pessoas.items():
    print(f'{k} + {v}')

# Apagando elemento
del pessoas['sexo']

# Alterando elemento
pessoas['nome'] = 'Leandro'

# Adicionando elemento
pessoas['peso'] = 98.5

# IMPORTANTE! CRIAR DICIONÁDIO DENTRO DE UMA LISTA
"""
brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'Espirito Santo', 'sigla': 'ES'}
brasil.append(estado1)
brasil.append(estado2)

print(brasil)
print(brasil[0])
print(brasil[1])
print(brasil[0]['uf'])
print(brasil[1]['sigla'])
"""
estado = dict()
brasil = list()

for c in range(3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy()) # <- Ele não funciona somento adicionando dentro da lista, nem se você tentar copiar com [:], para isso é necessário utilizar o copy()

for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}')

for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()
