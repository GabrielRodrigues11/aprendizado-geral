frase = input("Digite uma frase: ").replace(" ", "").lower() 
inverso = frase[::-1]
if frase == inverso:
    print("A frase é um palíndromo!")
else:
    print("A frase não é um palíndromo!")

print(frase, inverso)