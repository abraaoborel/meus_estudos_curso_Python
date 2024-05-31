'''
nome = str(input('Qual é o seu nome? '))
print(f'Tenha um bom dia {nome}!')
if nome == 'Abraão':
    print('Este é um escolhido por Deus, para ser Pai de muitas Nações!')
# Utilizamos apenas um if, chamamos isso de condição simples
'''

# Vamos criar agora uma condição composta:

'''
nome = str(input('Qual é o seu nome? '))
if nome == 'Abraão':
    print('Este é um escolhido por Deus, para ser Pai de muitas Nações!')
else:
    print('Seu nome é bem normal')
print(f'Tenha um bom dia {nome}!')
'''

# Isto é o que chamamos de estrutura condicional composta
# Vamos dar uma aprimorada nesse programa colocando um elif, posso utilizar mais de um elif
# e é o que vamos fazer a seguir:

nome = str(input('Qual é o seu nome? '))
if nome == 'Abraão':
    print('Este é um homem escolhido por Deus, para ser Pai de muitas Nações!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome feminino')
else:
    print('Seu nome é bem normal')
print(f'Tenha um bom dia {nome}!')

# Esta estruta acima, é uma estrutura condicional aninhada
# É assim que chamamos essa estrutura na programação
# Ela é aninhada, porque está num formato de ninho
# um ninho, dentro do outro, etc...