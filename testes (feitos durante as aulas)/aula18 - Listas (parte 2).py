# Nessa aula, vamos aprender o que são LISTAS e como utilizar listas em Python.
# As listas são variáveis compostas que permitem armazenar vários valores em uma mesma estrutura,
# acessíveis por chaves individuais.
#-----------------------------------------------

'''teste = list()
teste.append('Gustavo')
teste.append(40)
#print(teste)    # ['Gustavo', 40]
galera = list()
galera.append(teste)
print(galera)    # [['Gustavo', 40]]'''

# -------------------------------------------
'''teste = list()      # Criei uma lista
teste.append('Gustavo')     # essa lista recebe 'Gustavo'
teste.append(40)            # essa lista recebe 40
galera = list()             # criei outra lista chamada galera
galera.append(teste)        # joguei a lista teste dentro da lista galera
teste[0] = 'Maria'          # Quero que o teste na posição "0" mude de 'Gustavo' para 'Maria'
teste[1] = 22              # Quero que o teste na posição "1" mude de 40 para 22
galera.append(teste)        # dei mais um append
print(galera)    # [['Maria', 22], ['Maria', 22]]'''       # porque que isso aconteceu?
# Quando eu faço um append (como na linha 14) ali, eu estou criando uma ligação entre as duas estruturas
# Então se eu mudar a primeira estrutura que é o teste, automaticamente muda a segunda estrutura que é o galera

'''teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:])     # Então aqui eu tenho que fazer uma copia [:]
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])     # e aqui também outra cópia [:]
print(galera)      # [['Gustavo', 40], ['Maria', 22]]'''

# posso fazer a declaração de galera de uma outra maneira
galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]        # Aqui eu tenho 4 estruturas compostas, dentro de uma estrutura grande
#print(galera)   # [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
#print(galera[0])    # ['João', 19]
#print(galera[0][0])     # João
#print(galera[2][1])     # 13
#for p in galera:
#    print(p)
    # Resultado:
    # ['João', 19]
    # ['Ana', 33]
    # ['Joaquim', 13]
    # ['Maria', 45]

# se eu quiser só os nomes?
#for p in galera:
#    print(p[0])
    # Resoltado:
    # João
    # Ana
    # Joaquim
    # Maria

# só a idade?
#for p in galera:
#    print(p[1])
    # Resultado:
    # 19
    # 33
    # 13
    # 45

# Um print formatado!
#for p in galera:
#    print(f'{p[0]} tem {p[1]} anos de idade')
    # Resultado:
    # João tem 19 anos de idade
    # Ana tem 33 anos de idade
    # Joaquim tem 13 anos de idade
    # Maria tem 45 anos de idade

# ------------------------------------
# Outra coisa que eu posso fazer é pedir nome e idade
'''galera = list()
dado = list()       # lista temporária onde eu vou pegar os dados de 3 pessoas e vou jogar tudo pra lista [galera]
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))  # Li o nome e a idade e joguei na estrutura dado
    galera.append(dado[:])      # Coloquei uma cópia do dado dentro da estrutura galera
    dado.clear()        # peguei a estrutura dado e exluí os dados anteriormente recebidos
print(galera)   # [['Pedro', 22], ['Maria ', 22], ['Claudia', 55]]'''
#
'''galera = list()
dado = list()
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado)      # Se eu esquecer o [:], olha o que acontece!
    dado.clear()
print(galera)   # [[], [], []]'''
# porque isso aconteceu?
# Porque quando eu dou clear, eu dou clear tanto no [dado], quanto na [galera]
# já que eles estão ligados, porque eu não mandei criar uma cópia de [dado]

# outra coisa que podemos fazer é...
# eu quero mostrar só as pessoas que tem mais de 21 anos

galera = list()     # Criei a primeira estrutura
dado = list()       # Criei a segunda estrutura, que vai ser uma estrutura secundária, que eu vou pegar os dados dela e jogar na primeira estrutura
total_maior = total_menor = 0       # Vou ver o total maior e menor de idade

for c in range(0, 3):       # Essa primeira estrutura for, é pra mim ler [dado] e jogar dentro da [galera]
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()    # Apagando [dado] a cada vez que eu faço o laço

# Aqui eu analiso para saber, se a pessoa é maior ou menor de idade, e já vou totalizando pra mostrar quantos são maiores e quantos são menores
for p in galera:    # Para cada pessoa em [galera]
    if p[1] >= 21:      # Se a idade p[1] foi maior ou igual à 21
        print(f'{p[0]} é maior de idade.')      # Escreva esses dadoos
        total_maior += 1
    else:
        print(f'{p[0]} é menor de idade.')
        total_menor += 1
print(f'Temos {total_maior} maiores e {total_menor} menores de idade.')
# Resultado:
# Cleiton é maior de idade.
# Elaine é menor de idade.
# Caio é maior de idade.
# Temos 2 maiores e 1 menores de idade.