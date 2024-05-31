# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999
# Que é a condição de parada,
# No final, mostre quantos números foram digitados, e qual foi a soma entre eles.
# (Descondiserando a FLAG)



c = soma = 0        # NA RESOLUÇÃO DESSE EXERCÍCIO, NÃO PRECISOU DECLARAR N = 0, PRA ELE FUNCIONAR. POR CAUSA DO WHILE TRUE.
while True:             # POR ISSO EU EXCLUI
    n = int(input('Digite um número ou [999 para PARAR]: '))
    if n == 999:        # A ORDEM DO IF, PARA DAR CONDIÇÃO AO BREAK TEM QUE ESTAR MAIS ACIMA COMO ESTÁ AQUI!
        break           # TINHA FEITO DEPOIS DA LINHA DA SOMA, E TINHA SOMADO O 999 COM OS NUMEROS DIGITADOS.
    c += 1              # MAS ORGANIZANDO O IF PARA A FLAG DO BREAK MAIS ACIMA É O CORRETO!
    soma += n
print(f'Foram digitados {c} números, e a soma entre eles é {soma}')
