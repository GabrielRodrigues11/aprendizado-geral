distancia = int(input('Qual a distância de sua viagem? '))

print(f'Sua viagem custou R${0.50 * distancia} (50 centavos por km)' if distancia <= 200 else f'Sua viagem custou R${0.45 * distancia} (45 centavos por km)')