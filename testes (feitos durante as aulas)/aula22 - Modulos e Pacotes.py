# Nessa aula, vamos continuar nossos estudos de funções em Python,
# aprendendo como criar módulos em Python e reutilizar nossos códigos em outros projetos.
# Vamos aprender também como agrupar vários módulos em um pacote,
# ampliando ainda mais a modularização em grandes projetos em Python.

# Modularizar é o ato de contruir módulos
# Surgiu no inicio da epoca de 60
# Os sistemas estavam ficando maior
# O foco principal é dividir um programa grande, em pequenos módulos
# O segundo foco é aumentar a legibilidade, isto é, um programa muito grande é muito dificil de dar manutenção
# O terceiro é facilitar a manutenção do sistema

# Nós vamos utilizar módulos, para dividir um problemão em pequenos problemas.

# Criei um outro Projeto, com nome de Aula22 - Modulos
# Como faz parte da Aula vamos fazer todos os exercícios usando módulos agora!

# Copiei tudo que eu tinha feito lá, e colei aqui caso eu precise!

# O que a programação me permite fazer é criar uma arquivo uteis.py (por exemplo)
# E colocar todas as funções lá dentro!
# Observação fiz isso aqui!
# Restando apenas o programa principal

# Mas agora para utilizar as funções eu preciso dar um import nelas

# Posso fazer também utilizando o from uteis import fatorial, dobro, triplo
# Observação!!!
# Essa forma de from uteis import fatorial, dobro, triplo
# Não é tão recomendada pelo próprio Python porque essas funções podem ter confiltos
# Por exemplo se eu tiver uma outra bibliteca com uma função chamada fatorial ou dobro, ou triplo
# Ele vai ficar meio confuso para saber qual é o dobro que ele vai calcular,
# Imagina que eu importei varias bibliotecas na biblioteca uteis tem a função dobro
# Mas em outras bibliotecas que eu importei também tem a função dobro
# Aí o Python vai ficar, qual função eu vou executar? o primeiro dobro ou o segundo dobro
# Na prática o que vale, caso tiver essas duas funções chamada dobro a que vale é a última a ser importada.
# Mas para evitar esse tipo de incompatibilidade é só fazer o import uteis

# Vantagens de se ter uma modularização
# Organização do código
# Facilidade na manutenção
# Ocultação do código detalhado
# Reutilizar os meus módulos em outros projetos
# (é só copiar o arquivo uteis.py e jogar na pasta do outro projeto que todas as funções estarão ali para serem
# importadas caso sejam necessárias)

# O módulo é muito importante para ajudar o nosso programa a crescer
# E aí quando só os módulos já não puderem satisfazer, porque ficou muito grande
# A solução são os pacotes (algumas outras linguagens de programação chama isso de biblioteca)
# Mas o Python chama isso de pacotes

# O que é um pacote?
# vamos a um exemplo prático
# Se eu tenho por exemplo o meu uteis.py
# Com mutias funções lá dentro
# Por exemplo umas 50, 100...
# Isso vai dificultar a minha legibilidade, dificultando a minha manutenção
# A modularização nos ajuda até certo ponto
# O que agente começava a fazer dentro das linguagens de programação tradicionais
# era criar vários módulos, o Python facilitou isso de mais!!!
# e colocou além da criação de outros módulos a junção de módulos e separados por assunto
# Que é o que chamamos de pacote
# O pacote nada mais é do que uma pasta que contém módulos
# ao inves de ter o uteis.py
# eu vou ter um pacote chamado uteis, todas as funções que eu tinha anteriormente estão aqui
# só que agora separado por assuntos, dentro do meu pacote uteis eu posso ter por exemplo
# funções só para tratamentos de números, posso ter algumas funções para tratamento de strings,
# datas, cores...
# então dentro do meu pacote de utilidades agora eu tenho várias funções, vários módulos, separados por assunto
# é exatamente isso que se forma um pacote em python
# e para importar ele também é muito simples por exemplo:
# import uteis (e tudo vai ser importado)
# ou também posso fazer importações específicas de módulos dentro de pacotes, por exemplo:
# from uteis import datas

# E como fazemos para criar um pacote?
# Todo arquivo .py pode ser potencialmente um módulo
# Dentro de um Projeto Python, toda pasta é considerada um pacote
# Então se eu tenho um pacote chamado uteis
# basta eu criar uma pasta do projeto chamada uteis
# e se dentro da pasta uteis eu tenho, números, datas, strings, cores
# Posso por exemplo criar dentro do pacote uteis, uma pasta chamada cores ou até um módulo chamado cores
# e eu vou fazer isso (criar uma pasta dentro de uteis) para cada função

# Pacotes são para programas expressivamente grandes, muito grandes mesmo!
# Como o curso é basico nós não vamos chegar nesse ponto

# existe uma sintaxe para nomes de arquivos dentro de pacotes
# __init__.py
# dentro de cada uma das pastas vai ter que ter um arquivo __init__.py (escrito exatamente dessa forma)
# inclusive o pacote principal uteis, também pode ter um arquivo __init__.py
# Vamos agora criar um pacote e colocar nossas funções dentro dele
# alt+1 (vai abrir a barra de projetos à esquerda)
# Vou com o mause em cima do Projeto: Aula22 - Modulos
# Clicar com botão direito
# New
# Python Package (pacote python)
# vamos criar o uteis e dentro de uteis vamos criar outro pacote numeros, strings, datas

# criei um novo diretorio, ex107
# para não criar uma bagunça no meio dos exercícios