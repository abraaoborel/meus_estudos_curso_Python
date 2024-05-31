# Faça um programa que tenha uma função chamada escreva(),
# que receba um texto qualquer como parâmetro
# e mostre uma mensagem com tamanho adaptável.
# ex:
# escreva('Olá Mundo!')
# Saída:
# -----------
# Olá Mundo!
# -----------
def escreva(msg):
    tamanho = len(msg) + 4
    print('~' * tamanho)
    print(f'  {msg}')
    print(('~' * tamanho))

# Programa Principal
print('Um print personalizado!')
print('-' * 30)
escreva(str(input('Digite algo: ')))


# O programa que o Guanabara fez:
'''
escreva('Gustavo Guanabara')
escreva('Curso em Vídeo de Python')
escreva('CeV')'''
# ~~~~~~~~~~~~~~~~~~~~~
#   Gustavo Guanabara
# ~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   Curso em Vídeo de Python
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~
#   CeV
# ~~~~~~~
# ===================================//=====================