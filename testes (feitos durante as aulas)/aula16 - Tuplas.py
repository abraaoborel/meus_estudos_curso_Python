# No Python eu posso começar uma variável composta de 3 maneiras: () [] {}
# () TUPLA
# [] LISTA
# {} DICIONÁRIO
# Vamos aprender a TUPLA:
# anotação importante: A TUPLA É IMUTÁVEL

# Quando eu fazia:
'''
lanche = 'hamburguer'
lanche = 'suco'
print(lanche)
'''
# Repara que a mesma variável não recebe mais de 1 valor, e o 'suco', substituiu o 'hamburguer'.

'''
lanche = ('hamburguer', 'suco', 'Pizza', 'Pudim')
print(lanche)
'''
# Resultado desse print: ('hamburguer', 'suco', 'Pizza', 'Pudim')

# Posso criar uma TUPLA sem parênteses:
'''
lanche = 'hamburguer', 'suco', 'Pizza', 'Pudim'
print(lanche)
'''
# Resultado desse print: ('hamburguer', 'suco', 'Pizza', 'Pudim')
# funciona da mesma maneira

# Mas para efeitos práticos e didáticos,
# sempre que criarmos a TUPLA durante esse curso,
# vamos criar com parêntesees!

'''
lanche = ('hamburguer', 'suco', 'Pizza', 'Pudim')
print(lanche[1])
'''
# Na hora de referênciar é sempre colchetes
# Resultado desse print: suco

# Quem é o lanche 1?
# lanche = ('hamburguer', 'suco', 'Pizza', 'Pudim')
#                 0          1       2        3
#                -4         -3       -2       -1

'''
lanche = ('hamburguer', 'suco', 'Pizza', 'Pudim')
print(lanche[1:3])
'''
# Resultado desse print: ('suco', 'Pizza')
# O último elemento é ignorado quando eu faço o fatiamento
# Nesse caso do print(lanche[1:3]), ele foi do elemento 1 ao elemento 2 ignorando o 3
# o último elemento 3 do fatiamento foi ignorado

'''
lanche = ('hamburguer', 'suco', 'Pizza', 'Pudim')
print(lanche[2:])
'''
# Resultado do print: ('Pizza', 'Pudim')
# Fatiamento de 2: até o final

'''
lanche = ('hamburguer', 'suco', 'Pizza', 'Pudim')
print(lanche[:2])
'''
# Me mostre do inicio até o elemento 2, mas lembre-se que
# ele vai ignorar o elemento 2 que foi o ultimo elemento a ser fatiado
# Resultado dessse print: ('hamburguer', 'suco')

'''
lanche = ('hamburguer', 'suco', 'Pizza', 'Pudim')
print(lanche[-2:])
'''
# Resultado desse print: ('Pizza', 'Pudim')
# ele vai começar na pizza e vai até o final

'''
lanche = ('hamburguer', 'suco', 'Pizza', 'Pudim')
print(lanche[-3:])
'''
# Resultado desse print: ('suco', 'Pizza', 'Pudim')

# TUPLAS SÃO IMUTÁVEIS
# Por exemplo:
'''
lanche = ('hamburguer', 'suco', 'Pizza', 'Pudim')
lanche[1] = 'Refrigerante'
print(lanche[1])
'''
# Resultado da um erro!!!
# Porque as TUPLAS são IMUTÀVEIS
# Eu não consigo atribuir valores em uma TUPLA, a não ser na declaração dela

'''
lanche = ('hamburguer', 'suco', 'Pizza', 'Pudim', 'Batata Frita')

for comida in lanche:
    print(f'Eu vou comer {comida}')
    
print('Comi pra caramba!')
'''
# Resultado desse for:
# Eu vou comer hamburguer
# Eu vou comer suco
# Eu vou comer Pizza
# Eu vou comer Pudim
# Comi pra caramba!

'''
lanche = ('hamburguer', 'suco', 'Pizza', 'Pudim', 'Batata Frita')

for contador in range(0, len(lanche)):
    print(contador)
    
print('Comi pra caramba!')
'''
# Resultado desse for:
# 0
# 1
# 2
# 3
# 4
# Comi pra caramba!

# E se eu mostrar o lanche na posição [c]?
'''
lanche = ('hamburguer', 'suco', 'Pizza', 'Pudim', 'Batata Frita')

for c in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[c]}')
    
print('Comi pra caramba!')
'''
# Resultado desse for:
# Eu vou comer hamburguer
# Eu vou comer suco
# Eu vou comer Pizza
# Eu vou comer Pudim
# Eu vou comer Batata Frita
# Comi pra caramba!

# ==============================================
'''
lanche = ('hamburguer', 'suco', 'Pizza', 'Pudim', 'Batata Frita')

for comida in lanche:
    print(f'Eu vou comer {comida}')
    
print('Comi pra caramba!')
'''
# No exemplo acima eu uso diretamente a minha variável composta
# Esses 2 for tem o mesmo resultado!
# No exemplo abaixo eu uso o range
'''
lanche = ('hamburguer', 'suco', 'Pizza', 'Pudim', 'Batata Frita')

for c in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[c]}')
    
print('Comi pra caramba!')
'''
# ===============================================
# SEMPRE QUE VOCÊ PRECISAR MOSTRAR A POSIÇÃO, USE ESTE:
'''
lanche = ('hamburguer', 'suco', 'Pizza', 'Pudim', 'Batata Frita')

for c in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[c]} na posição {c}')
    
print('Comi pra caramba!')
'''
# Resultado desse codigo:
# Eu vou comer hamburguer na posição 0
# Eu vou comer suco na posição 1
# Eu vou comer Pizza na posição 2
# Eu vou comer Pudim na posição 3
# Eu vou comer Batata Frita na posição 4
# Comi pra caramba!

# TAMBÉM DA PRA FAZER ISSO DAQUI, QUE VAI FUNCIONAR DA MESMA FORMA QUE O CODIGO DE CIMA:
# ANOTAÇÃO: O enumerate me dá tanto o dado como a posição
'''
lanche = ('hamburguer', 'suco', 'Pizza', 'Pudim', 'Batata Frita')

for pos, comida in enumerate(lanche):        
    print(f'Eu vou comer {comida} na posição {pos}')
    
print('Comi pra caramba!')
'''
# Resultado desse codigo:
# Eu vou comer hamburguer na posição 0
# Eu vou comer suco na posição 1
# Eu vou comer Pizza na posição 2
# Eu vou comer Pudim na posição 3
# Eu vou comer Batata Frita na posição 4
# Comi pra caramba!

# ========================================================

'''
lanche = ('hamburguer', 'suco', 'Pizza', 'Pudim', 'Batata Frita')
print(sorted(lanche))
'''
# sorted significa organizado, em ordem
# Nesse comando eu mando mostrar o lanche em ordem
# Resultado desse print: ['Batata Frita', 'Pizza', 'Pudim', 'hamburguer', 'suco']
# O sorted ele não altera a sua TUPLA, ele simplismente coloca ela em ordem
# Então não se preocupe com o [], porque não virou uma lista. Continua sendo uma TUPLA
# Só que agora ela está organizada

# ============================================================

# Vou criar 2 TUPLAS:


'''
a = (2, 5, 4)       # Eu posso dar um print na TUPLA a, e também na TUPLA b.
b = (5, 8, 1, 2)
c = a + b           # Mas e se eu fizer isso?!
print(c)
'''
# Resultado: (2, 5, 4, 5, 8, 1, 2)
# ela juntou a + b

'''
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(c)
'''
# Resultado: (5, 8, 1, 2, 2, 5, 4)
# Repara que o resultado foi diferente do anterior

# OU SEJA?! A ORDEM AQUI TEM TOTAL INFLUÊNCIA!

'''
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(len(c))
'''
# Resultado: 7

'''
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(c.count(5))
'''
# .count vai mostrar quantas vezes está aparecendo o número 5 dentro de c?
# Resultado: 2

# Além do count eu tenho a propriedade .index do objeto TUPLA
# O .index vai mostrar em que posição está
'''
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(c)
print(c.index(5))
'''
# Resultado:
# (5, 8, 1, 2, 2, 5, 4)
# 0
# Mas tem um outro 5 nessa TUPLA
'''
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(c)
print(c.index(5, 1))
'''
# Eu não vou ver na posição 0, vou começar na posição 1
# Resultado:
# (5, 8, 1, 2, 2, 5, 4)
# 5
# Isso é chamado de deslocamento

# Eu também posso ter dados de tipos diferentes dentro das minhas TUPLAS
'''
pessoa = ('Gustavo', 39, 'M', 99.88)
print(pessoa)
'''
# Resultado: ('Gustavo', 39, 'M', 99.88)

'''
pessoa = ('Gustavo', 39, 'M', 99.88)
del(pessoa)
print(pessoa)
'''
# Deu erro!
# Porque? Porque quando eu uso a palavra del, eu estou apagando essa variável
# Então quando é apagado na memoria não resta resquíscio nenhum do que existia antes de começar a executar

# A TUPLA é imutável menos para ser apagada!
# Mas eu também não posso deletar um único item dentro da TUPLA
'''
pessoa = ('Gustavo', 39, 'M', 99.88)
del(pessoa[0])
print(pessoa)
'''
# TypeError: 'tuple' object doesn't support item deletion
# Mas se eu deletar a TUPLA inteira ele aceita sem problema nenhum
