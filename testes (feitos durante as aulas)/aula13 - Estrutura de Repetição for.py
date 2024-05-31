# Nessa aula, vamos começar nossos estudos com os laços e vamos fazer primeiro
# o “for”, que é uma estrutura versátil e simples de entender. Por exemplo:

'''
print('# --------------- PRIMEIRO EXEMPLO -----------------')
for c in range(0, 4):
    print( c )

print('Acabou')
'''


'''
print('\n\n# ---------------- SEGUNDO EXEMPLO -----------------------------')
print('oi')
print('oi')
print('oi')
print('oi')
print('oi')
print('oi')
print('# ---------------------------------------------\n\n')
'''
# Para escrever print 6x eu preciso fazer varios prints
# varias linhas de código!
# E se eu precisse escrever 10mil linhas?
# E fosse escrever uma por uma?!
'''
for c in range(0, 6):
    print('Oi')
print('FIM')
'''

# Depois de usar o comando for, cuidado com a identação, o que estiver identado será executado dentro do for
# Se eu identar(TAB) este print, para dentro do for. Vai executar: (Oi FIM, Oi FIM) 6x
'''
for c in range(0, 6):
    print(c)
print('FIM')
'''

# Repara que ele executou até o número 5 porque ele não considera o ultimo número.
# Então o que eu faço? Ao invés do 6 coloco o 7, e ele vai contar até 6
'''
for c in range(0, 7):
    print(c)
print('FIM')
'''


# E se eu quiser uma contagem de 6 até 0?
'''
for c in range(6, 0):
    print(c)
print('FIM')
'''
# Ele vai executar somente o FIM
# Na verdade você quer que ele conte para trás, de maneira regressiva
# Então vai ficar assim:
'''
for c in range(6, 0, -1):
    print(c)
print('FIM')
'''



# O que ele vai fazer aqui?
# Ele vai fazer: 6, 6-1, 5, 5-1, 4, 4-1, 3, 3-1, 2, 2-1, 1, FIM

'''
for c in range(0, 7, 2):
    print(c)
print('FIM')
'''
# Ele vai pular de 2 em 2: 0, 2, 4, 6, FIM

'''
n = int(input('Digite um número: '))
for c in range(0, n+1):     # Só para chegar no número em que o usuário digitou
    print(c)
print('FIM')
'''
# Ele vai contar de 0 até chegar ao número digitado e depois printar o FIM

'''
i = int(input('Inicio: '))  #DE, INICIO
f = int(input('Fim: '))     #ATÉ, FIM
p = int(input('Pulando: '))   #PULANDO DE, 2 em 2 (por exemplo)
for c in range(i, f+1, p):
    print(c)
print('FIM')
'''


# --------------------------------------------------
'''
for c in range(0, 3):           
    n = int(input('Digite um valor: '))             # Aqui ele executou este n, 3x
print('FIM')                                        # Porque este comando pra ler está dentro de um for
'''                                                 # Se ao invés do 3 eu colocar o número 10 por exemplo, ele vai executar
                                                    # Este input 10x
# ------------------------------------------------------------------------------

s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n          # s = s + n que é igual a formula dessa linha
print(f'O somatório de todos os valores foi {s}')
