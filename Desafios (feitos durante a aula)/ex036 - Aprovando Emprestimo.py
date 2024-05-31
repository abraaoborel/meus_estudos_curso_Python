# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

valor_casa = float(input('Qual o valor da casa? R$ '))
salario_comprador = float(input('Qual é o seu salário? R$ '))
prazo = int(input('Em quantos anos você vai pagar? R$ '))
prestaçao_mensal = valor_casa / (prazo * 12)
minimo = salario_comprador * 30 / 100
print(f'Para pagar uma casa de {valor_casa} em {prazo} anos,', end='')
print(f' a prestação será de {prestaçao_mensal:.2f}')
if prestaçao_mensal <= minimo:
    print('Emprestimo pode ser CONCEDIDO.')
else:
    print('Emprestimo NEGADO.')
# Nesse exercício fiquei mais travado, eu ia errar na conta e quando foi colocar o if não coloquei o : no final da linha
# e tinha dado erro e eu tinha ficado sem entender o porque
