# Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço formal
# – 3x ou mais no cartão: 20% de juros
# =========================================================================
print(f'{' LOJAS GUANABARA ':=^40}')
compra = float(input('Digite o preço das compras: R$ '))
print('''FORMA DE PAGAMENTO
[ 1 ] à vista dinheiro/pix
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão 
[ 4 ] 3x ou mais no cartão ''')
opçao = int(input('Qual é a opção? '))
if opçao == 1:
    total = compra - (compra * 10 / 100)
#    print(f'Sua compra de R$ {compra:.2f}, vai custar R$ {total:.2f} no final')
elif opçao == 2:
    total = compra - (compra * 5 / 100)
#    print(f'Sua compra de R$ {compra:.2f}, vai custar R$ {total:.2f} no final')
elif opçao == 3:  #aqui eu não preciso fazer a variavel opçao3, porque o preço vai continuar o mesmo
    total = compra
    parcela = compra / 2
    print(f'Sua compra será parcelada em 2x de R$ {parcela:.2f}, SEM JUROS')
elif opçao == 4:
    total = compra + (compra * 20 / 100)
    total_parcelado = int(input('Quantas parcelas? '))
    parcela = total / total_parcelado
    print(f'Sua compra será parcelada em {total_parcelado:.0f}x de R$ {parcela:.2f}, COM JUROS')
    print(f'Sua compra de R$ {compra:.2f}, vai custar R$ {total:.2f} no final')
else:
    total = compra
    print('Opção inválida! Tente novamente!')
print(f'Sua compra de R$ {compra:.2f}, vai custar R$ {total:.2f} no final')
