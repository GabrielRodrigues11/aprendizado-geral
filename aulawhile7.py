print('-' * 30)
print('Sequência de Fibonacci')
print('-' * 30)

n = int(input("Quantos termos da sequência de Fibonacci você quer ver? "))

anterior = 0
atual = 1
contador = 0

print('-' * 30)
while contador < n:
    print(anterior, end=' -> ')
    proximo = anterior + atual
    anterior = atual
    atual = proximo
    contador += 1
print('FIM')
print('-=' * 30)