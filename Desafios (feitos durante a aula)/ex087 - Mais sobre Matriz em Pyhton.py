# Aprimore o exercício anterior, mostrando no final:
# a) A soma de todos os valores pares digitados.
# b) A soma dos valores da terceira coluna.
# c) O maior valor da segunda linha.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_par = maior = soma_coluna = 0      # Vou criar essas variáveis, que vão realizar as funcionalidades solicitadas
for l in range(0, 3):   # Essa primeira estrutura para preencher a matriz
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-=' * 30)
for l in range(0, 3):   # Essa segunda para mostrar na tela a matriz
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')   # Quando eu estiver mostrando o valor da matriz linha coluna, vou verificar antes de terminar
        if matriz[l][c] % 2 == 0:   # Se o elemento que acabou de se exibido na tela for par
            soma_par += matriz[l][c]    # soma_par recebe ela mesma, mais a matriz[l][c] que foi o valor que acabei de ler
    print()
print('-=' * 30)
print(f'A soma dos valores pares é: {soma_par}')
# Quando eu peço o input de digite um valor, eu estabeleço a ordem em que será organizada
# l para linha e c para coluna, e os seus respectivos números
# Como eu preciso somar os valores da terceira coluna
# Terceira coluna: [0, 2], [1, 2], [2, 2]
# O valor da {c} não muda, e muda somente o valor de {l} que é a referência da linha
for l in range(0, 3):
    soma_coluna += matriz[l][2]     # soma_coluna recebe ela mesma, mais a matriz na linha [l], na coluna [2]
print(f'A soma dos valores da terceira coluna é: {soma_coluna}')
# agora eu preciso descobrir o maior valor da segunda linha
# a referência da segunda linha é: [1, 0], [1, 1], [1, 2]
# repara que {l} agora é fixa, e quem muda agora é {c}
# vou utilizar do mesmo raciocinio, que foi usado anteriormente
for c in range(0, 3):
    if c == 0:  # primeira coluna
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'O maior valor da segunda linha é: {maior}')