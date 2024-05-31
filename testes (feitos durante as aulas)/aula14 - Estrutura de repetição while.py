# A estrutra de repetição "while" é chamada de:
# Estrutura de Repetição com teste lógico

# A Estrutura de repetição "for" é chamada de:
# Estrutura de Repetição com variável de controle

# while significa enquanto
# vai funcionar da seguinte forma:
'''
c = 1               # enquanto "c" não for diferente de 10, ele vai dar loops. E só vai parar quando essa condição se tornar falsa.
while c != 10:      # enquanto essa condição se tornar verdadeira (diferente de 10 = verdadeiro = + 1 loop)
    print(c)        # quando eu chegar no 10 essa condição vai se tornar falso, porque cheguei no 10.
    c += 1          # E já não é mais diferente de 10, então a condição de != 10 se torna falso e o loop acaba.
print('FIM')
'''
# Eu uso a estrutura de repetição com variável de controle (for)
# Quando eu sei o limite, ou o número de repetições

# Quando eu não sei o limite, ou não sei o número de repetições,
# Então uso a estrutura de repetição com teste lógico (while)

# Não é regra, porque quando eu sei o limite posso usar também a estrutra de repetição (while)

# ===============================================================
'''for c in range(1, 10):
    print(c)
print('FIM')'''


'''c = 1               # Contador começa com 1
while c < 10:       # Enquanto contador for menor que 10
    print(c)
    c += 1          # ou: (c = c + 1) Pq? - Pq eu quero somar + 1 no c, toda vez que ele fizer o loop
print('FIM')'''
# ==============================================================

# AQUI EU VOU LER 4 VALORES, ISSO FOI FEITO AULA 13

'''for c in range(1, 5):
    n = int(input('Digite um valor: '))
print('FIM')'''

# MAS SE EU NÃO SOUBER QUANTOS VALORES EU QUERO LER?
# exemplo:
# Você vai digitar um valor, mas quando eu digitar 0, ele para.

'''n = 1                                           # Aqui eu crio uma variável, pra ela poder funcionar no (while)
while n != 0:                                   # Equanto o número for diferente de 0, ele vai ficar lendo um número.
    n = int(input('Digite um valor: '))         # este valor vai continuar sendo pedido até o usuário digitar 0
print('FIM')'''                                    # E só então, o loop finaliza!

# Com a estrutura (for) isso não seria possível!

# A condição que vem depois do while é chamada de (flag) é uma condição de parada

'''r = 'S'
while r == 'S':                                 # Enquanto r foi igual à "S", o loop vai continuar.
    n = int(input('Digite um valor: '))         # Se r não for "S", então é FALSO e o loop para.
    r = str(input('Quer continuar? [S/N] ')).upper()
print('FIM')'''

# =====================================================

# Eu quero saber quantos números pares e quantos números impares foram digitados
n = 1
par = impar = 0         # Qntd de par e qntd de impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:                  # Se n não for 0, se n for diferente de zero ele vai executar a identação
        if n % 2 == 0:                              # Se o "%" (resto da divisão) de "n" por "2" for = 0
            par += 1                                # Se for divisível por 2, par recebe +1
        else:                                       # Se não for divisível por 2, impar recebe +1
            impar += 1                              # E se digitado o 0, ele não entra nessa conta. Como dita o primeiro (if)
print(f'Você digitou {par} números pares, e {impar} números ímpares.')
