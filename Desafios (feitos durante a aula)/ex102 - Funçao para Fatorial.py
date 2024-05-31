# Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
# o primeiro que indique o número a calcular e outro chamado show,
# que será um valor lógico (opcional) indicando se será mostrado ou
# não na tela o processo de cálculo do fatorial.


# O parâmetro opcional, é chamado de show. Coloquei com o Padrão False, porque ao chamar o True, ele retorna show
def fatorial(n, show=False):        # a função, recebe um número como parâmetro, e show como parâmetro opicional
    """
    --> Calcula o Fatorial de um número. <--
    :param n: O número a ser calculado.
    :param show: (opicional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    """
    f = 1       # Variável fatorial começa com 1
    for c in range(n, 0, -1):        # Vai começar do número recebido como parâmetro até o zero, voltando 1
        if show:
            print(c, end='')    # Vou mandar mostrar c, sem quebrar a linha
            if c > 1:   # E se (c) tiver o contador maior do que 1
                print(' x ', end='')    # ele vai escrever um x
            else:       # Se o (c) não for maior do que 1
                print(' = ', end='')    # Escrevo = sem quebrar a linha
        f *= c      # fatorial vai receber ele mesmo vezes o contador
    return f        # Fora do for eu vou ter o return do valor de f


# Programa Principal
#print(fatorial(5))  # Saída: 120
print(fatorial(5, show=True))   # Saída: 5 x 4 x 3 x 2 x 1 = 120
#help(fatorial)  # Funcionando!