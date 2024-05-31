# ================================//============================
#                        ABSTRAÇÃO
# ================================//============================

# Anotação: A Abstração garante que cada objeto é algo único.

# A classe é a abstração do objeto
# Orientação a objeto é tentar levar algo do mundo real para o computador, do modo que ele funciona na vida real.

# classe abstração é só a definição
# já o objeto é a minha instância criada
# ou seja, é uma variável diferente, é um dado novo

# imagina que a classe é apenas um molde
# mas quando eu coloco todos os elemento lá dentro, e sai uma objeto novo
# eu tenho o objeto criado

# vamos fazer a abstração:
# class Caneca:
#     logo = ''
#     cor = ''
#     nome = ''
# # com isso eu já posso criar um objeto dessa classe
# caneca1 = Caneca()
# # Para acessar as propriedades, logo, cor e nome
#
# caneca1.nome = 'Teste'
# caneca1.logo = 'Logo'
# caneca1.cor = 'Verde'
# # Quando eu coloco ponto, eu tenho acesso a tudo que pertence essa classe
#
# print(caneca1.nome, caneca1.logo, caneca1.cor)      # Sáida: Teste Logo Verde


# ==========================//================================

# Eu também posso ter métodos, que são as funções da classe
# class Caneca:
#     logo = ''
#     cor = ''
#     nome = ''
#
#     def beber(self):        # O self vai especificar, qual o objeto que está chamando este método/função
#         print('Estou bebendo da caneca', self.nome)
#         # Por exemplo, se eu peço caneca1.beber() quem está chamando beber() é a caneca1, então é ela que entra no self
#         # Então nesse caso, self.nome vai ser preenchido com o nome definido em caneca1
#         # Repara que eu não preciso passar esse parâmetro,
#         # porque o self é passado sozinho, sendo o objeto que chamou o método
#
#
# caneca1 = Caneca()
# caneca1.nome = 'Teste'
# caneca1.logo = 'Logo'
# caneca1.cor = 'Verde'
#
#
# caneca1.beber()     # Saída: Estou bebendo da caneca Teste

# ==========================//================================
# Também posso fazer o seguinte:

# class Caneca:
#     logo = ''
#     cor = ''
#     nome = ''
#
#     def beber(self):
#         print('Estou bebendo da caneca', self.nome)
#
#
# caneca1 = Caneca()
# caneca1.nome = 'Teste'
# caneca1.logo = 'Logo'
# caneca1.cor = 'Verde'
#
#
# Caneca.logo = 'Padrão'      # Vou modificar aqui direto da classe
#
# # Vou criar a caneca2
# caneca2 = Caneca()
# print(caneca2.logo)     # Saída: Padrão

# Repara que ele printou Padrão, porque eu modifiquei da classe, eu não modifiquei do objeto
# E isso é muito ruim quando estamos trabalhando com orientação a objetos
# Quando agente tenha uma propriedade que é unica de cada objeto, ela não vai ser geral da classe

# Eu poderia ter uma característica geral aqui
# Por exemplo:

# class Caneca:
#     formato = 'Cilíndrico com alça lateral'
# Este é um formato de uma classe, ou seja toda caneca vai ser isso
# Se por ventura alguém falar, agora caneca são triângulares, eu vou ter que fazer o seguinte
# Vamos começar do zero.

#
#      def __init__(self):        # Esté é o método sempre que o python cria um objeto
# Lembra quando eu pus caneca1 = Caneca()
# Então o python já tem dentro dele esse método init
# Por isso que quando fazemos isso agora, caneca1 = Caneca()
# Agora precisamos preencher esses parênteses aqui
# Porque é uma chamada ao método init

# class Caneca:
#     formato = 'Cilíndrico com alça lateral'
#     def __init__(self):
# O que essa função init vai fazer? Ela vai criar um objeto de acordo com o que eu passar pra ela trabalhar

# class Caneca:
#     formato = 'Cilíndrico com alça lateral'     # Estático, vai ser sempre o mesmo para todas as canecas
#
#     def __init__(self, nome, logo, cor):
#         # Então agora sempre que eu criar uma caneca eu preciso passar o nome, logo e cor
#         self.nome = nome        # Já esses itens vão mudar de caneca para caneca
#         self.logo = logo
#         self.cor = cor
#         self.status = 'Cheia'   # Por padrão vou colocar que toda caneca vai vir cheia
#
#     def beber(self):
#         self.status = 'Vazia'
#
#     def encher(self):
#         self.status = 'Cheia'
#
# # Vamos fazer um teste para ver o que está acontecendo
#
# caneca1 = Caneca('Caneca Londrina', 'Cidade de Londres', 'Branca')
# caneca2 = Caneca('Caneca ByLearner', 'Foguete da Bylearn', 'Branca')
#
# print(f'A caneca {caneca1.nome} possui a logo {caneca1.logo}')
# print(f'A caneca {caneca2.nome} possui a logo {caneca2.logo}')
#
# caneca1.beber()
# caneca1.encher()
#
# caneca2.beber()
#
# print('Caneca 1:', caneca1.status)
# print('Caneca 2:', caneca2.status)

# Sáida:
# A caneca Caneca Londrina possui a logo Cidade de Londres
# A caneca Caneca ByLearner possui a logo Foguete da Bylearn
# Caneca 1: Cheia
# Caneca 2: Vazia


# ================================//============================
#                        HERANÇA
# ================================//============================
# Herança é o Segundo Pilar da Orientação a Objetos

# Vamos pensar o seguinte, você herdou várias coisas do seu pai
# Os seu pais herdaram várias coisas dos seus avós, e assim por diante
# de sempre pegar os atributos e as definições de seus antepassados

# Eu posso falar que eu sou filho dos meus pais, e se meus pais são seres humanos
# E seres humanos tem como propriedade um nome, idade
# E como método tem a função de respirar
# Eu posso falar que como eu sou filho deles eu herdei tudo isso
# Então eu também sei respirar, também tenho um nome, e uma idade
# Porque todo ser humano tem e eu herdei essa característica dos meus pais

# A mesma coisa acontece no Python
# Nos podemos ter as classes pais e as classes filhas
# Onde as classes filhas herdam todas as propriedades e métodos da classe pai

# então o que que eu vou fazer, eu vou criar uma classe caneca londrina
# que vai herdar da classe Caneca todos os atributos que ela tem

# Vamos ao código:

# class Caneca:
#     formato = 'Cilíndrico com alça lateral'
#
#     def __init__(self, nome, logo, cor):
#         self.nome = nome
#         self.logo = logo
#         self.cor = cor
#         self.status = 'Cheia'
#
#     def beber(self):
#         self.status = 'Vazia'
#         return f'É da {self.nome} que eu estou bebendo'     # self.nome se refere ao objeto que está chamando a função
#
#     def encher(self):
#         self.status = 'Cheia'
#         return f'Estou enchendo a {self.nome}'      # A mesma coisa aqui
#
# # O que eu fiz aqui???
# # Eu criando a Classe CanecaLondrina que herda de Caneca, então ela tem todas as propriedades de uma caneca
# class CanecaLondrina(Caneca):
#     def __init__(self):
#         self.nome = 'Caneca Londrina'
#         self.logo = 'Cidade de Londres'
#         self.cor = 'Branca'
#         self.status = 'Cheia'
#
#     # Lembra que quando eu herdo eu trago todas as propriedades e todos os métodos?
#     # Então a Caneca Londrina, já vai ter o método/função beber(), e o método/função encher()
#     # Assim como também já vai ter o formato Cilíndrico com alça lateral
#
# # Eu não preciso passar nada além do self, porque?
# # Porque tanto o nome, quanto a logo, quanto a cor eu já sei qual vão ser
# # Que vão ser essas daqui:
# # caneca1 = Caneca('Caneca Londrina', 'Cidade de Londres', 'Branca')
# # caneca2 = Caneca('Caneca ByLearner', 'Foguete da Bylearn', 'Branca')
# # Então eu não preciso ficar passando toda hora a informação
#
# caneca1 = CanecaLondrina()        # Repara que aqui, eu coloquei a caneca1, recebendo a CanecaLonrina
# caneca2 = Caneca('Caneca ByLearner', 'Foguete da Bylearn', 'Branca')
#
# print(f'A caneca {caneca1.nome} possui a logo {caneca1.logo}')
# print(f'A caneca {caneca2.nome} possui a logo {caneca2.logo}')
#
# print(caneca1.beber())      # depois que eu coloquei o return, na função eu chamei o print
# print(caneca1.encher())     # A mesma coisa aqui
#
# print(caneca2.beber())      # E aqui também
#
# print('Caneca 1:', caneca1.status)
# print('Caneca 2:', caneca2.status)
#
# print(caneca1.formato)

# Saída:
# A caneca Caneca Londrina possui a logo Cidade de Londres
# A caneca Caneca ByLearner possui a logo Foguete da Bylearn
# É da Caneca Londrina que eu estou bebendo
# Estou enchendo a Caneca Londrina
# É da Caneca ByLearner que eu estou bebendo
# Caneca 1: Cheia
# Caneca 2: Vazia
# Cilíndrico com alça lateral


# Vou limpar esse código para continuarmos:

# class Caneca:
#     formato = 'Cilíndrico com alça lateral'
#
#     def __init__(self, nome, logo, cor):
#         self.nome = nome
#         self.logo = logo
#         self.cor = cor
#         self.status = 'Cheia'
#
#     def beber(self):
#         self.status = 'Vazia'
#         return f'É da {self.nome} que eu estou bebendo'     # self.nome se refere ao objeto que está chamando a função
#
#     def encher(self):
#         self.status = 'Cheia'
#         return f'Estou enchendo a {self.nome}'      # A mesma coisa aqui
#
# class CanecaLondrina(Caneca):
#     def __init__(self):
#         self.nome = 'Caneca Londrina'
#         self.logo = 'Cidade de Londres'
#         self.cor = 'Branca'
#         self.status = 'Cheia'
#
# caneca1 = CanecaLondrina()        # Repara que aqui, eu coloquei a caneca1, recebendo a CanecaLonrina
# caneca2 = Caneca('Caneca ByLearner', 'Foguete da Bylearn', 'Branca')
#
# caneca3 = CanecaLondrina()
# caneca4 = CanecaLondrina()
# caneca5 = CanecaLondrina()
#
# print(caneca1)     # Saída:Caneca Londrina
# print(caneca2)     # Saída:Caneca ByLearner
# print(caneca3)     # Saída:Caneca Londrina
# print(caneca4)     # Saída:Caneca Londrina
# print(caneca5)     # Saída:Caneca Londrina
#
# # Cada objeto é unico, cada instância é um objeto diferente
# # se eu modificar a caneca5 isso não vai alterar a caneca3, ou as demais
# # cada cada caneca é um objeto único e é a Abastação que garante isso
#
# # Se por exemplo eu tirar o .nome, e printar somente o objeto
# # O resultado vai ser esse:
#
# print(caneca1) # Saída: <__main__.CanecaLondrina object at 0x0000028B69662AB0>
# print(caneca2) # Saída: <__main__.Caneca object at 0x0000028B69662B10>
# print(caneca3) # Saída: <__main__.CanecaLondrina object at 0x0000028B69662AE0>
# print(caneca4) # Saída: <__main__.CanecaLondrina object at 0x0000028B69662C30>
# print(caneca5) # Saída: <__main__.CanecaLondrina object at 0x0000028B69662C60>
#
# # Repara que cada objeto está em uma posição da memória
# # Como se fossem objetos diferentes

# vamos voltar um pouco
# class Caneca:
#     def __init__(self, nome, logo, cor):
#         self.nome = nome
#         self.logo = logo
#         self.cor = cor
#         self.status = 'Cheia'
#
#
# class CanecaLondrina(Caneca):
#     def __init__(self):     # Essa função init eu estou fazendo a mesma coisa que eu fiz na classe pai (classe herdada)
#         self.nome = 'Caneca Londrina'     # Seria interessante então chamar eu já chamar essa função init da classe pai
#         self.logo = 'Cidade de Londres'     # Para evitar repetir código, e o Python pode fazer isso através do super()
#         self.cor = 'Branca'
#         self.status = 'Cheia'


# vamos ver como isso vai ficar:
#
# class Caneca:
#     formato = 'Cilíndrico com alça lateral'
#
#     def __init__(self, nome, logo, cor):
#         self.nome = nome
#         self.logo = logo
#         self.cor = cor
#         self.status = 'Cheia'
#
#     def beber(self):
#         self.status = 'Vazia'
#         return f'É da {self.nome} que eu estou bebendo'
#
#     def encher(self):
#         self.status = 'Cheia'
#         return f'Estou enchendo a {self.nome}'
#
#
# # chamamos de super classe, aquela classe da qual eu herdei as coisas, ou seja a classe pai
# # Ao executar o super() ele vai executar da minha classe pai
# # Lembra que, é do init que vai ser executado a operação de criar um novo objeto
# # Então ao chamar um super() e de qual função do super eu quero chamar? r: da função init
# # e em init eu vou passar os parametros/propriedades
#
#
# class CanecaLondrina(Caneca):
#     def __init__(self):
#         super().__init__('Caneca Londrina', 'Cidade de Londres', 'Branca')
#         # E agora eu nem preciso mais do status
#         # Porque se eu chamo o init, da classe pai
#         # É como se eu estivesse dizendo ao Python
#         # Olha Python, sempre que você for criar uma CanecaLondrina
#         # Você vai criá-lá através do construtor(init) na classe super()
#         # É como se você estivesse reutilizando o molde Caneca
#         # Só que quando você for utilizar esse molde Caneca sempre que for da Londrina
#         # Ele já vai por automaticamente essa estampa, ja vai por automaticamente uma caneca dessa cor, etc...
#
#
# # Vou criar então com base nisso uma CanecaBatman:
#
# class CanecaBatman(Caneca):
#     def __init__(self):
#         super().__init__('Caneca Gotham', 'Batman', 'Preta')
#
#
# caneca_londres = CanecaLondrina()
# caneca_bylearn = Caneca('Caneca ByLearner', 'Foguete da Bylearn', 'Branca')
# caneca_batman = CanecaBatman()
#
# # Agora eu também posso criar novas funções somente para a CanecaBatman, e funções somente para a CanecaLondrina

# Vou copiar e colar o codigo novamente, sem os comentários para ficar mais facil de visualizar:

# class Caneca:
#     formato = 'Cilíndrico com alça lateral'
#
#     def __init__(self, nome, logo, cor):
#         self.nome = nome
#         self.logo = logo
#         self.cor = cor
#         self.status = 'Cheia'
#
#     def beber(self):
#         self.status = 'Vazia'
#         return f'É da {self.nome} que eu estou bebendo'
#
#     def encher(self):
#         self.status = 'Cheia'
#         return f'Estou enchendo a {self.nome}'
#
#
# class CanecaLondrina(Caneca):
#     def __init__(self):
#         super().__init__('Caneca Londrina', 'Cidade de Londres', 'Branca')
#
#     def extras(self):       # Bonus exclusivo da CanecaLondrina
#         print('Como bônus você ganha uma colher!')
#
# class CanecaBatman(Caneca):
#     def __init__(self):
#         super().__init__('Caneca Gotham', 'Batman', 'Preta')
#
#     def som(self):      # Função exclusiva da CanecaBatman
#         print("I'm Batman!")
#
#
# caneca_londres = CanecaLondrina()
# caneca_bylearn = Caneca('Caneca ByLearner', 'Foguete da Bylearn', 'Branca')
# caneca_batman = CanecaBatman()
#
# caneca_londres.extras()     # Saída: Como bônus você ganha uma colher!
# caneca_batman.som()     # Saída: I'm Batman!

# Essas funções extras eu defini no FILHO
# Ou seja, eu defini em Caneca Londrina e em CanecaBatman
# O filho tem tudo que o pai tem, ou seja tudo que está em Caneca
# A CanecaBatman e a CanecaLondrina tem!
# Porem, na caneca bylearn eu não tenho nem o som, e nem o extras
# Então a classe pai não pega nada da classe filha
# Se a filha tiver funções especificas não vai para a classe pai


# ================================//============================
#                        POLIMORFISMO
# ================================//============================
# É o terceiro pilar, da orientação à objetos
# O polimorfismo é a possibilidade ou o poder de reescrever/sobrescrever métodos da classe pai
# É como se fosse a classe filho executando da forma dela algo que tem na classe pai

# No codigo anterior quem tem a função beber?
# A função beber() está em Caneca ou seja na classe pai
# É o pai que tem a função beber()

# Vamos fazer assim
# A CanecaLondrina por ser de Londres ela vai ter a bebida como sendo um chá
# E a CanecaBatman, por ser uma tema mais escuro, vai ter como bebida o café
# E vou fazer uma forma de reescrever/sobrescrever o que eu tenho na minha classe pai
# No método beber(), olha o que eu vou fazer!

# Vamos ao código:

# class Caneca:
#     formato = 'Cilíndrico com alça lateral'
#
#     def __init__(self, nome, logo, cor):
#         self.nome = nome
#         self.logo = logo
#         self.cor = cor
#         self.status = 'Cheia'
#
#     def beber(self):
#         self.status = 'Vazia'
#         return f'É da {self.nome} que eu estou bebendo'
#
#     def encher(self):
#         self.status = 'Cheia'
#         return f'Estou enchendo a {self.nome}'
#
#
# class CanecaLondrina(Caneca):
#     def __init__(self):
#         super().__init__('Caneca Londrina', 'Cidade de Londres', 'Branca')
#         self.bebida = 'Chá'
#     def extras(self):
#         print('Como bônus você ganha uma colher!')
#
#     def beber(self):
#         self.status = 'Vazia'   # Só para manter um padrão vou colocar o return
#         return 'Tá na hora do chá das 5'
#
#
# class CanecaBatman(Caneca):
#     def __init__(self):
#         super().__init__('Caneca Gotham', 'Batman', 'Preta')
#         self.bebida = 'Café'
#
#     def som(self):
#         print("I'm Batman!")
#
#     # Aqui eu vou fazer diferente, vou chamar a minha função super()
#     # O que a função super vai retornar? Ela vai retornar, o return de beber() da classe pai
#     # Eu vou somente acrescentar algo a esse retorno, vou apenas complementar
#     def beber(self):
#         return super().beber() + f' {self.bebida}'
#
#
#
# caneca_londres = CanecaLondrina()
# caneca_bylearn = Caneca('Caneca ByLearner', 'Foguete da Bylearn', 'Branca')
# caneca_batman = CanecaBatman()
#
# # Vamos executar pra ver o que acontece!
#
# print(caneca_bylearn.beber())       # Saída: É da Caneca ByLearner que eu estou bebendo
# print(caneca_londres.beber())       # Saída: Tá na hora do chá das 5
# print(caneca_batman.beber())        # Saída: None

# Porque deu None, em caneca_batman.beber()?
# Quando eu dei super() em batman, ele executa o return da função beber() na classe pai
# eu tenho que chamar o return antes do super() na CanecaBatman, pq ele não vai fazer isso sozinho

# E agora sim depois que eu coloquei o return antes do super, ele me retornou o return da função beber() na classe pai
# Saída, atualizada depois de colocar o return antes do super(): É da Caneca Gotham que eu estou bebendo Café

# Então eu consigo reescrever, reutilizando a classe pai
# O super apenas vai executar a função, ele vai executar da classe pai
# Ele não vai inserir a função, ele vai apenas executar da classe pai

# E eu também posso fazer uma nova, com caracteríticas e funções novas
# É dessa forma que eu posso fazer o meu Polimorfismo
# Ou seja, eu vou reescrever algo da classe pai, executando como uma classe filha

# ================================//============================
#                        ENCAPSULAMENTO
# ================================//============================
# O quarto e último pilar da orientação a objetos
# E esse aqui no Python tem algumas peculiaridades
# Encapsulamento seria como se fosse o privilégio de execução


# Nós temos alguns escopos, quando agente esta trabalhando com uma linguagem que é fortemente
# Ou seja ela força a executar a orientação a objeto como um todo
# Como o java e o C#, lá nos temos o public e o private
# o que for public todo mundo pode acessar
# Vamos supor que a classe Caneca tem lá o método publico que é o preço dela
# O preço é publico todo mundo pode ver
# E pode tanto alterar, por exemplo um vendedor que quer fazer uma promoção ele pode alterar quanto
# pode verificar o seu valor, então um cliente pode verificar quanto a caneca custa, ele bate no leitor e vê o preço.
# Mas você tem também propriedades privadas, como o preço de fábrica
# Você não quer que o seu consumidor saiba o quanto você pagou na caneca para revender pra ele mais caro
# Então você vai deixar privado essa informação, então só a própria classe pode ter acesso

# O Python preza pela liberdade dos programadores, então p Python não tem o privado e o publico
# Ele deixa você editar de qualquer forma, porém tem uma convenção que se gerou que é de colocar __ antes do nome
# para falar que é uma propriedade privada, porém isso não é uma via de regra e da pra executar um bypass
# Ou seja da pra hackear isso daí

# Vamos para o código:

# class Caneca:
#     formato = 'Cilíndrico com alça lateral'
#
#     def __init__(self, nome, logo, cor):
#         self.nome = nome
#         self.logo = logo
#         self.cor = cor
#         self.status = 'Cheia'
#         self.preço = 24.90
#
#
#     def beber(self):
#         self.status = 'Vazia'
#         return f'É da {self.nome} que eu estou bebendo'
#
#     def encher(self):
#         self.status = 'Cheia'
#         return f'Estou enchendo a {self.nome}'
#
#
# class CanecaLondrina(Caneca):
#     def __init__(self):
#         super().__init__('Caneca Londrina', 'Cidade de Londres', 'Branca')
#         self.bebida = 'Chá'
#         self.preço = 29.90
#
#     def extras(self):
#         print('Como bônus você ganha uma colher!')
#
#     def beber(self):
#         self.status = 'Vazia'
#         return 'Tá na hora do chá das 5'
#
#
# class CanecaBatman(Caneca):
#     def __init__(self):
#         super().__init__('Caneca Gotham', 'Batman', 'Preta')
#         self.bebida = 'Café'
#         self.preço = 34.90
#
#     def som(self):
#         print("I'm Batman!")
#
#     def beber(self):
#         return super().beber() + f' {self.bebida}'
#
#
# caneca_londres = CanecaLondrina()
# caneca_bylearn = Caneca('Caneca ByLearner', 'Foguete da Bylearn', 'Branca')
# caneca_batman = CanecaBatman()
#
# print('PROMOÇÃO!!!')
# caneca_batman.preço -= 5        # caneca_batman.preço = a ela mesma - 5
# caneca_londres.preço -= 5
# caneca_bylearn.preço -= 5
#
# # Mostrando os novos preços!
# print(f'A {caneca_batman.nome} tem o valor de R$ {caneca_batman.preço}')
# print(f'A {caneca_londres.nome} tem o valor de R$ {caneca_londres.preço}')
# print(f'A {caneca_bylearn.nome} tem o valor de R$ {caneca_bylearn.preço}')

# Saída:
# PROMOÇÃO!!!
# A Caneca Gotham tem o valor de R$ 29.9
# A Caneca Londrina tem o valor de R$ 24.9
# A Caneca ByLearner tem o valor de R$ 19.9

# Vamos colocar agora que toda caneca vai ter o preço de fábrica de 15,00 por exemplo
# Vamos fazer isso no código:

class Caneca:
    formato = 'Cilíndrico com alça lateral'
    __preço_fabrica = 15    # Ou aqui também

    def __init__(self, nome, logo, cor):
        self.nome = nome
        self.logo = logo
        self.cor = cor
        self.status = 'Cheia'
        self.preço = 24.90
#        self.__preço_fabrica = 15   # repara nos dois __ antes do nome // Vamos executar isso!


    def beber(self):
        self.status = 'Vazia'
        return f'É da {self.nome} que eu estou bebendo'

    def encher(self):
        self.status = 'Cheia'
        return f'Estou enchendo a {self.nome}'


class CanecaLondrina(Caneca):
    def __init__(self):
        super().__init__('Caneca Londrina', 'Cidade de Londres', 'Branca')
        self.bebida = 'Chá'
        self.preço = 29.90

    def extras(self):
        print('Como bônus você ganha uma colher!')

    def beber(self):
        self.status = 'Vazia'
        return 'Tá na hora do chá das 5'


class CanecaBatman(Caneca):
    def __init__(self):
        super().__init__('Caneca Gotham', 'Batman', 'Preta')
        self.bebida = 'Café'
        self.preço = 34.90

    def som(self):
        print("I'm Batman!")

    def beber(self):
        return super().beber() + f' {self.bebida}'


caneca_londres = CanecaLondrina()
caneca_bylearn = Caneca('Caneca ByLearner', 'Foguete da Bylearn', 'Branca')
caneca_batman = CanecaBatman()

print('PROMOÇÃO!!!')
caneca_batman.preço -= 5        # caneca_batman.preço = a ela mesma - 5
caneca_londres.preço -= 5
caneca_bylearn.preço -= 5

# Mostrando os novos preços!
print(f'A {caneca_batman.nome} tem o valor de R$ {caneca_batman.preço}')
print(f'A {caneca_londres.nome} tem o valor de R$ {caneca_londres.preço}')
print(f'A {caneca_bylearn.nome} tem o valor de R$ {caneca_bylearn.preço}')

# print(caneca_londres.__preço_fabrica)
# Se eu tentar printar isso ele vai dar um erro:
# AttributeError: 'CanecaLondrina' object has no attribute '__preço_fabrica'. Did you mean: '_Caneca__preço_fabrica'?
# Dizendo que não tem esse atributo

# O Python já faz pra você essa convenção, ou seja tem dois __
# Vou deixar como privado
# Mas isso não é uma regra!!!
# O Python quando você pode dois __
# Ele muda o nome deste atributo, para: _NomeClasse
# Vou pegar a caneca_bylearn que é a classe pai
# Ela chama Caneca
# Se eu colocar _Caneca e depois __preço_fabrica
# Eu consigo pegar ele!
# Vamos executar ele aqui!

print(caneca_bylearn._Caneca__preço_fabrica)        # Saída: 15

# Ou seja não deu erro
# Ele ocultou isso!
# como eu posso também alterar esse valor

caneca_bylearn._Caneca__preço_fabrica = 1
print(caneca_bylearn._Caneca__preço_fabrica)    # Saída: 1

# Então o Python ele tem o encapsulamento
# Você pode fazer com essas duas __
# Porém saiba que, o usuário pode sim fazer um hacker para acessar de fora,
# Porém não é um encapsulamento total, tem algumas formulas mais avançadas
# Mas até mesmo as formulas avançadas e seguras tem como fazer um hacker

# Então encapsulamento na orientação a objetos
# é basicamente isso daí de você ter um método publico e privado
# O Python você usa dois __
# Então dessa forma que foi feita acima é privado, porém nada impede de ser hackeado e alguém acessar o método privado
# Mas basicamente isso é uma questão de segurança da orientação a objetos
# É como se você estivesse dizendo:
# Eu não quero que o programador não tenha acesso ao que ele não deve
# Eu quero ter uma questão de privilégio de segurança aqui!
# De guardar como privado esse valor

# O ideal é reorganizar, em módulos(pastas) para organizar o código
# Separando, a classe pai, das classes filhas, e chamando elas pelo import
# e um arquivo.py para executar os códigos, como se fosse o controlador de todo o código
