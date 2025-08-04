"""
continua = 'S'

while continua = 'S':
    texto = str(input('Digite alguma frase ou palavra que desejar: '))
    tamanho = len(texto)

    def escreva(texto, tamanho):
        print('~' * tamanho)
        print(texto)
        print('~' * tamanho)

    escreva(texto, tamanho)

    continua = str(input('Deseja continuar? [S/N] ').upper())
    if continua == 'N':
        break

print('Finalizado...')
"""
# TESTE COM VÁRIAS PALAVRAS


def escreva(texto,tamanho = None):
    tamanho = len(texto) + 4
    print('~' * tamanho)
    print(f'  {texto}')
    print('~' * tamanho)

escreva('Gustavo guanabara')
escreva('Curso de Python no Youtube')
escreva('CeV')

