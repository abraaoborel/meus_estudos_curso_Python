# As principais operações que vamos aprender são o Fatiamento de String,
# Análise com len(), count(), find(),
# transformações com replace(), upper(), lower(), capitalize(), title(), strip(), junção com join().

# Fatiamento:
frase = 'Curso em Vídeo Python'
print(frase[9]) #Resultado: V
print(frase[3]) #Resultado: s
print(frase[3:13]) #Resultado: so em Víde
print(frase[:13]) #Resultado: Curso em Víde
print(frase[13:]) #Resultado: o Python
print(frase[1:15]) #Resultado: urso em Vídeo
print(frase[1:15:2]) #Resultado: us mVdo
print(frase[1::2]) #Resultado: us mVdoPto
print(frase[::2]) #Resultado: Croe íe yhn

# -----------------//--------------------
# Analise:
print(len(frase)) #Quantos caracteres tem na string

print(frase.count('o'))
# importante notar que a letra deve estar em maiuscula ou minuscula na frase
# e mandar buscar a letra/palavra na string da mesma forma que vc pediu

print(frase.upper().count('O'))
# Estou mandando contar a quantidade de 'O' (maíuscula) numa string
# que foi transformada em letras maiusculas

print(frase.count('o', 0, 13))
# .count Ele vai contar quantas vezes aparece a letra 'o',
# virgula 0 e virgula 13 ele vai começar do 0 até o 13 sendo que
# o 13 não vai ser incluido.

print(frase.find('deo'))
# .find vai mostrar onde começa (numero) o caractere

print(frase.find('Android'))
# Quando eu mando buscar uma frase que não tem, como no caso da string
# Android ele me retorna -1 para mostrar que não tem essa palavra na string

print('Curso'in frase)
# comando in para saber se existe essa palavra dentro da string
# -----------------//--------------------

# Transformação:
print(frase.replace('Python','Android'))
# .replace para reposicionar/substituir

print(frase.upper())
# O que já for maiúsculo ele mantém, o que está minúsculo ele troca para maiúsculo

print(frase.lower())
# Faz exatamente o contrario do .upper() deixa tudo minusculo

print(frase.capitalize())
# .capitalize() vai colocar somente o primeiro caractere em maiúsculo e,
# o restante em minúsculo

print(frase.title())
# .title() vai analisar quantas palavras tem na string,
# onde tiver espaços ele vai fazer uma quebra de palavras

frase2 = '   Aprendendo Python  '
# Repara que existe espaços antes da string!

print(frase2.strip())
#.strip vai remover todos os espaços inúteis na string,
# tanto no começo quanto no final, mas os espaços do meio serão mantidos.

print(frase2.rstrip())
# .rstrip onde r significa right removendo somente os ultimos espaços

print(frase2.lstrip())
# .lstrip onde l significa left removendo somente os espaços da esquerda

# -----------------//--------------------
# Divisão:
print(frase.split())
# .split() vai dividir uma string em uma lista

#Junção: obs.: Ainda em combinação com a função split()
print('-'.join(frase))

# Posso utlizar a função print com """ 3 aspas pode ser aspas simples ou duplas,
# para escrever um texto com mais linhas

print('''João 3.16: Porque Deus amou o mundo de tal maneira
que deu seu Filho Unigênito para que todo aquele que nele crê, não
pereça mas tenha a vida eterna''')

dividido = frase.split()
print(dividido[0]) #Resultado: Curso
print(dividido[2][3]) #Resultado: e
