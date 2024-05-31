# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista.
# No final, mostre:
# a) Quantas pessoas foram cadastradas.
# b) Uma listagem com as pessoas mais pesadas.
# c) Uma listagem com as pessoas mais leves.

lista = []  # Armazena os dados
dados = []  # Recebe os dados temporáriamente
cadastros = maior_peso = menor_peso = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    #cadastros += 1
    if len(lista) == 0:    # Se eu não cadastrei ninguém ainda, é pq não tem nenhuma pessoa cadastrada.
        maior_peso = menor_peso = dados[1]   # dados[1] = peso, dados[0] = nome
    else:   # Se não for o primeiro
        if dados[1] > maior_peso:
            maior_peso = dados[1]
        if dados[1] < menor_peso:
            menor_peso = dados[1]

    lista.append(dados[:])      # [[Lista]] recebe copia de [dados]
    dados.clear()   # lista [dados] é zerada!

    resp = ' '
    while resp not in 'SN':     # Continuar sim ou nao?
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break

# OBS: A ORDEM DA ESTRUTURA ALTEROU O RESULTADO!
# TINHA COLOCADO O APPEND DE DADOS NA LISTA E DADOS CLEAN, DEBAIXO DESSE BLOCO DE COMANDOS PARA CONTINUAR
# E A CONTA NÃO ESTAVA BATENDO, NÃO ESTAVA REGISTRANDO DIREITO
'''print(f'Ao todo foram cadastradas {cadastros} pessoas.')     feito com um contador de cadastros'''

print('-=' * 30)
print(f'Ao todo foram cadastradas {len(lista)} pessoas.')   # len = tamanho de [cadastros] na [[lista]]
print(f'O maior peso cadastrado foi de {maior_peso}kg. Peso de ', end='')
for p in lista:
    if p[1] == maior_peso:
        print(f'[{p[0]}]')
print(f'O menor peso cadastrado foi de {menor_peso}kg. Peso de ', end='')
for p in lista:
    if p[1] == menor_peso:
        print(f'[{p[0]}]')
print()
