matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
contador = 0

for i in range(3):
    for j in range(3):
        matriz[i][j] = int(input(f'Digite um valor para [{i}, {j}]: '))

for l in range(3):
    for c in range(3):
        print(f"[{matriz[l][c]:^5}]", end=" ")
    print() 