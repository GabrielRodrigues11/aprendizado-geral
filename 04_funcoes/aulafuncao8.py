def fatorial(a, show=False):
    """
        -> Calcula o Fatorial de um número.
        :param n: O número a ser calculado
        :param show: (opcional) Mostrar ou não o cálculo
        :return: O valor do Fatorial um número n
        """
    fat = 1
    for i in range(a,0,-1):
        if show:
            print(i, end='')
            print(' x ' if i > 1 else ' = ', end='')
        fat *= i
    return fat

print(fatorial(5, True))
help(fatorial)