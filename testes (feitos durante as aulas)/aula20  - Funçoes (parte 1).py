# Nessa aula, vamos aprender o que são funções ou rotinas e como utilizar funções em Python.
# Funções são trechos de código que podem ser executados em momentos diferentes de nossos códigos em Python.
# Veja como funciona o comando def em Python e como utilizá-lo com parâmetros simples e múltiplos.

# O que é uma função?
# É uma ROTINA

# Qualquer coisa que fazemos frequentemente é uma rotina,
# E nos programas em python, também temos diversas tarefas repetidas
# Como mostrar linhas para separar textos
# Às vezes repetir o mesmo código várias vezes, dentro do mesmo programa
# etc... e para isso, eu crio uma função para me atender neste determinado caso.
# por exemplo:
# print('---------------------')
# print('  SISTEMA DE ALUNOS  ')
# print('---------------------')
# print('-------------------------')
# print('CADASTRO DE FUNCIONÁRIOS')
# print('-------------------------')
# print('---------------------')
# print('   ERRO DO SISTEMA   ')
# print('---------------------')
# Repara que o print dessa linha acontece 6x
# E acaba ficando uma tarefa muito repetitiva

# Para otimizar eu tenho que fazer o seguinte:
# eu escrevo a linha uma vez:
# print('---------------------')
# e depois eu crio uma ROTINA, uma FUNÇÃO, chamada mostralinha
# como eu faço? Simples!

# def mostralinha():
#     print('---------------------')

# quando eu crio essa def, os traços acontecem 6x
# .... vou dar uma simplificada
# mostralinha()
# print('  SISTEMA DE ALUNOS  ')
# mostralinha()
# mostralinha()
# print('CADASTRO DE FUNCIONÁRIOS')
# mostralinha()
# mostralinha()
# print('   ERRO DO SISTEMA   ')
# mostralinha()

'''
print('-' * 30)
print('   CURSO EM VÍDEO   ')
print('-' * 30)
print('-' * 30)
print('   APRENDA PYTHON   ')
print('-' * 30)
print('-' * 30)
print('  GUSTAVO GUANABARA  ')
print('-' * 30)'''

'''
def lin():
    print('-' * 30)


# Programa Principal
print('   CURSO EM VÍDEO   ')
print('   APRENDA PYTHON   ')
print('  GUSTAVO GUANABARA  ')'''

# Resultado:
#    CURSO EM VÍDEO
#    APRENDA PYTHON
#   GUSTAVO GUANABARA

# Mas porque ele não executou o mando print('-' * 30) lá em cima?
# Quando você executa o programa ele não executa as suas defs
# Ele só vai executar as suas funçoes quando você chamar o cabeçalho, pelo nome

'''
def lin():
    print('-' * 30)


# Programa Principal
lin()
print('   CURSO EM VÍDEO   ')
print('   APRENDA PYTHON   ')
print('  GUSTAVO GUANABARA  ')
lin()'''
# Resultado:
# ------------------------------
#    CURSO EM VÍDEO
#    APRENDA PYTHON
#   GUSTAVO GUANABARA
# ------------------------------

# Todas as vezes que eu precisar colocar a linha é só chamar a função lin, que eu criei

# =======================//======================

# Mas a função DEF, é um pouco mais poderoso do que isso
# Na verdade, bem mais poderoso do que isso!
# Porque eu posso trabalhar com parâmetros
# vamos continuar como exemplo o que estamos trabalhando acima
'''
def mensagem(msg):
    print('-' * 30)
    print(msg)
    print('-' * 30)
mensagem('SISTEMA DE ALUNOS')'''
# Resultado:
# ------------------------------
# SISTEMA DE ALUNOS
# ------------------------------

# Na hora que eu mandar escrever o msg
# ele vai receber o conteúdo de msg que eu recebi como parâmetro
# por exemplo:
# quando eu chamei a mensagem()
# que é a minha função
# def mensagem()
# eu passei o parâmetro
# mensagem('SISTEMA DE ALUNOS')
# na declaração da mensagem()
# eu digo que eu recebo um parâmetro chamado msg
# def mensagem (msg)
# msg nesse caso vai ser 'SISTEMA DE ALUNOS'

'''
def mensagem(msg):
    print('-' * 30)
    print(msg)
    print('-' * 30)
mensagem('EU VOU TRABALHAR COM PYTHON')
mensagem('NÃO VEJO A HORA DE COMEÇAR')
mensagem('QUERO SER O MELHOR!!!')'''
# Resultado:
# ------------------------------
# EU VOU TRABALHAR COM PYTHON
# ------------------------------
# ------------------------------
# NÃO VEJO A HORA DE COMEÇAR
# ------------------------------
# ------------------------------
# QUERO SER O MELHOR!!!
# ------------------------------

# ===============//=====================

'''
a = 4
b = 5
s = a + b
print(s)    # 9

a = 8
b = 9
s = a + b
print(s)    # 17

a = 2
b = 1
s  = a + b
print(s)    # 3'''
# Resultado:
# 9
# 17
# 3

# Repara que eles são quase iguais, muda apenas os valores recebidos
# seria ótimo se eu pudesse fazer:
# soma(4, 5)
# soma(8, 9)
# soma(2, 1)
# e obviamente se eu executar isso vai dar erro!
# porque? não existe em python esse comando soma()
# mas eu posso criar, personalizar, definir soma()

'''
def soma(a, b):
    s = a + b
    print(s)


# Programa Principal
soma(4, 5)
soma(8, 9)
soma(2, 1)'''

#Resultado:
# 9
# 17
# 3

# eu coloquei em def soma(a, b):
# apenas 2 parâmetros: a e b
# entao se eu tentar mostrar
# soma(4) ele dá erro!
# porque eu especifiquei que eu quero 2 parâmetros
# quanto defini a soma(a, b)

# posso também fazer isso daqui:
'''
def soma(a, b):
    s = a + b
    print(s)


# Programa Principal
soma(a=4, b=5)  # 9
soma(b=4, a=5)  # 9'''
# Eu posso mudar a ordem, contanto que eu deixe explícito

'''
def soma(a, b):
    print(f'A = {a}, e B = {b}')
    s = a + b
    print(f'A soma de A + B = {s}')


# Programa Principal
soma(a=4, b=5)'''
# Resultado:
# A = 4, e B = 5
# A soma de A + B = 9

# Posso alterar a ordem de A ou B, deixando explícito
# E seu eu quiser:
# soma(5, 7, 8)
# vai dar erro, porque eu coloquei apenas 2 parâmetros!

# Mas... No python existe uma função que se chama EMPACOTAMENTO
# vamos entender isso na prática

# Como eu vou receber vários números eu coloco um * na frente,
# informando que eu não sei quantos parâmetros vão ser recebidos
'''
def contador(*num):
    print(num)


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)'''
# Resultado:
# (2, 1, 7)
# (8, 0)
# (4, 4, 7, 6, 2)

# repara que ele criou uma tupla
# O que eu posso fazer com isso?
'''
def contador(*num):
    for valor in num:
        print(f'{valor} ', end='')
    print('FIM!')


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)'''
# Resultado:
# 2 1 7 FIM!
# 8 0 FIM!
# 4 4 7 6 2 FIM!

# -------------------------

'''def contador(*num):
    tamanho = len(num)
    print(f'Recebi os valores {num}, que são ao todo {tamanho} números.')


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)'''

# Resultado:
# Recebi os valores (2, 1, 7), que são ao todo 3 números.
# Recebi os valores (8, 0), que são ao todo 2 números.
# Recebi os valores (4, 4, 7, 6, 2), que são ao todo 5 números.

# -------------------------

# Além de podermos trabalhar com as tuplas() que são um pouco limitadas
# Porque não podem ser alteradas, podemos também trabalhar com listas[]

'''
def dobra(lst):   # dobra recebe uma lista que eu chamei aqui de (lst)
    pos = 0     # pos de posição
    while pos < len(lst):     # enquanto a posição for menor do que o tamanho da lista
        lst[pos] *= 2     # lst na posição pos, vai receber o dobro
        pos += 1        # depois pos recebe pos + 1

valores = [6, 3, 9, 1, 6, 2, 7]     # ele vai criar uma lista valores
dobra(valores)      # eu passei como parâmetro valores, e essa lista valores vai para lst
print(valores)      # ele vai dobrar todos os valores dentro da lista valores'''
# Resultado: [12, 6, 18, 2, 12, 4, 14]

# nesse momento eu vou ter duas listas na memória, uma lista chamada valores e uma lista chamada lst
# Tudo que eu fizer em lst vai interferir em valores diretamente!


# GUANABARA DEIXOU ESCAPAR ISSO, DIZENDO QUE É PAPO DE QUEM É MAIS EXPERIÊNTE:
# Para o Python toda passagem de parâmetros é por referência
# Diferente de outras linguagens como C e Java onde a passagem de parâmetros é por valor

# -------------------------
# Voltando ao DESEMPACOTAMENTO, só mais um exemplo:
def soma(* valores):    # vou receber aqui vários valores
    s = 0   # soma recebe zero
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')


soma(5, 2)
soma(2, 9, 4)
# Resultado:
# Somando os valores (5, 2) temos 7
# Somando os valores (2, 9, 4) temos 15

# Em algumas situações é melhor usar o EMPACOTAMENTO e em outras é melhor utilizar lista.
