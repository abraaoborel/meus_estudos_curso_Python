# O mesmo professor do desafio anterior quer sortear a ordem de
# apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

'''
import random
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print('A ordem de apresentação será ')
print(lista)
'''

# 2a maneira:

from random import shuffle
n1 = str(input('\033[1;7;30;107mPrimeiro aluno:\033[m '))
n2 = str(input('\033[1;7;31;107mSegundo aluno:\033[m '))
n3 = str(input('\033[1;7;32;107mTerceiro aluno:\033[m '))
n4 = str(input('\033[1;7;33;107mQuarto aluno:\033[m '))
lista = [n1, n2, n3, n4]
shuffle(lista) # para embaralhar a (lista)
print('\033[7;34;107mA ordem de apresentação será:\033[m')
print(f'\033[7;97;40m{lista}\033[m')