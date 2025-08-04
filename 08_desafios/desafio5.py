# Verificador de número primo

def verificar_primo(n):
    if n <= 1:
        return "Não é primo"
    
    for i in range(2, n):
        if n % i == 0:
            return "Não é primo"
    
    return "É primo!"


num = int(input("Digite um número: "))
print(verificar_primo(num))
