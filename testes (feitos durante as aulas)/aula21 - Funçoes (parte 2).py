# Nessa aula, vamos continuar nossos estudos de funções em Python,
# aprendendo mais sobre Interactive Help em Python,
# o uso de docstrings para documentar nossas funções,
# argumentos opcionais para dar mais dinamismo em funções Python,
# escopo de variáveis e retorno de resultados.

# ==========================//=======================================

# INTERACTIVE HELP: (ajuda interativa)

# para usar a ajuda interativa do Python é muito simples!
# basta digitar:
# help()
# na verdade uma função interna
# quando eu abro e fecho parênteses depois de um nome, isso é uma função! isso é um metodo!
# posso abrir ele no prompt de comando do python
# ou por aqui mesmo
# quando eu executar help()
# (é só isso mesmo!)
# ele vai abrir uma ajuda interativa
# e se eu quiser saber mais sobre determinado metodo, biblioteca, função
# e se eu der escrever:
# quit
# ele vai sair desse prompt
# eu também posso pedir dessa forma:
# por exemplo se eu der help(print)
# ele vai me ensinar todas as funções dentro de print
# me dando uma explicação sobre o que eu pedi
# e existe uma outra maneira também que é imprimir um doc interno
# (input.__doc__)
# Não necessáriamente a mesma do help()
# Vamos executar os dois pra vc ver como funciona os dois juntos
'''help(input)
print('-' * 30)
print(input.__doc__)'''
# essa são duas maneiras de fazer
# talvez mude apenas a formatação
# Mas eu gostei mais do help()


# ================================//=============================

# DOCSTRINGS: (String de Documentação)
# quando eu dou help(input)
# ele me mostra a docstring do comando input, mostra o manual do comando input
# e todas as funcionalidades internas do Python tem a sua docstring
# Vamos pra um exemplo prático de uma função que vamos criar!

'''def contador(i, f, p):  # parâmetros reais
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('FIM!')


contador(2, 10, 2)  # parâmetros formais, faz uma cópia dos valores e envia para parâmetros reais'''

# existe uma cópia dos valores dos parâmetros formais, que ficam embaixo no programa principal: contador(2, 10, 2)
# para os parâmetros reais que são os que ficam lá em cima na função: def contador(i, f, p)

# se foi eu que criei essa função contador() então eu sei o que que é contador(i, f, p)
# Mas e se não fui eu que criei essa função?
# Se alguem está utilizando a minha funcionalidade?

# será que seu eu der um help(contador)
# ele vai me mostrar um manual?
# help(contador)  # contador(i, f, p)
# não adiantou nada pra mim! Ao menos eu sei que ele tem 3 parâmetros

# Para que eu possa utilizar o comando help(contador) e ele me dar um manual da minha função
# é só utilizar as docstrings
# a docstring ela começa exatamente depois do comando def
# e como eu faço uma docstring?
# É só abrir aspas duplas " 3x embaixo do comando def: """
# Depois de fazer isso você pode colocar um manual completo (ou 3 aspas simples também dá, testei aqui!)

'''def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela.
    :param i: Início da contagem
    :param f: Fim da contagem
    :param p: Passo da contagem
    :return: Sem retorno
    Função criada por Gustavo Guanabara do canal CursoemVideo.
    """
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('FIM!')


help(contador)'''

# o que está entre essas aspas logo na linha abaixo de def
# é a docstrings
# E logo a partir desse momento, se esse comando for importado eu consigo ter a docstring dele
# e consigo ajudar o meu programador ou usuário que estiver programando e usando a minha funcionalidade.


# =====================================//====================================

# PARAMÊTROS OPCIONAIS

'''
def somar(a, b, c):
    """
    -> Faz a soma de três valores e mostra o resultado na tela.
    :param a: O primeiro valor
    :param b: O segundo valor
    :param c: O terceiro valor
    Função criada por Gustavo Guanabara do canal CursoemVideo.
    """
    s= a + b + c
    print(f'A soma vale {s}')


somar(3, 2, 5)      # A soma vale 10
somar(3, 2)     # TypeError: somar() missing 1 required positional argument: 'c'
'''

# Repara que ao tentar executar o segundo comando da erro
# Porque o parâmetro c não foi informado
# E como resolvemos isso?
# Simples, lá em cima em def
# eu vou colocar c=0, e dessa forma ele se torna um PARÂMETRO OPCIONAL (informo ou não o c)
# ou seja se não tiver o parâmetro c, c vai ser igual a zero
# e posso fazer isso com todos os outros parâmetros também!

'''
def somar(a, b, c=0):
    """
    -> Faz a soma de três valores e mostra o resultado na tela.
    :param a: O primeiro valor
    :param b: O segundo valor
    :param c: O terceiro valor
    Função criada por Gustavo Guanabara do canal CursoemVideo.
    """
    s= a + b + c
    print(f'A soma vale {s}')


somar(3, 2, 5)      # A soma vale 10
somar(3, 2)     # A soma vale 5
'''

# Prox exemplo:
'''
def somar(a, b, c=0):
    """
    -> Faz a soma de três valores e mostra o resultado na tela.
    :param a: O primeiro valor
    :param b: O segundo valor
    :param c: O terceiro valor
    Função criada por Gustavo Guanabara do canal CursoemVideo.
    """
    s= a + b + c
    print(f'A soma vale {s}')


somar(3, 2, 5)      # A soma vale 10
somar(3)     # TypeError: somar() missing 1 required positional argument: 'b'
'''

# Para resolver esse erro é só transformar o parâmetro b=0
# Vou fazer com todos!

'''
def somar(a=0, b=0, c=0):
    """
    -> Faz a soma de três valores e mostra o resultado na tela.
    :param a: O primeiro valor
    :param b: O segundo valor
    :param c: O terceiro valor
    Função criada por Gustavo Guanabara do canal CursoemVideo.
    """
    s= a + b + c
    print(f'A soma vale {s}')


somar(3, 2, 5)      # A soma vale 10
somar(3)     # A soma vale 3
somar()     # A soma vale 0
somar(3, 3, 5)      # A soma vale 11
somar(3, 3, 5, 8)       # TypeError: somar() takes from 0 to 3 positional arguments but 4 were given
'''


# Ou seja posso informar de 0 a 3 parâmetros
# Caso eu deseje informar mais do que isso eu utilizo * dentro da função def


# =====================================//============================================

# ESCOPO DE VARÁVEIS (escopo de declarações)

# basicamente na programação escopo é o local onde uma variável vai existir
# e o local onde a variável não vai mais existir
# vamos para a explicação:


'''#                   => Escopo Global(fora de def)
def teste():                # => escopo local(dentro de def)
    x = 8
    print(f'Na função teste, n = {n}')
    print(f'Na função teste, x vale {x}')
                            # => escopo local(dentro de def)
# dentro de def o escopo é local,
# por isso a variável x vai funcionar somente dentro do escopo local


# Programa Principal
n = 2
print(f'No programa principal, n = {2}')
teste()
print(f'No programa principal, x vale {x}')
# e a variável n vai funcionar dentro do escopo global,
# ou seja vai funcionar até dentro do escopo local


#                   => Escopo Global(fora de def)'''

# Sáida:
# No programa principal, n = 2
# Na função teste, n = 2
# Na função teste, x vale 8
# (tentativa de printar o x no programa principal)   # NameError: name 'x' is not defined

# Mesmo n sendo definido no programa principal ele vai funcionar dentro de todo o Escopo Global

# Vamos fazer um teste:

'''def funçao():
    n1 = 4
    print(f'N1 escopo local = {n1}')        # dentro


n1 = 2
funçao()
print(f'N1 escopo global = {n1}')       # fora

# saída:
# N1 escopo local = 4
# N1 escopo global = 2'''

# Vou utilizar de um exemplo mostrado na aula, para servir de anotação!
# vamos aprender o comando global
# por exemplo se eu quiser usar o n1 do escopo global no escopo local
# eu tenho que fazer o seguinte:
# adicionar a função
# global n1 (ou o nome correspondente à variável)

'''
def teste(b):       # parâmetro a representado pela letra b
    a = 8       # a recebe 8 (escopo local)
    b += 4      # b recebe ele mesmo + 4
    c = 2       # c recebe 2
    print(f'A no escopo local vale {a}')
    print(f'B no escopo local vale {b}')
    print(f'C no escopo local vale {c}')


# Programa principal /Escopo Global
a = 5       # a recebe 5 (escopo global)
teste(a)    # teste recebe o parâmetro a
print(f'A no escopo global vale {a}')

# Saída: 
# A no escopo local vale 8
# B no escopo local vale 9
# C no escopo local vale 2
# A no escopo global vale 5'''

'''
def teste(b):       # parâmetro a representado pela letra b
    global a        # função global estou dizendo, por favor não crie uma variável a, use o a global
    a = 8       # dada a função global a, o escopo local não muda! o que muda é o escopo global
    b += 4      # b recebe ele mesmo + 4
    c = 2       # c recebe 2
    print(f'A no escopo local vale {a}')
    print(f'B no escopo local vale {b}')
    print(f'C no escopo local vale {c}')


# Programa principal /Escopo Global
a = 5       # a recebe 8 (por causa da função global)
teste(a)    # teste recebe o parâmetro a
print(f'A no escopo global vale {a}')     # Resultado recebe a variável do escopo local, e não usa a variável a global

# Saída:
# A no escopo local vale 8
# B no escopo local vale 9
# C no escopo local vale 2
# A no escopo global vale 8     # perdeu o valor 5 que tinha anteriormente'''

# ==============================//===============================

# RETORNANDO VALORES
# return

# As funções em Python elas podem não retornar, ou retornar um valor
# e pra isso utilizamos o return

'''
def somar(a=0, b=0, c=0):
    s = a + b + c
    print(f'A soma vale {s}')


somar(3, 2, 5)
somar(2, 2)
somar(6)

# Saída: 
# A soma vale 10
# A soma vale 4
# A soma vale 6
'''

# percebe que todos eles seguem um padrão
# eles escrevem o resultado da mesma maneira
# A soma vale 10
# A soma vale 4
# A soma vale 6

# está é a limitação de não se utilizar o return
# vamos entender melhor:
# vou tirar o print e colocar o return, significa que eu vou dar um retorno pra variável s

'''
def somar(a=0, b=0, c=0):   # os parâmetros do escopo local, vão receber ser preenchidas com os parâmetros informados
    s = a + b + c       # s vai somar os parâmetros recebidos em a, b, c
    return s        # ele vai retornar o s, para o que vier antes de somar() no programa principal


# Programa Principal
# então aqui eu vou ter que colocar alguma coisa antes, por exemplo resp =
resp = somar(3, 2, 5)       # resp vai receber o return de s
print(resp)         # Saída: 10

# ou eu também posso colocar dentro de um print
print(somar(3, 2, 5))       # Saída: 10

# Posso fazer isso também!!!
r1 = somar(3, 2, 5)
r2 = somar(1, 7)
r3 = somar(4)
print(f'Meus cálculos deram {r1}, {r2} e {r3}.')        # Saída: Meus cálculos deram 10, 8 e 4.
'''

# Funções que retornam resultados, são muito úteis quando eu quero ter uma personalização dos resultados

# vamos fazer alguns exercícios na prática!

'''
def fatorial(num=1):    # se eu não informar um valor, num vale 1
    f = 1       # varável f, que é o fatorial valendo 1
    for c in range(num, 0, -1):     # vai começar em um número e vai até zero, de 1 em 1
        f *= c      # f recebe f vezes c
    return f


n = int(input('Digite um número: '))
print(f'O fatorial de {n} é igual à {fatorial(n)}')
# Saída: O fatorial de 5 é igual à 120
'''

# vamos executar isso de outra maneira

'''
def fatorial(num=1):    # se eu não informar um valor, num vale 1
    f = 1       # varável f, que é o fatorial valendo 1
    for c in range(num, 0, -1):     # vai começar em um número e vai até zero, de 1 em 1
        f *= c      # f recebe f vezes c
    return f


f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são: {f1}, {f2} e {f3}')

# Saída: Os resultados são: 120, 24 e 1
'''

# vamos para outro exemplo!

'''
def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um número: '))
print(par(num))

# Saída:
# Digite um número: 15
# False

# Digite um número: 84
# True
'''

# Ainda neste ultimo exemplo

def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um número: '))
print(par(num))
if par(num):    # se num for par
    print('É par!')
else:
    print('Não é par!')
    
# Saída:
# Digite um número: 5
# False
# Não é par!

# Digite um número: 8
# True
# É par!
