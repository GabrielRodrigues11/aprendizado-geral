### COMPLEMENTO DO CONDICOES8.PY

a = float(input("Digite o primeiro lado: "))
b = float(input("Digite o segundo lado: "))
c = float(input("Digite o terceiro lado: "))

if a + b > c and a + c > b and b + c > a:
    if a == b and a == c:
        print('Você tem um triângulo EQUILÁTERO!')
    elif a == b or a == c:
        print('Você tem um triângulo ISÓSCELES!')
    else:
        print('Você tem um triângulo ESCALENO!')
else: 
    print('Que pena! Não é possível formar um triângulo!')

