times = ('Fortaleza','Juventude','Vasco da Gama','Cruzeiro','Grêmio','Corinthians','Flamengo','Internacional','Bahia',
         'São Paulo','Sport Recife','Botafogo','Palmeiras','Ceará SC','Bragantino','Atletico-MG','Santos','Mirassol',
         'Fluminense','EC Vitória')

print('-=' * 10)
print(f'Lista de times do Brasileirao: {times}')
print('-=' * 10)

# 5 Primeiros
for c in range(0,5):
    print(f'{c + 1}ª {times[c]}')
print(f'Os 5 primeiros são :{times[0:5]}')

print('-=' * 10)

# 4 Últimos
for c in range(len(times) - 4, len(times)):
    print(f'{c + 1}ª {times[c]}')
print(f'Os 4 últimos são:{times[-4:]}')
    
print('-=' * 10)

# Times em ordem alfabética
print(f'Os times em ordem alfabética: {sorted(times)}')
    
print('-=' * 10)

# Posição do Botafogo na tabela
print(f'O Botafogo está na {times.index('Botafogo') + 1}ª posição')