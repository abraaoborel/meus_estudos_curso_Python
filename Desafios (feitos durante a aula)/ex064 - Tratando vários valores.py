# Crie um progrma que leia vários números inteiros pelo teclado.
# O progrma só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles.
# (Desconsiderando o flag).

'''n = 0
contador = 0        # Zero, Pq eu não li número nenhum
soma = 0''' #SIMPLIFICADO NO CÓDIGO ABAIXO:
n = cont = soma = 0         # Atribui todas essas variáveis à zero, em uma única linha
n = int(input('Digite um número ou, [999 para parar]: '))
while n != 999:
    soma += n
    cont += 1
    n = int(input('Digite um número ou, [999 para parar]: '))
print(f'Você digitou {cont} números, e a soma entre eles foi {soma}')

# EXERCÍCIO UM POUCO QUANTO CONFUSO