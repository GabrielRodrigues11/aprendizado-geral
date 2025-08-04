algo = input('Digite algo: ')
print(f'O tipo primitivo desse valor é {type(algo)}\n'
      f'Só tem espaços? {algo.isspace()}\n'
      f'É um número? {algo.isnumeric()}\n'
      f'É alfabético? {algo.isalpha()}\n'
      f'É alfanumérico? {algo.isalnum()}\n'
      f'Está em maiúsculas? {algo.isupper()}\n'
      f'Está em minúsculas? {algo.islower()}\n'
      f'Está capitalizada? {algo.istitle()}')

