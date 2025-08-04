import requests

url = 'https://www.google.com'

try:
    resposta = requests.get(url)
    if resposta.status_code == 200:
        print(f'O site {url} está acessível!')
    else:
        print(f'O site {url} respondeu com o código {resposta.status_code}')
except requests.exceptions.RequestException as erro:
    print(f'Não foi possível acessar o site {url}. Erro: {erro}')
