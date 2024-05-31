# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas
# os valores pares e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.

lista = []
pares = list()
impares = list()
while True:
    lista.append(int(input('Digite um valor: ')))

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if resp == 'N':
        break

for inc, vlr in enumerate(lista):       # inc ("de indice") recebeu a contagem de loops # vlr ("valor") recebeu num digitado em lista
    if vlr % 2 == 0:
        pares.append(vlr)
    elif vlr % 2 == 1:
        impares.append(vlr)

print('-=' * 30)
print(f'A lista completa é: {lista}')
print(f'A lista dos números pares são: {pares}')
print(f'A lista dos números impares são: {impares}')

