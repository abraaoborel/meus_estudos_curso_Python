# Nessa aula, vamos aprender como utilizar a instrução break e os
# loopings infinitos a favor das nossas estratégias de código.
# É muito importante saber usar o break no Python,
# já que em alguns casos precisamos interromper um laço no meio do caminho.

# Além disso, vamos aprender como trabalhar com as novas fstrings do Python.

'''cont = 1
while cont <= 10:
    print(cont, ' -> ', end='')
    cont += 1
print('ACABOU')'''

'''cont = 1
while True: # Se eu usar essa estrutura ele vai executar infinitas vezes
    print(cont, ' -> ', end='')
    cont += 1
print('ACABOU')'''

# ==============================================

'''while n != 999:         # Se eu executar somente essas duas linhas ele vai dar um erro
    n = int(input('Digite um número: '))'''        # Porque? Porque eu estou testando um número e nem comecei ele.

# Então o que eu faço?

'''n = 0
while n != 999:
    n = int(input('Digite um número: '))'''

# OK, quantas vezes ele vai fazer isso? Eu não disse quantas vezes ele vai fazer isso.
# Eu não estou utilizando um contador, se eu quissesse contar 5 números

'''n = cont = 0
while cont < 5:
    n = int(input('Digite um número : '))
    cont += 1'''

# OK, o que eu fiz? Eu fiz contador começar com 0
# E enquanto o contador for menor do que 5 ele vai executar o loop

# ====================================================================================

'''n = 0
while n != 999:         # A CONDIÇÃO DE PARADA É CHAMADA DE FLAG
    n = int(input('Digite um número: '))'''

# OK, agora eu quero somar todos esses números:

'''n = s = 0       # INICIEI A VARIAVEL 'S', QUE VAI RECEBER A SOMA ==== (A VARIÁVEL TEM QUE SER INICIADA!) =====
while n != 999:
    n = int(input('Digite um número: '))
    s += n      # ESSE 'S', VAI SEMPRE RECEBER O 'S' + 'N' (SOMAR O S)
print(f'A soma vale {s}')'''

# NESSE RESULTADO, ELE ESTÁ SOMANDO A FLAG

'''n = s = 0
while n != 999:
    n = int(input('Digite um número: '))
    s += n
s -= 999
# ESSA É UMA TREMENDA GAMBIARRA. (s -= 999)
# PQ? Pq vc mandou ler um número e somar ele logo em seguida, você não tem como testar ou interromper
# ESSE RESULTADO ATÉ FUNCIONA, MAS NÃO USE GAMBIARRA!
print(f'A soma vale {s}')'''

# COMO INTERROMPER, ESSE LOOP DA MANEIRA CORRETA?

n = s = 0
while True:      # CRIEI UM LOOP INFINITO
    n = int(input('Digite um número: '))
    if n == 999:    # COLOQUEI UMA CONDIÇÃO
        break       # QUE EXECUTA O BREAK
    s += n
print(f'A soma vale {s}')

# O COMANDO BREAK, É PARA SAIR DE DENTRO DO LOOP INFINITO.
# OU SEJA: SAIR DO LAÇO WHILE

# ====================================
# NA EPOCA EM QUE O GUANABARA LANÇOU O CURSO TEVE UMA ATUALIZAÇÃO
# HOJE EM QUE EU ESTOU FAZENDO O CURSO JÁ DEVE TER PASSADO POR MUITAS ATUALIZAÇÕES
# O GUANABARA ENSINOU A USAR AS F STRINGS. AO INVÉS DE USAR O
# ANTES ERA ('{}'.FORMAT())
# DEPOIS DA ATUALIZAÇÃO É (F'{}')
# OBS.: EU JÁ ESTAVA USANDO ESSAS F STRINGS ANTES MESMO DE ELE ENSINAR ISSO
# PORQUE EU TINHA OBSERVADO EM ALGUM COMENTÁRIO NO YOUTUBE DE UM DOS EXERCÍCIOS DO CURSO EM VIDEO
# E LÁ ALGUEM TINHA ENSINADO ISSO, DIZENDO QUE É UMA MANEIRA MAIS ATUALIZADA DE FAZER
# PRA NÃO PRECISAR FAZER O .FORMAT()
# POR ISSO TODOS OS MEUS EXERCÍCIOS, FORAM REFEITOS COM O F STRINGS
# OU A MAIORIA DELES.
# ======================================
