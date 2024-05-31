# Crie um programa que leia nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não.
# No final, mostre:
# A) Qual é o total gasto na compra.
# B) Quantos produtos custam mais de R$ 1000
# C) Qual é o nome do produto mais barato.

print('-'*40)
print('{:^40}'.format('LOJA SUPER BARATÃO'))    # 40 espaços, texto no meio
print('-'*40)

total = acima_mil = menor = contador = barato = 0
barato = ' '
# enquanto a variável [resp = ' '] estava aqui em cima, ela não estava loopando.
while True:
    produto = str(input('Nome do produto: '))
    preço = int(input('Preço: R$ '))
    contador += 1
    total += preço

    if preço > 1000:
        acima_mil += 1

    if contador == 1 or preço < menor:
        menor = preço
        barato = produto
    '''else:
        if preço < menor:
            menor = preço
            barato = produto'''

    resp = ' '          # depois que trouxe [resp = ' '] pra cá o loop infinito deu certo
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':     # quando este if, entava dentro deste while não estava executando o break
        break           # tive que voltar esta identação para funcionar

print('{:-^40}'.format(' FIM DO PROGRAMA '))    # TEXTO ENTRE 40 TRAÇOS
print(f'O total gasto na compra foi de R$ {total:.2f}')
print(f'Temos {acima_mil} produtos custando acima de R$ 1000.00')
print(f'O produto mais barato custa R$ {menor:.2f}')
