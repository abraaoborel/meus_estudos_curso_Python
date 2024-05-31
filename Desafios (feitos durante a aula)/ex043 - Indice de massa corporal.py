# Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
# calcule seu Índice de Massa Corporal (IMC) e mostre seu status,
# de acordo com a tabela abaixo:

# – IMC abaixo de 18,5: Abaixo do Peso
# – Entre 18,5 e 25: Peso Ideal
# – 25 até 30: Sobrepeso
# – 30 até 40: Obesidade
# – Acima de 40: Obesidade Mórbida

# O IMC é calculado dividindo o peso (em kg) pela altura ao quadrado (em m),
# de acordo com a seguinte fórmula: IMC = peso / (altura x altura).

# O resultado de IMC é dado em kg/m2.
# ====================================================================================================

peso = float(input('Qual o seu peso? (Kg) '))
alt = float(input('Qual a sua altura? (m) '))
imc = peso / (alt * alt)  # ou: peso / (alt ** 2)
print(f'O IMC dessa pessoa é de {imc:.1f}')
if imc <= 18.5:
    print('Você está na faixa de peso da, Magreza')  # Abaixo do Peso
elif imc <= 24.9:
    print('Parabens! Você está na faixa de Peso, Normal')  # Peso Ideal
elif imc <= 29.9:
    print('Você está na faixa de, Sobrepeso!')
elif imc <= 34.9:  # Acrescentei o 34.9, porque são dados atualizados de 2024
    print('Você está na faixa de peso, Obesidade grau I')  # Obesidade
elif imc <= 39.9:
    print('Você está na faixa de peso, Obesidade grau II')
else:
    print('Você está na faixa de peso, Obesidade grau III')  # Obesidade Mórbida
