# Nessa aula, vamos aprender o que são LISTAS e como utilizar listas em Python.
# As listas são variáveis compostas que permitem armazenar vários valores em
# uma mesma estrutura, acessíveis por chaves individuais.

# Como as Tuplas são Imutáveis
# Tupla:

'''
lanche = ('sanduiche', 'suco', 'pizza', 'pudim')
# Ordem:
#                0         1       2        3
#               -4        -3      -2       -1
print(lanche[2])
'''

# e se eu tentar mudar uma Tupla?
# Não dá porque já vimos na aula anterior que as Tuplas são imutáveis!
# E como que eu consigo resolver esse problema?
# Nesse caso já não poderiamos utilizar uma Tupla!
# Vamos ter que utilizar em Python uma lista

# Tuplas ()
# Listas []
'''
lanche = ['sanduiche', 'suco', 'pizza', 'pudim']
lanche[3] = 'picolé'
print(lanche)
'''
# resultado: ['sanduiche', 'suco', 'pizza', 'picolé']
# E se eu quiser adicionar uma 4 casa na lista?

# Para adicionar elementos novos na lista, temos um comando especial que é o metodo .append('biscoito')
# exemplo:
'''
lanche = ['sanduiche', 'suco', 'pizza', 'pudim']
lanche[3] = 'picolé'
lanche.append('biscoito')
print(lanche)
'''
# Resultado: ['sanduiche', 'suco', 'pizza', 'picolé', 'biscoito']
#                   0         1       2         3          4
# Repara que o elemento 4 foi criado e adicionado um biscoito

# Eu posso adicionar um elemento no meio dessa lista também
# Exemplo:
# Para isso eu vou utilizar um outro metodo que é o metodo .insert()
'''
lanche = ['sanduiche', 'suco', 'pizza', 'pudim']
lanche[3] = 'picolé'
lanche.append('biscoito')
lanche.insert(0, 'tomate')
print(lanche)
'''
# resultado: ['tomate', 'sanduiche', 'suco', 'pizza', 'picolé', 'biscoito']
#                0           1         2        3         4         5

# antes: ['sanduiche', 'suco', 'pizza', 'picolé', 'biscoito']
#               0         1       2         3          4

# Reprara que depois do .insert(0, 'tomate') o 'tomate',
# entrou no lugar do 'sanduiche', e "empurrou" o sanduiche pra casa do lado

# e como que eu posso apagar elementos?
# o modo mais básico é o comando del, note que não é um método
# del lanche[3]
# outra maneira de eliminar a pizza seria
# lanche.pop(3) aqui já é o metodo .pop()
# normalmente o método .pop() é pra eliminar o último elemento
# mas posso para como parâmetro o indice que eu quero pra ele eliminar
# existe um outro método que é o método .remove('pizza')
# No .remove() você não vai inidicar o indice, vocÊ vai indicar o valor que você quer eliminar

# del lanche[3]     para remover pela chave ou o indice em que se encontra o objeto use del ou .pop()
# lanche.pop(3)
# lanche.remove('pizza')        para eliminar pelo conteúdo, usar .remove('pizza')

# Em todos esses casos acima, ele vai eliminar a 'pizza', vai eliminar o valor, e vai refazer os indices
# exemplo:
'''
lanche = ['sanduiche', 'suco', 'pizza', 'pudim']
lanche[3] = 'picolé'
lanche.append('biscoito')
lanche.insert(0, 'tomate')
lanche.remove('pizza')
print(lanche)
'''
# antes era assim: ['tomate', 'sanduiche', 'suco', 'pizza', 'picolé', 'biscoito']
#                       0           1         2        3         4         5
# depois do .remove(): ['tomate', 'sanduiche', 'suco', 'picolé', 'biscoito']
#                          0           1          2        3          4
# ele  eliminou a 'pizza', eliminou o valor, refez os indices

# E se eu tentar remover um elemento que não existe?
# se eu tentar remover um elemento que nao existe na lista eu vou receber um erro
# pra fazer isso eu teria de utilizar a estrutura if, juntamente com o operador in
# exemplo:
# if 'pizza' in lanche:
#       lanche.remove('pizza')

# posso criar listas também através de range
# exemplo:
# valores = list(range(4, 11))
# a função list() para declarar uma lista, partindo do range de 4 até 11
# O range ele cria elementos já em ordem, de forma organizada de forma crescente

# E se eu quiser um elemento fora de ordem?
# Se eu fizer isso daqui, ele vai pegar esses valores e colocar dentro da lisa chamada valores
'''
valores = [8, 2, 5, 4, 9, 3, 0]         # E pra organizar esses valores de maneira facil?
valores.sort()                          # se eu der esse comando ele vai ordenar todos os valores organizados
valores.sort(reverse=True)              # Fazendo isso os valores ficam ordenados em ordem reversa (decrescente)
'''

'''
valores = [8, 2, 5, 4, 9, 3, 0]
print(len(valores))
'''
# resultado: 7
# Isso é muito útil quando precisamos fazer laços

# =============================================================
# TESTES!

'''
num = (2, 5, 9, 1)
num[2] = 3      # error: 'tuple' object does not support item assignment
print(num)'''

'''
num = [2, 5, 9, 1]      # mudei de tupla, pra lista apenas trocando () por []
num[2] = 3
print(num)'''
# resultado: [2, 5, 3, 1]       agora funciona normalmente

'''
num = [2, 5, 9, 1]      # mudei de tupla, pra lista apenas trocando () por []
num[2] = 3
num[4] = 7              # error: list assignment index out of range
print(num)'''
# Para que eu possa adicionar o valor 7, eu preciso fazer isso daqui:
'''
num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
print(num)'''
# resultado: [2, 5, 3, 1, 7]

# Repara que ainda está fora de ordem, vamos colocar isso em ordem!
'''
num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort()
print(num)'''
# resultado: [1, 2, 3, 5, 7]

'''
num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True) #
print(num)'''
# resultado: [7, 5, 3, 2, 1]

'''
num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True) 
print(num)
print(f'Essa lista tem {len(num)} elementos.') #
'''
# resultado:
# [7, 5, 3, 2, 1]
# Essa lista tem 5 elementos.

# adicionar elementos:
'''
num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 0) #
print(num)
print(f'Essa lista tem {len(num)} elementos.')'''
# resultado:
# [7, 5, 0, 3, 2, 1]
# Essa lista tem 6 elementos.

# remover elementos:
'''
num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 0)
num.pop() #
print(num)
print(f'Essa lista tem {len(num)} elementos.')'''
# resultado:
# [7, 5, 0, 3, 2]
# Essa lista tem 5 elementos.

'''
num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 0)
num.pop(2) #
print(num)
print(f'Essa lista tem {len(num)} elementos.')'''
# resultado:
# [7, 5, 3, 2, 1]
# Essa lista tem 5 elementos.

# vou alterar o .insert() agora para ver como ele se comporta, alterando 0 para 2
'''
num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 2)
print(num)
print(f'Essa lista tem {len(num)} elementos.')'''
# antes:
# [7, 5, 0, 3, 2, 1]
# Essa lista tem 6 elementos.

# depois de alterar:
# [7, 5, 2, 3, 2, 1]
# Essa lista tem 6 elementos.

# Temos 2 números 2 agora, e eu vou usar o .remove(), o que vai acontecer? já que tem 2 valores iguais²
'''
num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 2)
num.remove(2)
print(num)
print(f'Essa lista tem {len(num)} elementos.')'''
# resultado: [7, 5, 3, 2, 1]
# Essa lista tem 5 elementos.
# Ele vai procurar do inicio da lista a primeira ocorrência do valor que vc mandou eliminar,
# ele não vai até o final para eliminar todos os números mas da pra fazer isso usando laços


# E se eu tentar remover um número que não tem na lista? Por exemplo 4
# o que vai acontecer?
# # ValueError: list.remove(x): x not in list
# Vamos fazer o que foi feito lá em cima, usando a estrutura if e in
'''
num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 2)
if 4 in num:
    num.remove(4)       # Se por exemplo eu colocar aqui o número 5, se tiver o 5 vai remover o 5
else:
    print('Não achei o número 4')       
print(num)
print(f'Essa lista tem {len(num)} elementos.')'''
# resultado:
# Não achei o número 4
# [7, 5, 2, 3, 2, 1]
# Essa lista tem 6 elementos.

# =========================================================

'''
valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for v in valores:
    print(f'{v}...', end='')'''
# resultado: 5...9...4...

# posso fazer também...
'''
valores = list()
valores.append(5)
valores.append(9)
valores.append(4)

for c, v in enumerate(valores):       # se eu quiser além do valor o índice, as chaves faço assim
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')'''
# resultado:
# Na posição 0 encontrei o valor 5!
# Na posição 1 encontrei o valor 9!
# Na posição 2 encontrei o valor 4!
# Cheguei ao final da lista.

# Outra coisa que podemos fazer é ler valores pelo teclado e colocar dentro da lista

'''valores = list()
for cont in range(0,5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):       # se eu quiser além do valor o índice, as chaves faço assim
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')'''
# digitei: 54321
# resultado:
# Na posição 0 encontrei o valor 5!
# Na posição 1 encontrei o valor 4!
# Na posição 2 encontrei o valor 3!
# Na posição 3 encontrei o valor 2!
# Na posição 4 encontrei o valor 1!
# Cheguei ao final da lista.

# Uma peculiaridade do Python!

'''
a = [2, 3, 4, 7]
b = a
print(f'Lista A: {a}')
print(f'Lista B: {b}')'''
# result:
# Lista A: [2, 3, 4, 7]
# Lista B: [2, 3, 4, 7]

'''a = [2, 3, 4, 7]
b = a       
b[2] = 8     # a partir do momento em que eu igualo uma lista à outra, o Python cria uma ligação entre elas
print(f'Lista A: {a}')
print(f'Lista B: {b}')'''
# result:
# Lista A: [2, 3, 8, 7]
# Lista B: [2, 3, 8, 7]

a = [2, 3, 4, 7]
b = a[:]      # [:] mandando b receber todos os itens de a,
b[2] = 8      # dessa maneira aqui ele não vai criar uma ligação, ele vai criar uma cópia
print(f'Lista A: {a}')
print(f'Lista B: {b}')
# result:
# Lista A: [2, 3, 4, 7]
# Lista B: [2, 3, 8, 7]
