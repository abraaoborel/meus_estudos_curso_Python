# Escreva um programa em Python que leia um número inteiro qualquer e
# peça para o usuário escolher qual será a base de conversão:
# 1 para binário,
# 2 para octal e
# 3 para hexadecimal.
# ========================================================================

num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão: 
[ 1 ] Converter para BINÁRIO
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADECIMAL''')
opçao = int(input('Sua opção: '))
if opçao == 1:
    print(f'{num} Convertido para BINÁRIO é igual à {bin(num) [2:]}') # [2:] Para seguir do 3o caractere da string
elif opçao == 2:
    print(f'{num} Convertido para OCTAL é igual à {oct(num) [2:]}')
elif opçao == 3:
    print(f'{num} Convertido para HEXADECIMAL é igual à {hex(num) [2:]}')
else:
    print('Opção inválida! Tente novamente!')
