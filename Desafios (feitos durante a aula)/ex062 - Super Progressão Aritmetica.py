# Melhore o DESAFIO 061, perguntando para o usuário
# se ele quer mostrar mais alguns termos.
# O programa encerra quando ele disse que quer mostrar 0 termos.

print('Gerador de PA')
print('-='*10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
contador = 1
total = 0
mais = 10
while mais != 0:        # Enquanto mais não for diferente de 0:
    total = total + mais        # total vai receber 0 + 10
    while contador <= total:       # Enquanto (contador) for (<=) do que o total ou seja (10)
        print(f'{termo} -> ', end='')       # Ele segue com a lógica do ex061 (anterior)
        termo += razao
        contador += 1
    print('PAUSA')         # (mais) é exibido, quando essa identação se torna False ou seja: (<= 10) == (contador <= total)
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Progressão finalizada com {total} termos mostrados.')

# DESAFIO É FAZER ESTE EXERCÍCIO, VÁRIAS VEZES!
