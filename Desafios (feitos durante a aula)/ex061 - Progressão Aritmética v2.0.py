# Refaça o DESAFIO 051, lendo o primeiro termo
# e a razão de uma PA, mostrando os 10 primeiros termos da Progressão
# usando a estrutura while.
print('Gerador de PA')
print('-='*10)
primeiro = int(input('Primeiro termo: '))       # PRIMEIRO TERMO DA PA
razao = int(input('Razão da PA: '))       # RAZÃO = PULAR, A PARTIR DO PRIMEIRO TERMO DE TANTO EM TANTO
termo = primeiro        # Aqui ele mostra o (termo) / contador (termo) começa com o (primeiro) termo que foi solicitado
contador = 1            #E aqui ele mostra quantos termos foram / contador de termo, começa com 1 pq eu quero q ele me mostra os 10 primeiros termos
while contador <= 10:       #Enquanto ele não chegar à 10, ele vai mostrar o termo
    print(f'{termo} -> ', end='')
    termo += razao      # termo recebe o primeiro termo solicitado, depois termo é somado com a razão, dentro de 10 loops
    contador += 1       # contador vai contar os loops, e quando chegar no 10º loop, ele se torna Falso.
print('FIM')
