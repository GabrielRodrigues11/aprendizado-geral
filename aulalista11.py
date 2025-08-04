matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
contador = 0
soma = 0
soma_3_coluna = 0

for i in range(3):
    for j in range(3):
        matriz[i][j] = int(input(f'Digite um valor para [{i}, {j}]: '))

        if matriz[i][j] % 2 == 0:
            soma += matriz[i][j]   

        if j == 2:
            soma_3_coluna += matriz[i][j]

print('-=' * 15)

for l in range(3):
    for c in range(3):
        print(f"[{matriz[l][c]:^5}]", end=" ")
    print() 


print('-=' * 15)
print(f'A soma dos valores pares é: {soma}')
print(f'A soma dos números da 3º coluna é: {soma_3_coluna}')
print(f'O maior número da segunda linha é: {max(matriz[1])}')