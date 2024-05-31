# Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média atingida:
# – Média abaixo de 5.0: REPROVADO
# – Média entre 5.0 e 6.9: RECUPERAÇÃO
# – Média 7.0 ou superior: APROVADO
#============================================================================
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
print(f'Tirando um nota de {nota1:.1f} e outra de {nota2:.1f}, a média do aluno é de {media:.1f}')
if 5.0 > media:
    print('REPROVADO!')
elif 6.9 > media >= 5.0:
    print('RECUPERAÇÃO!')
elif 7 <= media:
    # Meio confuso na hora da teoria, mas é só fazer a conta reversa.
    # se: (sete menor do que media) == (media é maior do que sete)
    print('APROVADO!')
