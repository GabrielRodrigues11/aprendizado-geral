# Contador de vogais

def contador_vogais(texto):
    texto = texto.lower()

    vogais = "aeiouáéíóúAEIOUÁÉÍÓÚ"
    contador = 0

    for letra in texto:
        if letra in vogais:
            contador += 1
            
    return(f"A frase tem {contador} vogais")

entrada = input("Digite uma palavra ou texto: ")

print(contador_vogais(entrada))