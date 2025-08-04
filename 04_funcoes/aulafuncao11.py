def notas(*num, sit=False):
    """
    -> Função para analissar notas e situações de vários alunos.
    :param n: Uma ou mais notas dos alunos (aceita várias)
    :param sit: Valor opcional, indicando se deve ou não adicionar a situação
    :return: Retorna o dicionário com várias informações sobre a situação da turma
    """
    dados = dict()

    dados['total'] = len(num)
    dados['maior'] = max(num)
    dados['menor'] = min(num)
    dados['média'] = sum(num) / len(num)

    if sit:
        if dados['média'] < 6:
                dados['situação'] = 'RUIM'
        elif 6 <= dados['média'] < 7:
                dados['situação'] = 'RAZOÁVEL'
        elif 7 <= dados['média'] < 9:
                dados['situação'] = 'BOA'
        else:
                dados['situação'] = 'ÓTIMA'

    return dados

resp = notas(1, 2, 8, 4, 6, sit=True)

print(resp)
help(notas)