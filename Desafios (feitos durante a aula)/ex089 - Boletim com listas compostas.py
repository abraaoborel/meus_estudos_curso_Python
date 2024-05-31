# Crie um programa que leie nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e
# permita que o usuário possa mostrar as notas de cada aluno individualmente.

ficha = list()  # primeiro vamos declarar uma ficha padrão para cada aluno
while True:     # Já que eu quero que isso aconteça várias vezes, uso um loop infinito
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])  # vamos ler os dados do aluno

    resp = ' '      # Aqui eu crio uma condição para saber se o usuário quer continuar ou não
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
# print(ficha)    [['Abraão', [8.0, 9.0], 8.5], ['Isaque', [7.0, 8.0]]
print('-=' * 30)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 26)
for i, a in enumerate(ficha):   # a[0] = nome ..... a[1] = nota1, nota2 ..... a[2] = média
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
# Agora eu preciso mostrar individualmente as notas de cada aluno, caso for solicitado
while True:     # pra isso vou criar mais um loop infinito
    print('-' * 35)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(ficha) - 1:
        # se o opc for menor do que o len de ficha ou seja qntd de alunos cadastrados -1, porque o primeiro aluno é 0 e o ultimo é -1
        print(f'Notas de ficha {ficha[opc][0]} são de {ficha[opc][1]}')
print('<<< VOLTE SEMPRE >>>')
