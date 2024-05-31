# Nessa aula, vamos ver como o Python permite tratar erros e criar respostas a essas exceções.
# Aprenda como usar a estrutura try except no Python de uma forma simples.
# =====================//===========================

# ERROS ACONTECEM, SEMPRE!
# E VOCÊ DEVE ESTAR PREPARAD0 PARA TRATAR ESSAS FALHAS/ERROS

# exemplo:
# primt(x)
# isso é um erro de sintaxe, porque eu troquei as letras
# Mas não é esse tipo de erro que estou falando

# print(x)
# é esse daqui!
# Saída: NameError: name 'x' is not defined
# isso porque eu não inicializei a variável x, ou porque x não existe
# isso não é um erro de sintaxe, é um erro semântico
# ou seja, mesmo que você digite um comando certinho isso pode acarretar um erro

# quando esse erro não se da de forma sintática
# nós chamamos esse erro de Exceção
# nesse caso uma Exceção chamada NameError

# Quer ver outro erro muito comum
# n = int(input('Número: '))
# print(f'Você digitou o número {n}')
# Se o usuário digitar por exemplo, oito
# Saída: ValueError: invalid literal for int() with base 10: 'oito'
# É um erro de valor, isso porque ele estava esperando receber um número inteiro
# e acabou recebendo um valor do tipo string
# Sendo assim ele deu um erro na hora da atribuição de n
# porque eu digitei um valor errado, eu digitei a palavra 'oito' e a palavra 'oito'
# não pode ser convertida para inteiro pela função int, e isso disparou a Exceção ValueError

# Mais um exemplo:
# a = int(input('Numerador: '))
# b = int(input('Denominador: '))
# r = a / b
# print(f'O resultado é {r}')
# Repara que não tem erro sintático nenhhum!
# Se eu digitar a palavra 'oito', vai dar o problema que vimos anteriormente
# Mas esse tem outro problema!
# Se eu digitar por exemplo, Saída:
# Numerador: 8
# Denominador: 0
# ZeroDivisionError: division by zero
# Na matemática divisão por zero é um problema!
# Ela não existe no campo dos números inteiros e reais
# E nesse caso ele me deu uma outra Exceção
# ZeroDivisionError: division by zero

# Mais um exemplo:
# r = 2 / '2'
# Esse valor '2' é um número?
# Algumas linguagens de programação até considerariam um número como JavaScript e PHP
# Só que o Python não
# Para o Python isso é um TypeError, ou um erro de tipo

# Mais um exemplo:
# lista = [3, 6, 4]
# print(lista[3])
# Como não existe o index 3
# vai dar um erro
# Nesse caso vamos ter uma Exceção do tipo IndexError
# No caso dos dicionários, KeyError

# Um outro exemplo, da ultima aula a 22
# sobre importar modulos
# por exemplo
# import uteis
# se esse arquivo uteis.py não for encontrado
# ele vai disparar uma Exceção
# e essa Exceção se chama
# ModuleNotFoundError

# e existe muitas Exceções
# Mas eu não preciso decorar ou aprender todas elas
# Elas vão começar a acontecer
# Já identificamos onde está o nome da Exceção

# Toda Exceção no Python é filho de uma classe maior
# chamada Exception
# sempre quando você ver essa palavra Exception você vai ler como exceção
# Na verdade é meio que um erro, mas um erro que não ocorre sempre
# Você digitou um comando certo, não é um erro sintático
# Mas ele está acontecendo e isso é sempre tratado como uma Exceção

# Vamos aprender como lidar com as Exceções, como tratar as Exceções
# Para tratar uma Exceção com Python
# vamos utilizar a estrutura try: (tente) except: (senão)
# por exemplo:
# try: (Tente Alguma coisa)
#   (operação)
#   Aqui dentro vamos colocar o que geralmente pode dar problema
#   Qual é o comando, ou quais são os comandos que geralmente dão problema
# except: (Senão acontece uma Exceção)
#   (falhou)
#   Isto é, se eu tentar o try, e falhar
#   O que que vai acontecer?


# Vamos ver isso na prática!
# Vamos usar um dos exemplos que foi feito acima:
'''try:        # Vou tentar fazer esses 3 comandos aqui
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except:     # Se der problema
    print('Infelizmente tivemos um problema. =(')
print(f'O resultado é {r}')
# Saída:
# Numerador: oi
# Infelizmente tivemos um problema. =(
# NameError: name 'r' is not defined'''

# Ok, mas e se não der problema?
# Aí nesse caso eu vou usar o else

'''try:        # Vou tentar fazer esses 3 comandos aqui
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except:     # Se der problema
    print('Infelizmente tivemos um problema. =(')
else:       # Deu certo (se o meu try deu certo!)
    print(f'O resultado é {r:.1f}')
# Saída:
# Numerador: oi
# Infelizmente tivemos um problema. =(
# ou
# Numerador: 5
# Denominador: 0
# Infelizmente tivemos um problema. =(
# Repara que já não tem mais mensagem de erro!
# Isso é um tratamento de erro!'''

# Ainda temos mais uma clausula que podemos colocar!
# E Está ultima clausula é o finally (Se deu certo, ou se deu um erro, ele vai acontecer)
# As clausulas else e finallu são opcionais, nem sempre você precisa usar.
# Mas nesse caso vamos usar!

# Vamos voltar ao exemplo anterior:

'''try:        # Vou tentar fazer esses 3 comandos aqui
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except:     # Se der problema
    print('Infelizmente tivemos um problema. =(')
else:       # Deu certo (se o meu try deu certo!)
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte Sempre! Muito Obrigado!')
# Saída:
# Numerador: oi
# Infelizmente tivemos um problema. =(
# Volte Sempre! Muito Obrigado!'''

# Inclusive, podemos tratar esse erro, mostrando o que aconteceu!
# Vejamos:

'''try:        # Vou tentar fazer esses 3 comandos aqui
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except Exception as erro:     # Chamei aquela classe principal Exception, e atribuí ela à uma variável erro
    print(f'Problema encontrado foi {erro.__class__}')
else:       # Deu certo (se o meu try deu certo!)
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte Sempre! Muito Obrigado!')
# Saída:
# Numerador: 5
# Denominador: oi
# Problema encontrado foi <class 'ValueError'>
# Volte Sempre! Muito Obrigado!
# Saída:
# Numerador: 7
# Denominador: 0
# Problema encontrado foi <class 'ZeroDivisionError'>
# Volte Sempre! Muito Obrigado!'''

# Claro que você não vai mostrar isso pro usuário
# Mas enquanto você estiver desenvolvendo, você vai poder capturar o erro
# E mostrar na tela uma mensagem personalizada
# E essa mensagem personalizada é possível porque essa estrutura pode se expandir muito!
# Na verdade todo try pode ter mais de um Exception
# E cada um deles com sua própria mensagem com seu próprio tratamento

# Vamos continuar no exemplo prático:

try:
    a = int(input('Numerador: '))       # Posso criar um try para cada ação, um try pro a, um try pro b, um try pro r
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou.')
except ZeroDivisionError:
    print('Não é possível dividir um número por zero!')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados!')
#except Exception as erro:       # Forma genérica
#    print(f'O erro encontrado foi {erro.__cause__}')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte Sempre! Muito Obrigado!')
