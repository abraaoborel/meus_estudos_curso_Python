# Nessa aula, vamos aprender o que são DICIONÁRIOS e como utilizar dicionários em Python.
# Os dicionários são variáveis compostas que permitem armazenar vários valores em uma mesma estrutura,
# acessíveis por chaves literais.

# Nas aulas passadas vimos como declarar uma lista
# dados = list()
# essa variavel dados pode conter vários valores, é uma lista de valores
# eu posso adicionar itens na lista usando o comando
# dados.append('Pedro')
# indice:         0
# dados.append(25)
# indice:       1
# se eu der print(dados[0]) resultado: Pedro
# se eu der print(dados[1]) resultado: 25
# dados tem ['Pedro', 25]
# indices:      0      1

# e se eu quisse ter indices literais?
# Por exemplo ao invés de chamar pelo indice 0
# eu chamar pelo indice: nome, ou idade

# Fazemos isso através dos dicionários!
# Os dicionários são estrutura de dados semelhantes às tuplas e às listas
# só que desta vez eu consigo ter indices literais, eu consigo personalizar os indices

# tupla = ()     /  tupla = tuple()
# lista = []     / lista = list()
# Dicionário = {}    / dicionario = dict()

# lembra que na lista eu tinha:
# dados tem ['Pedro', 25]
# indices:      0      1

# Agora no dicionário eu tenho:
# dados {'nome':'Pedro', 'idade':25}
# dados {'Pedro', 25}
# ind:   nome,   idade

# o indice agora não é 0 ou 1
# E sim, nome ou idade

# dados {'nome':'Pedro', 'idade':25}
# Eu não posso mais dar print dados[0] ou print dados[1]
# Agora eu tenho que fazer por exemplo:
# print(dados['nome']) Resultado: Pedro
# print(dados['idade']) Resultado: 25

# E como que eu faço para adicionar elementos?
# No caso do dicionário o .append() não funciona
# Eu posso simplismente criar um novo elemento usando este comando:
# dados['sexo'] = 'M'

# Agora minha estrutura dados ficou dessa forma:
# dados('nome':'Pedro', 'idade':25, 'sexo',:'M'}

# No caso do dicionário para remover elementos eu uso o comando del
# Exemplo:
# del dados['idade']
# depois de dar este comando a minha estrutura dados ficou dessa forma:
# dados('nome':'Pedro', 'sexo',:'M'}

# Vou criar um dicionário para guardar nomes de filmes
# filme = {'titulo':'Star Wars',
#          'ano':1977,
#          'diretor':'George Lucas'
#          }

# Então eu tenho a estrutura de dados, com os seguintes elementos
# filme
# {'Star Wars', 1977, 'George Lucas'}   - valores/ .values()
#  'titulo',    'ano', 'diretor'        - elementos/ .keys()
# o Python chama esses elementos de keys

# se eu fizer:
# print(filme.values())
# print(filme.keys())

# E se eu quiser pegar todos os valores
# Por exemplo, eu quero tanto o values quanto o keys
# eu vou utilizar o .items()
# print(filme.items())

# Eu posso utilizar esse conceitos de values, keys, e items
# para utilizar nos laços, o for por exemplo:
# é bem parecido com o enumerate que utilizamos nas tuplas e nas listas

# {'Star Wars', 1977, 'George Lucas'}   - valores/ .values()
#  'titulo',    'ano', 'diretor'        - elementos/ .keys()

# vou criar uma variável k que é pra keys, e v que é pra values (já que eu tenho os dois dentro de items)

# for k, v in filme.items():        Pra cada {k} é a chave/ keys, e values no filme.items()
#       print(f'O {k} é {v}')       {k} = 'titulo', 'ano', 'diretor' / {v} = 'Star Wars', 1977, 'George Lucas'
# Resultado: O título é Star Wars
#            O ano é 1977
#            O diretor é George Lucas
# ele vai fazer 3 for, porque existe 3 items dentro de filme
# o primeiro for vai fazer {k} é {v} = O título é Star Wars
# o segundo for vai fazer {k} é {v} = O ano é 1977
# o terceiro for vai fazer {k} é {v} = O diretor é George Lucas
# depois dos 3 elementos ele não tem mais nenhum elemento, então ele termina a estrutura de repetição

# Podemos juntar listas, tuplas e dicionários:
# exemplo:
# Posso criar uma lista chamada: locadora
# E eu posso criar uma lista onde cada elemento tem um dicionário dentro
# as listas são identificadas por números e os dicionários por textos(podem ser números também)

# ===============================================================================

# pessoas = {'nome':'Gustavo', 'sexo':'M', 'idade':25}
# print(pessoas)     {'nome': 'Gustavo', 'sexo': 'M', 'idade': 25}
# print(pessoas[0])       KeyError: 0
# print(pessoas['nome'])      Gustavo
# print(pessoas['idade'])     25
# na hora de declarar eu vou usar chaves {}
# na hora de referênciar eu vou usar []
# print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')      O Gustavo tem 25 anos.
# print(pessoas.keys())       dict_keys(['nome', 'sexo', 'idade'])
# print(pessoas.values())     dict_values(['Gustavo', 'M', 25])

# print(pessoas.items())      dict_items([('nome', 'Gustavo'), ('sexo', 'M'), ('idade', 25)])
# Repara que no resultado desse print, foi uma composição de elementos
# ele disse que os items são, uma lista[], composta por 3 tuplas

# Eu posso também acessar as chaves, os valores e os items por laços
# pessoas = {'nome':'Gustavo', 'sexo':'M', 'idade':25}
# for k in pessoas.keys():
#     print(k)
# nome
# sexo
# idade

# pessoas = {'nome':'Gustavo', 'sexo':'M', 'idade':25}
# for k in pessoas.values():
#     print(k)
# Gustavo
# M
# 25

# Se eu quiser utilizar o items(), vou ter que colocar a chave e o valor:
# pessoas = {'nome':'Gustavo', 'sexo':'M', 'idade':25}
# for k, v in pessoas.items():
#     print(f'{k} = {v}')
# nome = Gustavo
# sexo = M
# idade = 25
# viu como é simples? Aqui eu não tenho o enumerate, que seria o enumerate para utilizar nas tuplas e nas listas
# No dicionário eu tenho que utilizar o items()

# Agora eu vou apagar um elemento /key
# pessoas = {'nome':'Gustavo', 'sexo':'M', 'idade':25}
# del pessoas['sexo']
# for k, v in pessoas.items():
#      print(f'{k} = {v}')
# nome = Gustavo
# idade = 25
# O elemento 'sexo' foi apagado pelo comando del


# Posso modificar:
# pessoas = {'nome':'Gustavo', 'sexo':'M', 'idade':25}
# pessoas['nome'] = 'Leandro'
# for k, v in pessoas.items():
#     print(f'{k} = {v}')
# nome = Leandro
# sexo = M
# idade = 25


# Posso adicionar:
# pessoas = {'nome':'Gustavo', 'sexo':'M', 'idade':25}
# pessoas['peso'] = 98.5
# for k, v in pessoas.items():
#     print(f'{k} = {v}')
# nome = Gustavo
# sexo = M
# idade = 25
# peso = 98.5
# Então funciona sem eu precisar dar o .append() pra isso

# ======================//=========================

# Agora eu vou criar um dicionário dentro de uma lista
'''brasil = []
estado1 = {'uf':'Rio de Janeiro', 'sigla':'RJ'}
estado2 = {'uf':'São Paulo', 'sigla':'SP'}
brasil.append(estado1)
brasil.append(estado2)'''
# print(estado1)      {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
# print(estado2)      {'uf': 'São Paulo', 'sigla': 'SP'}
# print(brasil)       [{'uf': 'Rio de Janeiro', 'sigla': 'RJ'}, {'uf': 'São Paulo', 'sigla': 'SP'}]
# indices:                           0                                          1
# E agora eu tenho uma lista com dicionários
# print(brasil[0])        {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
# print(brasil[1])        {'uf': 'São Paulo', 'sigla': 'SP'}
#print(brasil[0]['uf'])      Rio de Janeiro
#print(brasil[1]['sigla'])       SP

# ===========================//===========================

# Uma característica interessante:
# estado = dict()
# brasil = list()
# Eu vou querer ler 3 estados:
# for c in range(0, 3):
#     estado['uf'] = str(input('Unidade Federativa: '))
#     estado['sigla'] = str(input('Sigla do Estado: '))
    # ele vai ler isso 3x, depois disso eu tenho que adicionar à lista brasil
#     brasil.append(estado)
# print(brasil)       [{'uf': 'Acre', 'sigla': 'AC'}, {'uf': 'Acre', 'sigla': 'AC'}, {'uf': 'Acre', 'sigla': 'AC'}]

# Porque acre, ac.....?!
# estado = dict()
# brasil = list()
# for c in range(0, 3):
#     estado['uf'] = str(input('Unidade Federativa: '))
#     estado['sigla'] = str(input('Sigla do Estado: '))
#     brasil.append(estado[:])
# print(brasil)         deu erro!
# brasil.append(estado[:])
#               ~~~~~~^^^
# KeyError: slice(None, None, None)

# Porque deu erro? Porque eu não posso fazer fatiamento
# Então como eu posso fazer uma copia do elemento sem fazer um fatiamento?

# No caso do dicionário existe um metodo interno, que é o metodo copy()
# estado = dict()
# brasil = list()
# for c in range(0, 3):
#     estado['uf'] = str(input('Unidade Federativa: '))
#     estado['sigla'] = str(input('Sigla do Estado: '))
#     brasil.append(estado.copy())
#print(brasil)
# [{'uf': 'Minas Gerais', 'sigla': 'Mg'}, {'uf': 'Acre', 'sigla': 'AC'}, {'uf': 'Parana', 'sigla': 'PR'}]


# da pra fazer mais bonito!

# estado = dict()
# brasil = list()
# for c in range(0, 3):
#     estado['uf'] = str(input('Unidade Federativa: '))
#     estado['sigla'] = str(input('Sigla do Estado: '))
#     brasil.append(estado.copy())
# for e in brasil:    # para cada estado em brasil
#     print(e)
# {'uf': 'Rio', 'sigla': 'RJ'}
# {'uf': 'Sampa', 'sigla': 'SP'}
# {'uf': 'Paraná', 'sigla': 'PR'}


# estado = dict()
# brasil = list()
# for c in range(0, 3):
#     estado['uf'] = str(input('Unidade Federativa: '))
#     estado['sigla'] = str(input('Sigla do Estado: '))
#     brasil.append(estado.copy())
# for e in brasil:    # esse for de fora, é da lista
#     for k, v in e.items():   # esse for de dentro, para o dicionário
#         print(f'O campo {k} tem valor de {v}.')
# O campo uf tem valor de Rio de Janeiro.
# O campo sigla tem valor de RJ.
# O campo uf tem valor de São Paulo.
# O campo sigla tem valor de SP.
# O campo uf tem valor de Goiás.
# O campo sigla tem valor de GO.


estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for v in e.values():     # posso colocar só para valor
#        print(v)
# Rio
# RJ
# Sampa
# SP
# Bahia
# BA
        print(v, end=' ')
    print()
# Acre AC
# Amazonas AM
# Pará PA
