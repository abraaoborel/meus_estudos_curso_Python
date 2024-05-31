# Crie uma frase qualquer e diga se ela é um palíndromo,
# desconsiderando os espaços e acentos (Mas você vai digitar com espaços)
# Palíndromo é aquela frase que você pode ler de trás pra frente e de frente pra trás,
# que vai dar na mesma.
# ex:
# APOS A SOPA
# A SACADA DA CASA
# A TORRE DA DERROTA
# O LOBO AMA O BOLO
# ANOTARAM A DATA DA MARATONA
# ----------------------------------------------------------
'''             # PRIMEIRO RESULTADO:

frase = str(input('Digite uma frase : ')).upper().strip()
palavras = frase.split()
tudo_junto = ''.join(palavras) #.join() faz a junção de .slpit()
inverso = ''
for letra in range(len(tudo_junto) - 1, -1, -1):    # Explicando os -1: da ultima letra, até a primeira, voltando uma letra
    inverso += tudo_junto[letra]
print(f'O inverso de {tudo_junto} é {inverso}')

if inverso == tudo_junto:
    print('Temos um Palíndromo!')
else:
    print('A frase digitada não é um Palíndromo!')

'''
        # SEGUNDO RESULTADO, APENAS COM TRATAMENTO DA STRING:

frase = str(input('Digite uma frase : ')).upper().strip()
palavras = frase.split()
tudo_junto = ''.join(palavras) #.join() faz a junção de .slpit()
inverso = tudo_junto[::-1]
print(f'O inverso de {tudo_junto} é {inverso}')
if inverso == tudo_junto:
    print('Temos um Palíndromo!')
else:
    print('A frase digitada não é um Palíndromo!')
