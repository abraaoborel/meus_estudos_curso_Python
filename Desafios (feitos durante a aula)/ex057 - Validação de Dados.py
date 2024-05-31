# Faça um progrma que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

'''sx = 'm', 'f'

while sx != 'm' and sx != 'f':
    sx_ = str(input('Informe seu sexo: [M/F] ')).strip().lower()

    if sx != 'm' and sx != 'f':
        sx = str(input('Dados inválidos. Por Favor, informe seu sexo: [M/F] ')).strip().lower()
    print(f'Sexo {sx} registrado com sucesso.')

print(f'Sexo {sx} registrado com sucesso.')'''

sexo = str(input('Informe o seu sexo [M/F]')).strip().lower()[0]    # Quero somente a primeira letra
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo [M/F] '))
print(f'Sexo {sexo} registrado com sucesso.')

# Quebrei a cabeça tentando fazer com and, or, !=, ==, if, else. Esse not in foi novidade pra mim.
# kkkkkkk....
