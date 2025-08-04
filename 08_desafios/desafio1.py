# Verificador de palíndromo

#Texto Palíndromo de exemplo => A man, a plan, a canal, Panama 

def verificador_palindromo(texto):
    texto = texto.lower()

    texto_limpo = ""

    for c in texto:
        if c.isalnum():
            texto_limpo += c

    if texto_limpo == texto_limpo[::-1]:
        return "É um palíndromo!"
    else:
        return "Não é um Palíndromo!"
    
#Teste

entrada = input("Digite uma palavra ou frase: ")
print(verificador_palindromo(entrada))

