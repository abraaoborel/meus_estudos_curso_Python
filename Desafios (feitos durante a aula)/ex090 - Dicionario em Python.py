# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.
# Exemplo Resultado:
# Nome: Glaucia
# Media de Glaucia: 8.5
# Nome é igual a Glaucia
# Média é igual a 8.5
# Situação é igual a Aprovado
# ============//===================

'''pessoa = dict()
pessoa['nome'] = str(input('Nome: ')).strip()
pessoa['media'] = float(input(f'Média de {pessoa["nome"]}: '))
print('-=' * 15)
print(f'Nome é, {pessoa["nome"]}')
print(f'Média é, {pessoa["media"]}')
if pessoa['media'] >= 7:
    print('Situação = Aprovado!')
else:
    print('Situação = Reprovado!')
print('-=' * 15)'''
# Fiz sozinho!

# O resultado do Guanabara foi um pouco diferente, mas bem interessante!
# ele usou este for que eu achei diferente, tenho q praticar isso!
aluno = dict()
aluno['nome'] = str(input('Nome: ')).strip()
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['Situação'] = 'Aprovado!'
elif 5 <= aluno['media'] < 7:
    aluno['Situação'] = 'Recuperação'
else:
    aluno['Situação'] = 'Reprovado!'
print('-=' * 20)
for k, v in aluno.items():
    print(f'  - {k} igual à, {v}')
print('-=' * 20)
