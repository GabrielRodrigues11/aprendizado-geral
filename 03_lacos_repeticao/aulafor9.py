from datetime import date

ano = date.today().year
menores = 0
maiores = 0

for c in range(1,8):
    nascimento = int(input(f'Em que ano a {c}ª pessoa nasceu?: '))
    if ano - nascimento < 18:
        menores += 1
    else:
        maiores += 1
print(f'''Ao todo tivemos {maiores} pessoas maiores de idade
E também tivemos {menores} pessoas menores de idade''')
