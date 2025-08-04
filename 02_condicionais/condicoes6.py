a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))
c = float(input("Digite o terceiro número: "))

# Maior
if a >= b and a >= c:
    maior = a
elif b >= a and b >= c:
    maior = b
else:
    maior = c

# Menor
if a <= b and a <= c:
    menor = a
elif b <= a and b <= c:
    menor = b
else:
    menor = c

print(f'O maior número é {maior}')
print(f'O menor número é {menor}')


# Jeito simples
"""
maior = max(a, b, c)
menor = min(a, b, c)

print(f'O maior número é: {maior}')
print(f'O menor número é: {menor}')"
"""