a = float(input("Digite o primeiro lado: "))
b = float(input("Digite o segundo lado: "))
c = float(input("Digite o terceiro lado: "))

if a + b > c and a + c > b and b + c > a:
    print ('Você tem um triangulo!')
else:
    print('Que pena! não é possível formar um triângulo!')
