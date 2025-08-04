# Soma de Números

quantidade = int(input("Quantos números você deseja somar? "))
soma = 0

for _ in range(quantidade):
    numero = float(input("Digite um número: "))
    soma += numero
print(f"A soma total é {soma}")

# Jeito pythonico

numeros = list(map(float, input("Digite os números separados por espaço: ").split()))
print(f"A soma total é {sum(numeros)}")