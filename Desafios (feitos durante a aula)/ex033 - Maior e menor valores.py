# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

# Resolução que foi feita na aula 033, no vídeo:

'''num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número '))

# Verificando quem é o menor

menor = num1
if num2 < num1 and num2 < num3:
    menor = num2
if num3 < num1 and num3 < num2:
    menor = num3

# Verificando quem é o maior

maior = num1
if  num2 > num1 and num2 > num3:
    maior = num2
if num3 > num1 and num3 > num2:
    maior = num3

print(f'O menor valor digitado foi {menor}')
print(f'O maior valor digitado foi {maior}')'''

# Vi um comentário no YouTube no qual o cara postou uma solução mais simples sem usar as condicionais if ou else
# segue o Código:

'''n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite um último número: '))
lista = [n1, n2, n3]
lista.sort()
print(f'O maior número é {lista[2]}, e o menor é {lista[0]}')'''
# O método .sort() ordena os números da lista em ordem crescente, tornando  o programa mais compacto.

# E encontrei um outro mais simplificado ainda!

n1 = int(input('\033[97;44mDigite o primeiro número:\033[m '))
n2 = int(input('\033[97;42mDigite o segundo número:\033[m '))
n3 = int(input('\033[97;41mDigite o terceiro número:\033[m '))
print(f'\033[4;7;97;44mO maior numero é {max(n1, n2, n3)}\033[m') #Retorna o maior item/argumento
print(f'\033[4;7;97;42mO menor numero é {min(n1, n2, n3)}\033[m') #Retorna o menor item/argumento
