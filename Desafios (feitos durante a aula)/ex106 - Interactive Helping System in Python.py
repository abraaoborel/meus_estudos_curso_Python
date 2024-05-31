# Faça um mini-sistema que utilize o Interactive Help do Python.
# O usuário vai digitar o comando e o manual vai aparecer.
# Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará.
# Importante: use cores.

from time import sleep

c = ('\033[m',             # 0 - sem cores
     '\033[1;97;41m',      # 1 - negrito, letras brancas, fundo vermelho
     '\033[1;97;44m',      # 2 - negrito, letras brancas, fundo Azul
     '\033[1;30;107m'      # 3 - negrito, Letras pretas, fundo branco
     )


def ajuda(com):
    título(f'Acessando o manual do comando \'{com}\'', 2)       # Contra barra aqui apenas para escapar {com}
    print(c[3], end='')         # Sobre essa contra barra aqui em cima. ==> Saída: sem contra barra: print/ com 'print'
    help(com)
    print(c[0], end='')
    sleep(2)

def título(msg, cor=0):     # Se eu não digitar nada a cor padrão vai ser zero
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')
    sleep(1)


# Programa Principal
comando = ' '
while True:
    título('SISTEMA DE AJUDA PyHELP', 1)
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':        # se o usuário possa digitar fim de mais/minus... vai funcionar
        break
    else:
        ajuda(comando)
título('ATÉ LOGO!', 1)
