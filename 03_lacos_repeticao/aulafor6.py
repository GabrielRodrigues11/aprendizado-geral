termo = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))

print("Os 10 primeiros termos da PA são:")
for n in range(10):
    resultado = termo + n * razao 
    print(resultado, end=' -> ')
print('ACABOU')