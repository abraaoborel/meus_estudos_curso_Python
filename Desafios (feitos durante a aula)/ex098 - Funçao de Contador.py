# Faça um programa que tenha uma função chamada contador(),
# que receba três parâmetros: inicio, fim e passo e realize a contagem.
# Seu programa tem que realizar três contagens atráves da função criada:
# a) De 1 até 10, de 1 em 1
# b) De 10 até 0, de 2 em 2
# c) Uma contagem personalizada.

from time import sleep

'''
def contador(inicio, fim, passo):
    print('-' * 40)
    print('Contagem de 1 até 10, de 1 em 1:')
    for x in range(1, 11, 1):
        print(x, end=' ')
        sleep(0.5)
    print('FIM!')

    sleep(0.5)
    print('-' * 40)
    print('Contagem de 10 até 0, de 2 em 2:')
    for x in range(10, 0, -2):
        print(x, end=' ')
        sleep(0.5)
    print('FIM!')

    sleep(0.5)
    print('-' * 40)
    print('Agora é a sua vez de personalizar: ')
    for x in range(inicio, fim, passo):
        print(x, end=' ')
        sleep(0.5)
    print('FIM!')

inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)'''

# Tentei fazer da forma acima e não deu certo,
# estou vendo a resolução do exercício foi totalmente diferente do que eu fiz

# função nova que foi mostrada nesta aula: flush=True
# Pq quando ele mandava mostrar o contador, travava, e ficava travado, mas contando os intervalos por causa do sleep
# e não mostrava nada, ai depois de fazer a contagem junto com o sleep, ele dava um print de tudo pronto
# sem o intervalo de sleep, esse comando flush=True foi pra resolver esse BUG que deu quando ele gravava
# eu não tive problema com isso! Não deu BUG, o programa seguiu normal.
# Provavelmente já corrigiram esse BUG, mas anotei pra caso eu precise!

from time import sleep

def contador(i, f, p):
    if p < 0:       # Se p for menor do que zero, ou seja negativo
        p *= -1     # converto número negativo em positivo
    if p == 0:      # Se p for igual à zero:
        p = 1       # ele vai começar com 1

    print('-' * 40)
    print(f'Contagem de {i} até {f}, de {p} em {p}:')
    sleep(2.5)

    if i < f:       # Se o início foi menor do que o fim:
        cont = i        # contador começa do início
        while cont <= f:        # Enquanto contador for menor do que o fim, faça isso:
            print(f'{cont} ', end='')       # mostrar contador
            sleep(0.5)
            cont += p       # Contador recebe ele mesmo + 1
        print('FIM!')
    else:       # Caso contrário, ou seja, se o fim for maior do que o início:
        cont = i        # contador começa no início
        while cont >= f:        # Enquanto o contador, for maior ou igual ao fim, faça isso:
            print(f'{cont} ', end='')       # mostrar contador
            sleep(0.5)
            cont -= p       # contador recebe ele mesmo - 1
        print('FIM!')


# Programa Principal
contador(1, 10, 1)
contador(10, 0, 2)
print('-' * 40)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim:    '))
pas = int(input('Passo:  '))
contador(ini, fim, pas)

# Complexo! Tentei fazer usando o for, mas não consegui
# Poderia ter continuado tentando até conseguir
# Mas o programa ficaria enorme!
