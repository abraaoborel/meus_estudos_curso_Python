# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas
# respectivas posições na lista.

'''num = [int(input('Digite um valor para a posição 0: ')),
       int(input('Digite um valor para a posição 1: ')),
       int(input('Digite um valor para a posição 2: ')),
       int(input('Digite um valor para a posição 3: ')),
       int(input('Digite um valor para a posição 4: '))]
print('-='*20)
print(f'Você digitou os valores {num}')
print(f'O maior valor digitado foi {max(num)}')
print(f'O menor valor digitado foi {min(num)}')'''

# Começei fazendo como foi feito acima.
# Mas depois voltei nas minhas anotações da aula 17
# E consultando como que faz a busca pela posição de cada item na lista
# Encontrei essa maneira de fazer a lista com o for!

valores = list()
for contador in range(0, 5):
       valores.append(int(input(f'Digite um valor para a posição {contador}: ')))
print('-='*20)
print(f'Você digitou os valores {valores}')
maior = max(valores)
menor = min(valores)
print(f'O maior valor digitado foi {maior}, nas posições ', end='')
for c, v in enumerate(valores):
       if v == maior:
              print(f'{c}...', end='')
print()
print(f'O menor valor digitado foi {menor}, nas posições ', end='')
for c, v in enumerate(valores):
       if v == menor:
              print(f'{c}...', end='')
print()

# Esse foi o meu código! # Mas eu só consegui resolver ele depois de assistir a resoluçãd o exercicio
# Mas vou copiar o código do Guanabara:

# Lógica do Guanabara dentro do primeiro if:
# Eu vou te pedir um valor: ...
# Qual é o maior e qual é o menor? resposta: 7, porque só tem ele
# if c == 0: é exatamente isso, se

'''lista_num =[]
maior = 0
menor = 0
for c in range(0, 5):
       lista_num.append(int(input(f'Digite um valor para a posição {c}: ')))
       if c == 0:
              maior = menor = lista_num[c]
       else:
              if lista_num[c] > maior:
                     maior = lista_num[c]
              if lista_num[c] < menor:
                     menor = lista_num[c]
print('-=' * 30)
print(f'Você digitou os valores {lista_num}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for i, v in enumerate(lista_num):
       if v == maior:
              print(f'{i}... ', end='')
print()
print(f'O menor valor digitado foi {menor} nas posições ', end='')
for i, v in enumerate(lista_num):
       if v == menor:
              print(f'{i}... ', end='')'''