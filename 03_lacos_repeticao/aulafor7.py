n = int(input("Digite um número: "))

if n < 2:
    print(f"{n} não é primo!")
else:
    for i in range(2, n):
        if n % i == 0:
            print(f"{n} não é primo!")
            break
    else:
        print(f"{n} é primo!")