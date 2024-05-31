# Faça um programa que leia um ângulo qualquer e mostre na tela o valor
# do seno, cosseno e tangente desse ângulo.

# Consegui fazer este desafio com ajuda da resolução. Até tentei ler sobre mas não entendi nada.
# Segue a solução:

'''
import math
angulo = float(input('Digite o angulo que você deseja: '))
seno = math.sin(math.radians(angulo))
print('O ângulo de {} tem o SENO de {:.2f}'.format(angulo, seno))
cosseno = math.cos(math.radians(angulo))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(angulo, cosseno))
tangente = math.tan(math.radians(angulo))
print('O ângulo de {} tem a TANGENTE de {:.2f} '.format(angulo, tangente))
'''

#2a forma de fazer:

from math import radians, sin, cos, tan
angulo = float(input('\033[1;7;97;40mDigite o angulo que você deseja:\033[m '))
seno = sin(radians(angulo))
print(f'\033[7;30;107mO ângulo de {angulo} tem o SENO de {seno:.2f}\033[m')#.format(angulo, seno))
cosseno = cos(radians(angulo))
print(f'\033[7;30;107mO ângulo de {angulo} tem o COSSENO de {cosseno:.2f}\033[m')#.format(angulo, cosseno))
tangente = tan(radians(angulo))
print(f'\033[7;30;107mO ângulo de {angulo} tem a TANGENTE de {tangente:.2f}\033[m')#.format(angulo, tangente))
