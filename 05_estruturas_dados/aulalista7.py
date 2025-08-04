expressao = str(input('Digite sua expressão: '))
expressao = expressao.strip()
expressao_list = list(expressao)

contador_parenteses_aberto = 0
contador_parenteses_fechado = 0

for letra in expressao_list:
    if letra == '(':
        contador_parenteses_aberto += 1
    
    if letra == ')':
        contador_parenteses_fechado += 1
        
if contador_parenteses_aberto == contador_parenteses_fechado:
    print('Expressão CORRETA!')
else:
    print('Expressão ERRADA!')