num = int(input('Digite um número inteiro: '))
print('Escolha uma base de conversão:')
print('1 - Binário')
print('2 - Octal')
print('3 - Hexadecimal')
    
opcao = int(input("Sua opção: "))
   
if opcao == 1:
    print(f'{num} em binário é {bin(num)[2:]}')
elif opcao == 2:
    print(f'{num} em octal é {oct(num)[2:]}')
elif opcao == 3:
    print(f'{num} em hexadecimal é {hex(num)[2:]}')
else:
    print('Opção inválida!')

