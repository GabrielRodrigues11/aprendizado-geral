# CRIAR UMA TUPLA COM VÁRIAS PALAVRAS ALEATORIAS DEPOIS MOSTRAR PARA CADA PALAVRA QUAIS SAO SUAS VOGAIS

palavras = ("Computador", "Programacao", "Python", "Algoritmo", "Dados", 
            "Inteligencia", "Artificial", "Rede", "Neural", "Aprendizado")

vogais = "aAeEiIoOuU"

for p in palavras:
    print(f'\nNa palavra {p.upper()} temoas as vogais: ', end = '')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end = ' ')