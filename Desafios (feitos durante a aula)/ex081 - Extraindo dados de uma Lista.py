# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

lista = []
while True:
    lista.append(int(input('Digite um valor : ')))   # o valor de num é inserido na lista

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break

print('-=' * 30)

print(f'Você digitou: {lista}. \nForam digitados {len(lista)} números.')
lista.sort(reverse=True)        # Vou ordenar a lista(sort), e depois (reverse=True) para uma ordem decrescente
print(f'A lista em ordem decrescente: {lista}')
if 5 in lista:
    print('O valor 5 foi digitado, e está na lista.')
else:
    print('O valor 5 não foi encontrado na lista.')
