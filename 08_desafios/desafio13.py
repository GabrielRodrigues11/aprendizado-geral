# Calcular notas

quantidade = int(input("Quantas notas você quer dar? "))
soma = 0
notas = []

for x in range(quantidade):
    codigo_aluno = input("RM: ")
    nota = float(input("Nota: "))
    resultado = [codigo_aluno, nota]
    notas.append(resultado)
    soma += nota

print(f"Quantidade de notas: {len(notas)}")

for n in notas:
    codigo_aluno = n[0]
    nota = n[1]
    print(f"O RM {codigo_aluno} tirou a nota: {nota}")

media = soma / quantidade
print(f"A média das notas é: {media:.2f}")